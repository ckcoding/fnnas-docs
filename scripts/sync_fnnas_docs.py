#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag


SITE_ROOT = "https://developer.fnnas.com"
SITEMAP_URL = f"{SITE_ROOT}/sitemap.xml"
REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "docs"
ASSETS_ROOT = REPO_ROOT / "assets"
ALL_DOCS_PATH = REPO_ROOT / "ALL_DOCS.md"
DOCS_INDEX_PATH = DOCS_ROOT / "README.md"
USER_AGENT = "fnnas-docs-sync/1.0 (+https://github.com/your-name/your-repo)"

SECTION_LABELS = {
    "guide": "Entry",
    "quick-started": "Quick Start",
    "core-concepts": "Core Concepts",
    "cli": "CLI Tools",
    "update-log": "Update Logs",
    "category": "Categories",
}

ALERT_MAP = {
    "info": "NOTE",
    "success": "TIP",
    "warning": "WARNING",
    "danger": "CAUTION",
}

INLINE_TAGS = {
    "a",
    "code",
    "em",
    "strong",
    "del",
    "img",
    "span",
    "b",
    "i",
    "kbd",
    "sup",
    "sub",
    "br",
}


@dataclass(frozen=True)
class Page:
    route: str
    source_url: str
    title: str
    soup: BeautifulSoup

    @property
    def output_path(self) -> Path:
        return output_path_for_route(self.route)


def log(message: str) -> None:
    print(message, flush=True)


def normalize_text(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = text.replace("\u200b", "")
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    return text


def collapse_blank_lines(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def normalize_doc_route(path_or_url: str) -> str | None:
    parsed = urlparse(path_or_url)
    path = parsed.path if parsed.scheme else path_or_url
    path = unquote(path.strip())

    if not path.startswith("/docs/"):
        return None

    if path.endswith("/index.html"):
        path = path[: -len("/index.html")]

    if path == "/docs":
        return None

    if not path.endswith("/"):
        path = f"{path}/"

    return path


def source_url_for_route(route: str) -> str:
    return f"{SITE_ROOT}{route}"


def output_path_for_route(route: str) -> Path:
    relative = route.removeprefix("/docs/").strip("/")
    return (DOCS_ROOT / Path(relative)).with_suffix(".md")


def title_from_soup(soup: BeautifulSoup) -> str:
    selectors = [
        ".theme-doc-markdown.markdown h1",
        ".generatedIndexPage_pu2q header h1",
    ]
    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            return node.get_text(" ", strip=True).replace("​", "")

    if soup.title:
        return soup.title.get_text(" ", strip=True).split("|")[0].strip()

    return "Untitled"


def make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        }
    )
    return session


def fetch_sitemap_routes(session: requests.Session) -> list[str]:
    response = session.get(SITEMAP_URL, timeout=30)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    routes: list[str] = []
    seen: set[str] = set()

    for loc in root.findall(".//{*}loc"):
        if not loc.text:
            continue
        route = normalize_doc_route(loc.text)
        if not route or route in seen:
            continue
        seen.add(route)
        routes.append(route)

    return routes


def load_soup(session: requests.Session, url: str) -> BeautifulSoup:
    response = session.get(url, timeout=30)
    response.raise_for_status()
    response.encoding = response.encoding or "utf-8"
    text = response.text.replace("\x00", "")
    return BeautifulSoup(text, "lxml")


class MarkdownConverter:
    def __init__(self, session: requests.Session, route_map: dict[str, Path]) -> None:
        self.session = session
        self.route_map = route_map
        self.download_cache: dict[str, Path | None] = {}

    def convert(self, page: Page) -> str:
        current_output = page.output_path
        content = page.soup.select_one(".theme-doc-markdown.markdown")

        if content:
            parts: list[str] = []
            for child in content.children:
                if not isinstance(child, Tag):
                    continue
                rendered = self.render_block(
                    child,
                    current_output=current_output,
                    current_source_url=page.source_url,
                    skip_h1=True,
                )
                if rendered:
                    parts.append(rendered)
            body = collapse_blank_lines("\n\n".join(parts))
        else:
            generated_index = page.soup.select_one(".generatedIndexPage_pu2q")
            if not generated_index:
                raise RuntimeError(f"Could not find content container for {page.source_url}")
            body = self.render_generated_index(
                generated_index,
                current_output=current_output,
                current_source_url=page.source_url,
            )

        lines = [
            f"# {page.title}",
            "",
            f"> Source: [{page.source_url}]({page.source_url})",
            "",
            body.rstrip(),
        ]

        pagination = self.render_pagination(page.soup, current_output, page.source_url)
        if pagination:
            lines.extend(["", "---", "", pagination.rstrip()])

        return collapse_blank_lines("\n".join(lines))

    def render_generated_index(self, node: Tag, current_output: Path, current_source_url: str) -> str:
        parts: list[str] = []

        header = node.find("header")
        if header:
            for child in header.children:
                if not isinstance(child, Tag):
                    continue
                if child.name == "h1":
                    continue
                rendered = self.render_block(child, current_output, current_source_url)
                if rendered:
                    parts.append(rendered)

        cards: list[str] = []
        for card in node.select(".docCardListItem_ryg4 a.card"):
            href = self.resolve_href(card.get("href", ""), current_output, current_source_url)
            title_node = card.find(["h2", "h3"])
            desc_node = card.find("p")
            title = title_node.get_text(" ", strip=True).replace("📄️", "").strip() if title_node else href
            desc = desc_node.get_text(" ", strip=True) if desc_node else ""
            if desc:
                cards.append(f"- [{title}]({href}): {desc}")
            else:
                cards.append(f"- [{title}]({href})")

        if cards:
            parts.extend(["## Pages", "", *cards])

        return collapse_blank_lines("\n".join(parts))

    def render_pagination(self, soup: BeautifulSoup, current_output: Path, current_source_url: str) -> str:
        items = []
        for label, selector in (("Previous", ".pagination-nav__link--prev"), ("Next", ".pagination-nav__link--next")):
            node = soup.select_one(selector)
            if not node:
                continue
            href = self.resolve_href(node.get("href", ""), current_output, current_source_url)
            text = node.select_one(".pagination-nav__label")
            title = text.get_text(" ", strip=True) if text else node.get_text(" ", strip=True)
            items.append(f"- {label}: [{title}]({href})")
        return "\n".join(items)

    def render_block(
        self,
        node: Tag,
        current_output: Path,
        current_source_url: str,
        *,
        skip_h1: bool = False,
    ) -> str:
        classes = set(node.get("class", []))

        if node.name == "header":
            parts = []
            for child in node.children:
                if isinstance(child, Tag):
                    rendered = self.render_block(
                        child,
                        current_output=current_output,
                        current_source_url=current_source_url,
                        skip_h1=skip_h1,
                    )
                    if rendered:
                        parts.append(rendered)
            return "\n\n".join(parts)

        if re.fullmatch(r"h[1-6]", node.name or ""):
            level = int(node.name[1])
            if skip_h1 and level == 1:
                return ""
            text = self.render_inline_children(node, current_output, current_source_url).strip()
            return f'{"#" * level} {text}' if text else ""

        if node.name == "p":
            return self.render_inline_children(node, current_output, current_source_url).strip()

        if node.name in {"ul", "ol"}:
            return self.render_list(node, current_output, current_source_url, depth=0)

        if node.name == "blockquote":
            body = self.render_container(node, current_output, current_source_url)
            return self.prefix_lines(body, "> ")

        if node.name == "hr":
            return "---"

        if node.name == "table":
            return self.render_table(node, current_output, current_source_url)

        if node.name == "details":
            summary = node.find("summary")
            summary_text = (
                self.render_inline_children(summary, current_output, current_source_url).strip()
                if summary
                else "Details"
            )
            blocks = []
            for child in node.children:
                if child is summary or not isinstance(child, Tag):
                    continue
                rendered = self.render_block(child, current_output, current_source_url)
                if rendered:
                    blocks.append(rendered)
            body = self.prefix_lines("\n\n".join(blocks), "> ")
            return f"> [!NOTE]\n> {summary_text}\n>\n{body}"

        if node.name == "pre":
            return self.render_pre(node)

        if node.name == "div" and "theme-code-block" in classes:
            return self.render_code_block(node)

        if node.name == "div" and "theme-admonition" in classes:
            return self.render_admonition(node, current_output, current_source_url)

        if node.name == "div":
            return self.render_container(node, current_output, current_source_url)

        return self.render_container(node, current_output, current_source_url)

    def render_container(self, node: Tag, current_output: Path, current_source_url: str) -> str:
        parts = []
        for child in node.children:
            if isinstance(child, NavigableString):
                text = normalize_text(str(child)).strip()
                if text:
                    parts.append(text)
                continue
            if not isinstance(child, Tag):
                continue
            if child.name in INLINE_TAGS:
                text = self.render_inline(child, current_output, current_source_url).strip()
                if text:
                    parts.append(text)
                continue
            rendered = self.render_block(child, current_output, current_source_url)
            if rendered:
                parts.append(rendered)
        return "\n\n".join(parts)

    def render_list(self, node: Tag, current_output: Path, current_source_url: str, depth: int) -> str:
        lines = []
        ordered = node.name == "ol"
        for index, item in enumerate(node.find_all("li", recursive=False), start=1):
            lines.extend(
                self.render_list_item(
                    item,
                    current_output=current_output,
                    current_source_url=current_source_url,
                    depth=depth,
                    ordered=ordered,
                    index=index,
                )
            )
        return "\n".join(lines)

    def render_list_item(
        self,
        node: Tag,
        current_output: Path,
        current_source_url: str,
        depth: int,
        ordered: bool,
        index: int,
    ) -> list[str]:
        indent = "  " * depth
        marker = f"{index}. " if ordered else "- "

        inline_parts: list[str] = []
        blocks: list[str] = []

        for child in node.children:
            if isinstance(child, NavigableString):
                text = normalize_text(str(child))
                if text.strip():
                    inline_parts.append(text)
                continue

            if not isinstance(child, Tag):
                continue

            if child.name in INLINE_TAGS or child.name == "p":
                text = self.render_inline_children(child, current_output, current_source_url).strip()
                if text:
                    inline_parts.append(text)
                continue

            if child.name in {"ul", "ol"}:
                if inline_parts:
                    blocks.append("".join(inline_parts).strip())
                    inline_parts = []
                blocks.append(self.render_list(child, current_output, current_source_url, depth + 1))
                continue

            if inline_parts:
                blocks.append("".join(inline_parts).strip())
                inline_parts = []

            rendered = self.render_block(child, current_output, current_source_url)
            if rendered:
                blocks.append(rendered)

        if inline_parts:
            blocks.insert(0, "".join(inline_parts).strip())

        if not blocks:
            return [f"{indent}{marker}"]

        first = blocks[0]
        remaining = blocks[1:]
        lines = [f"{indent}{marker}{first}"]
        nested_indent = indent + "  "
        for block in remaining:
            for line in block.splitlines():
                lines.append(f"{nested_indent}{line}" if line else "")
        return lines

    def render_admonition(self, node: Tag, current_output: Path, current_source_url: str) -> str:
        classes = " ".join(node.get("class", []))
        kind = "NOTE"
        for source_kind, github_kind in ALERT_MAP.items():
            if f"theme-admonition-{source_kind}" in classes:
                kind = github_kind
                break

        content = node.select_one(".admonitionContent_IXtt") or node
        body_blocks = []
        for child in content.children:
            if isinstance(child, Tag):
                rendered = self.render_block(child, current_output, current_source_url)
                if rendered:
                    body_blocks.append(rendered)

        body = "\n\n".join(body_blocks).strip()
        if not body:
            return f"> [!{kind}]"

        return f"> [!{kind}]\n{self.prefix_lines(body, '> ')}"

    def render_code_block(self, node: Tag) -> str:
        title_node = node.select_one(".codeBlockTitle_QcLQ")
        pre = node.find("pre")
        if not pre:
            return ""

        body = self.render_pre(pre)
        if title_node:
            title = title_node.get_text(" ", strip=True)
            return f"**{title}**\n\n{body}"
        return body

    def render_pre(self, node: Tag) -> str:
        classes = " ".join(node.get("class", []))
        match = re.search(r"language-([A-Za-z0-9_+-]+)", classes)
        language = match.group(1) if match else ""

        token_lines = node.select(".token-line")
        if token_lines:
            body = "\n".join(line.get_text("", strip=False).rstrip() for line in token_lines)
        else:
            body = node.get_text("", strip=False)

        body = body.rstrip("\n")
        return f"```{language}\n{body}\n```"

    def render_table(self, node: Tag, current_output: Path, current_source_url: str) -> str:
        rows = []
        for tr in node.find_all("tr"):
            cells = tr.find_all(["th", "td"], recursive=False)
            if not cells:
                continue
            row = []
            for cell in cells:
                text = self.render_inline_children(cell, current_output, current_source_url).strip()
                row.append(text.replace("|", r"\|"))
            rows.append(row)

        if not rows:
            return ""

        width = max(len(row) for row in rows)
        normalized_rows = []
        for row in rows:
            normalized_rows.append(row + [""] * (width - len(row)))

        header = normalized_rows[0]
        separator = ["---"] * width
        lines = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join(separator) + " |",
        ]
        for row in normalized_rows[1:]:
            lines.append("| " + " | ".join(row) + " |")
        return "\n".join(lines)

    def render_inline_children(self, node: Tag, current_output: Path, current_source_url: str) -> str:
        parts = []
        for child in node.children:
            if isinstance(child, NavigableString):
                parts.append(normalize_text(str(child)))
            elif isinstance(child, Tag):
                parts.append(self.render_inline(child, current_output, current_source_url))

        text = "".join(parts)
        text = text.replace("​", "")
        text = re.sub(r" *\n *", "\n", text)
        text = re.sub(r" {2,}", " ", text)
        return text

    def render_inline(self, node: Tag, current_output: Path, current_source_url: str) -> str:
        if node.name == "br":
            return "  \n"

        if node.name == "code":
            text = node.get_text("", strip=False).replace("`", r"\`")
            return f"`{text}`" if "\n" not in text else f"``{text}``"

        if node.name in {"strong", "b"}:
            text = self.render_inline_children(node, current_output, current_source_url).strip()
            return f"**{text}**"

        if node.name in {"em", "i"}:
            text = self.render_inline_children(node, current_output, current_source_url).strip()
            return f"*{text}*"

        if node.name == "del":
            text = self.render_inline_children(node, current_output, current_source_url).strip()
            return f"~~{text}~~"

        if node.name == "span":
            text = self.render_inline_children(node, current_output, current_source_url)
            classes = " ".join(node.get("class", [])).lower()
            if "badge" in classes:
                return f" {text.strip()}"
            return text

        if node.name == "a":
            if "hash-link" in node.get("class", []):
                return ""
            href = self.resolve_href(node.get("href", ""), current_output, current_source_url)
            text = self.render_inline_children(node, current_output, current_source_url).strip() or href
            return f"[{text}]({href})"

        if node.name == "img":
            src = self.resolve_url(node.get("src", ""), current_source_url)
            local = self.download_image(src)
            href = self.relative_path(current_output, local) if local else src
            alt = node.get("alt", "").strip()
            return f"![{alt}]({href})"

        return self.render_inline_children(node, current_output, current_source_url)

    def resolve_href(self, href: str, current_output: Path, current_source_url: str) -> str:
        absolute = self.resolve_url(href, current_source_url)
        if not absolute:
            return ""

        parsed = urlparse(absolute)

        if parsed.scheme in {"mailto", "tel"}:
            return absolute

        doc_route = normalize_doc_route(parsed.path)
        if parsed.netloc in {"developer.fnnas.com", "fnnas.com"} and doc_route:
            target = self.route_map.get(doc_route)
            if target:
                if target == current_output and parsed.fragment:
                    return f"#{parsed.fragment}"
                relative = self.relative_path(current_output, target)
                return f"{relative}#{parsed.fragment}" if parsed.fragment else relative

        return absolute

    @staticmethod
    def resolve_url(href: str, current_source_url: str) -> str:
        if not href:
            return ""
        return urljoin(current_source_url, href)

    def download_image(self, absolute_url: str) -> Path | None:
        if not absolute_url:
            return None

        parsed = urlparse(absolute_url)
        if parsed.scheme not in {"http", "https"}:
            return None

        if absolute_url in self.download_cache:
            return self.download_cache[absolute_url]

        target: Path | None = None

        if parsed.netloc in {"developer.fnnas.com", "fnnas.com"} and parsed.path.startswith(("/assets/", "/img/")):
            target = ASSETS_ROOT / "site" / parsed.path.lstrip("/")
        elif parsed.netloc == "static.fnnas.com":
            target = ASSETS_ROOT / "static" / parsed.path.lstrip("/")

        if target is None:
            self.download_cache[absolute_url] = None
            return None

        target.parent.mkdir(parents=True, exist_ok=True)
        response = self.session.get(absolute_url, timeout=30)
        response.raise_for_status()
        target.write_bytes(response.content)

        self.download_cache[absolute_url] = target
        return target

    @staticmethod
    def relative_path(current_output: Path, target: Path) -> str:
        return Path(shutil.os.path.relpath(target, current_output.parent)).as_posix()

    @staticmethod
    def prefix_lines(text: str, prefix: str) -> str:
        return "\n".join(f"{prefix}{line}" if line else prefix.rstrip() for line in text.splitlines())


def build_route_map(pages: list[Page]) -> dict[str, Path]:
    route_map: dict[str, Path] = {}
    for page in pages:
        route_map[page.route] = page.output_path
        route_map[page.route.rstrip("/")] = page.output_path
        route_map[f"{page.route}index.html"] = page.output_path
    return route_map


def prepare_output_directories() -> None:
    for path in (DOCS_ROOT, ASSETS_ROOT):
        if path.exists():
            shutil.rmtree(path)
    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    ASSETS_ROOT.mkdir(parents=True, exist_ok=True)


def fetch_pages(session: requests.Session) -> list[Page]:
    routes = fetch_sitemap_routes(session)
    pages: list[Page] = []

    for route in routes:
        url = source_url_for_route(route)
        log(f"Fetching {url}")
        soup = load_soup(session, url)
        title = title_from_soup(soup)
        pages.append(Page(route=route, source_url=url, title=title, soup=soup))

    return pages


def write_docs_index(pages: list[Page]) -> None:
    grouped: dict[str, list[Page]] = {}
    for page in pages:
        key = page.route.removeprefix("/docs/").split("/", 1)[0]
        grouped.setdefault(key, []).append(page)

    lines = [
        "# fnOS Developer Docs",
        "",
        "Auto-generated from `https://developer.fnnas.com/docs/guide/`.",
        "",
        f"- Combined file: [../{ALL_DOCS_PATH.name}](../{ALL_DOCS_PATH.name})",
        "",
        "## Index",
        "",
    ]

    for section, section_pages in grouped.items():
        lines.append(f"### {SECTION_LABELS.get(section, section)}")
        lines.append("")
        for page in section_pages:
            relative = page.output_path.relative_to(DOCS_ROOT).as_posix()
            lines.append(f"- [{page.title}]({relative})")
        lines.append("")

    DOCS_INDEX_PATH.write_text(collapse_blank_lines("\n".join(lines)), encoding="utf-8")


def write_all_docs(pages: list[Page]) -> None:
    lines = [
        "# fnOS Developer Docs",
        "",
        "This file is auto-generated. It concatenates the Markdown pages into a single document.",
        "",
        "- Index: [docs/README.md](docs/README.md)",
        "",
        "## Contents",
        "",
    ]

    for page in pages:
        relative = page.output_path.relative_to(REPO_ROOT).as_posix()
        lines.append(f"- [{page.title}]({relative})")

    for page in pages:
        content = page.output_path.read_text(encoding="utf-8")
        body = re.sub(r"^# .+\n\n> Source: .+\n\n", "", content, count=1)
        lines.extend(
            [
                "",
                "---",
                "",
                f"## {page.title}",
                "",
                body.strip(),
            ]
        )

    ALL_DOCS_PATH.write_text(collapse_blank_lines("\n".join(lines)), encoding="utf-8")


def run() -> None:
    prepare_output_directories()

    with make_session() as session:
        pages = fetch_pages(session)
        route_map = build_route_map(pages)
        converter = MarkdownConverter(session, route_map)

        for page in pages:
            markdown = converter.convert(page)
            page.output_path.parent.mkdir(parents=True, exist_ok=True)
            page.output_path.write_text(markdown, encoding="utf-8")

        write_docs_index(pages)
        write_all_docs(pages)

    log(f"Wrote {len(pages)} pages into {DOCS_ROOT}")


if __name__ == "__main__":
    try:
        run()
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
