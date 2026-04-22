# fnOS Developer Docs Sync

This repository syncs the public fnOS developer documentation from `https://developer.fnnas.com/docs/guide/`, converts it to GitHub-friendly Markdown, downloads referenced images, and commits the result automatically.

## Files

- `scripts/sync_fnnas_docs.py`: crawl + convert entrypoint
- `docs/`: generated Markdown pages
- `assets/`: generated local images
- `ALL_DOCS.md`: generated single-file merged version
- `.github/workflows/sync.yml`: daily GitHub Actions workflow

## Local run

```bash
pip install -r requirements.txt
python scripts/sync_fnnas_docs.py
```

## GitHub Actions

The workflow runs once per day at `01:00 UTC`, which is `09:00` in China Standard Time.

If you publish this repo to GitHub, make sure:

1. Actions are enabled.
2. Repository `Settings -> Actions -> General -> Workflow permissions` allows `Read and write permissions`.
3. The default branch accepts pushes from `GITHUB_TOKEN`.

## Notes

- The script uses the sitemap to discover doc pages, so newly added pages should be picked up automatically.
- Generated files under `docs/`, `assets/`, and `ALL_DOCS.md` are meant to be committed.
- The source site mixes canonical `fnnas.com` URLs with actual downloadable `developer.fnnas.com` pages. The script normalizes this automatically.
