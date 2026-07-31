# Native 应用案例

> 原始页面: [https://developer.fnnas.com/docs/examples/native/](https://developer.fnnas.com/docs/examples/native/)

Native 应用是在飞牛 fnOS 上运行的进程。它可以提供 Web UI、后台服务、CLI 工具，或这些能力的组合。

这一页从零创建一个 Notepad 示例应用，并将它打包成可以安装运行的 `.fpk` 文件。示例应用包含一个 Node.js 后端服务和一个 React 前端页面，用户可以在页面中编辑笔记，笔记内容会保存到飞牛 fnOS 创建的数据目录中。

本案例使用：

- 项目目录：notepad-demo
- 应用包名：notepad
- 访问方式：统一网关 /app/notepad
- 网关 Socket：app.sock
- 运行时依赖：nodejs_v22

## 创建源码目录

先创建项目目录：

```bash
mkdir -p notepad-demo/backend notepad-demo/frontend/src notepad-demo/scripts
cd notepad-demo
```

目录结构如下：

```text
notepad-demo/
├── backend/
├── frontend/
│   └── src/
└── scripts/
```

## 根目录配置

根目录使用 npm workspace 管理前后端项目：

**notepad-demo/package.json**

```json
{
  "name": "notepad-demo",
  "version": "1.0.0",
  "private": true,
  "workspaces": [
    "frontend",
    "backend"
  ],
  "scripts": {
    "dev:frontend": "npm --workspace frontend run start",
    "dev:backend": "npm --workspace backend run start",
    "build:frontend": "npm --workspace frontend run build",
    "serve:dist": "cross-env FRONTEND_DIST=../frontend/dist npm --workspace backend run start",
    "start": "npm run build:frontend && npm run serve:dist",
    "build": "node scripts/build-combined.js"
  },
  "devDependencies": {
    "cross-env": "^7.0.3"
  }
}
```

## 后端服务

后端提供两个接口：

- GET /api/note：读取笔记内容。
- POST /api/note：保存笔记内容。

创建后端依赖文件：

**notepad-demo/backend/package.json**

```json
{
  "name": "notepad-backend",
  "version": "1.0.0",
  "private": true,
  "main": "server.js",
  "type": "commonjs",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.19.2"
  }
}
```

创建后端服务：

**notepad-demo/backend/server.js**

```js
const express = require("express");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 5001;
const SOCKET_PATH = process.env.SOCKET_PATH || "";
const GATEWAY_PREFIX = process.env.GATEWAY_PREFIX || "/app/notepad";
const DATA_DIR = process.env.DATA_DIR || path.join(__dirname, "data");

app.use(express.json({ limit: "1mb" }));
app.use(express.urlencoded({ extended: true }));

fs.mkdirSync(DATA_DIR, { recursive: true });

const router = express.Router();

function getUserId(req) {
  return req.headers["x-trim-userid"] || "local";
}

function getNoteFile(req) {
  const userId = String(getUserId(req)).replace(/[^a-zA-Z0-9_-]/g, "_");
  return path.join(DATA_DIR, `note-${userId}.txt`);
}

router.get("/api/note", (req, res) => {
  try {
    const noteFile = getNoteFile(req);
    let content = "";
    let updatedAt = null;

    if (fs.existsSync(noteFile)) {
      content = fs.readFileSync(noteFile, "utf8");
      updatedAt = fs.statSync(noteFile).mtime;
    }

    res.json({ content, updatedAt, userId: getUserId(req) });
  } catch (error) {
    res.status(500).json({ error: "Failed to read note" });
  }
});

router.post("/api/note", (req, res) => {
  try {
    const noteFile = getNoteFile(req);
    const content = typeof req.body.content === "string" ? req.body.content : "";

    if (content.length > 1_000_000) {
      return res.status(413).json({ error: "Content too large" });
    }

    fs.writeFileSync(noteFile, content, "utf8");
    res.json({ ok: true, savedAt: fs.statSync(noteFile).mtime });
  } catch (error) {
    res.status(500).json({ error: "Failed to write note" });
  }
});

app.use("/", router);
app.use(GATEWAY_PREFIX, router);

const FRONTEND_DIST = process.env.FRONTEND_DIST;
const LOCAL_PUBLIC = path.join(__dirname, "public");
const STATIC_DIR = FRONTEND_DIST && fs.existsSync(FRONTEND_DIST)
  ? FRONTEND_DIST
  : (fs.existsSync(path.join(LOCAL_PUBLIC, "index.html")) ? LOCAL_PUBLIC : null);

if (STATIC_DIR) {
  app.use(GATEWAY_PREFIX, express.static(STATIC_DIR));
  app.get(`${GATEWAY_PREFIX}/*`, (req, res) => {
    res.sendFile(path.join(STATIC_DIR, "index.html"));
  });

  app.use(express.static(STATIC_DIR));
  app.get("*", (req, res) => {
    res.sendFile(path.join(STATIC_DIR, "index.html"));
  });
}

if (SOCKET_PATH) {
  fs.rmSync(SOCKET_PATH, { force: true });
  app.listen(SOCKET_PATH, () => {
    console.log(`notepad server running on ${SOCKET_PATH}`);
  });
} else {
  app.listen(PORT, () => {
    console.log(`notepad server running at http://localhost:${PORT}`);
  });
}
```

这里使用两个环境变量：

- PORT：本地开发时使用的服务端口。
- SOCKET_PATH：安装到飞牛 fnOS 后使用的 Unix Socket 路径。
- GATEWAY_PREFIX：统一网关访问前缀，本案例使用 /app/notepad。
- DATA_DIR：笔记保存目录。安装到飞牛 fnOS 后，指向 data-share 创建的数据目录。

统一网关会在请求转发时带上 `X-Trim-Userid`。示例使用该 Header 为不同用户保存不同的笔记文件。本地开发时没有这个 Header，会使用 `local` 作为用户标识。

## 前端页面

前端通过相对路径调用后端接口。这样本地运行和安装到飞牛 fnOS 后都不需要写死域名。

创建前端依赖文件：

**notepad-demo/frontend/package.json**

```json
{
  "name": "notepad-frontend",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.1",
    "vite": "^5.4.0"
  }
}
```

创建 Vite 配置：

**notepad-demo/frontend/vite.config.mjs**

```js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  base: "/app/notepad/",
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/app/notepad": "http://localhost:5001"
    }
  }
});
```

创建 HTML 入口：

**notepad-demo/frontend/index.html**

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Notepad</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

创建前端页面：

**notepad-demo/frontend/src/main.jsx**

```jsx
import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";

function App() {
  const [content, setContent] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadNote() {
      try {
        const res = await fetch("/app/notepad/api/note");
        if (!res.ok) throw new Error("Failed to load");
        const data = await res.json();
        setContent(data.content || "");
      } catch (err) {
        setError(err.message || "Failed to load");
      }
    }

    loadNote();
  }, []);

  async function saveNote() {
    try {
      setSaving(true);
      const res = await fetch("/app/notepad/api/note", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content })
      });

      if (!res.ok) throw new Error("Failed to save");
      setError("");
    } catch (err) {
      setError(err.message || "Failed to save");
    } finally {
      setSaving(false);
    }
  }

  return (
    <main style={{ maxWidth: 720, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h1>Notepad</h1>
      <textarea
        value={content}
        onChange={(event) => setContent(event.target.value)}
        rows={12}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
      <div style={{ marginTop: 12 }}>
        <button onClick={saveNote} disabled={saving}>
          {saving ? "Saving..." : "Save"}
        </button>
      </div>
      {error ? <p style={{ color: "crimson" }}>{error}</p> : null}
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
```

## 本地运行

安装依赖：

```bash
npm install --workspaces
```

启动本地预览：

```bash
npm run start
```

访问：

```text
http://localhost:5001/app/notepad
```

如果本地页面可以打开，并且能保存和重新读取笔记，再继续应用打包。本地开发时，前端构建路径和接口路径也使用 `/app/notepad`，用于提前模拟统一网关下的访问路径。

## 创建应用打包目录

在 `notepad-demo/` 目录下创建飞牛 fnOS 应用包目录：

```bash
fnpack create notepad
```

创建后目录结构如下：

```text
notepad-demo/
├── backend/
├── frontend/
├── scripts/
├── notepad/
│   ├── app/
│   ├── cmd/
│   ├── config/
│   │   ├── privilege
│   │   └── resource
│   ├── wizard/
│   ├── manifest
│   ├── LICENSE
│   ├── ICON.PNG
│   └── ICON_256.PNG
├── package-lock.json
└── package.json
```

`notepad/` 是应用包目录。后续运行文件、入口配置、权限和资源声明都放在这个目录中。

## 编辑 manifest

将 `notepad/manifest` 改为：

**notepad-demo/notepad/manifest**

```ini
appname=notepad
version=0.0.1
desc=A simple notepad
display_name=Notepad
maintainer=someone
distributor=someone
platform=all
desktop_uidir=ui
desktop_applaunchname=notepad.main
source=thirdparty
install_dep_apps=nodejs_v22
os_min_version=1.1.3100
ctl_stop=true
```

字段说明：

- appname=notepad 是应用包名。
- platform=all 表示当前包不包含平台相关二进制，能适配不同架构。
- desktop_uidir=ui 表示入口配置位于 app/ui/。
- desktop_applaunchname=notepad.main 表示应用卡片打开 notepad.main 入口。
- install_dep_apps=nodejs_v22 表示应用依赖 Node.js 运行时。
- os_min_version=1.1.3100 表示应用使用统一网关，国内版需要声明最低系统版本。
- 统一网关通过 Socket 转发请求，因此这里不需要声明 service_port。
- ctl_stop=true 表示应用有启动、停止和状态检查逻辑。

更多字段可参考 [Manifest](../core-concepts/manifest.md)。

## 编辑权限

将 `notepad/config/privilege` 改为：

**notepad-demo/notepad/config/privilege**

```json
{
  "defaults": {
    "run-as": "package"
  },
  "username": "notepad",
  "groupname": "notepad"
}
```

这样应用进程会以 `notepad` 用户运行，降低应用异常或漏洞带来的系统风险。更多说明可参考 [应用权限](../core-concepts/privilege.md)。

## 声明数据目录

Notepad 需要保存用户笔记。将 `notepad/config/resource` 改为：

**notepad-demo/notepad/config/resource**

```json
{
  "data-share": {
    "shares": [
      {
        "name": "notepad/notes"
      }
    ]
  }
}
```

安装时，系统会创建该目录，并为应用运行用户授予访问权限。应用运行时可通过 `TRIM_DATA_SHARE_PATHS` 读取系统创建的数据目录，也可以通过 `/var/apps/notepad/share/notes` 软链访问这个目录。

一般情况下不需要写 `permission`。只有需要授权其他应用访问该目录时，再声明额外的访问权限。更多说明可参考 [应用资源](../core-concepts/resource.md)。

## 编辑启停脚本

将 `notepad/cmd/main` 改为：

**notepad-demo/notepad/cmd/main**

```bash
#!/bin/bash

LOG_FILE="${TRIM_PKGVAR}/app.log"
PID_FILE="${TRIM_PKGVAR}/app.pid"

export PATH=/var/apps/nodejs_v22/target/bin:$PATH

APP_DIR="${TRIM_APPDEST}/server"
DATA_DIR="${TRIM_DATA_SHARE_PATHS%%:*}"
GATEWAY_PREFIX="/app/notepad"
SOCKET_PATH="${TRIM_APPDEST}/app.sock"

log_msg() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

check_process() {
  local pid="$1"
  kill -0 "$pid" 2>/dev/null
}

status_app() {
  if [ -f "$PID_FILE" ]; then
    local pid
    pid="$(head -n 1 "$PID_FILE" | tr -d '[:space:]')"
    if [ -n "$pid" ] && check_process "$pid"; then
      return 0
    fi
    rm -f "$PID_FILE"
  fi

  return 1
}

start_app() {
  if status_app; then
    return 0
  fi

  log_msg "Starting Notepad..."
  cd "$APP_DIR" || exit 1
  DATA_DIR="$DATA_DIR" GATEWAY_PREFIX="$GATEWAY_PREFIX" SOCKET_PATH="$SOCKET_PATH" node server.js >> "$LOG_FILE" 2>&1 &
  echo "$!" > "$PID_FILE"
}

stop_app() {
  log_msg "Stopping Notepad..."

  if [ ! -f "$PID_FILE" ]; then
    return 0
  fi

  local pid
  pid="$(head -n 1 "$PID_FILE" | tr -d '[:space:]')"

  if [ -z "$pid" ] || ! check_process "$pid"; then
    rm -f "$PID_FILE"
    return 0
  fi

  kill -TERM "$pid" 2>> "$LOG_FILE" || true

  local count=0
  while check_process "$pid" && [ "$count" -lt 10 ]; do
    sleep 1
    count=$((count + 1))
  done

  if check_process "$pid"; then
    kill -KILL "$pid" 2>> "$LOG_FILE" || true
  fi

  rm -f "$PID_FILE"
  rm -f "$SOCKET_PATH"
}

case "$1" in
  start)
    start_app
    ;;
  stop)
    stop_app
    ;;
  status)
    if status_app; then
      exit 0
    fi
    exit 3
    ;;
  *)
    echo "Unknown command: $1" > "$TRIM_TEMP_LOGFILE"
    exit 1
    ;;
esac
```

这个脚本会：

- 将 Node.js 运行时加入 PATH。
- 从 TRIM_DATA_SHARE_PATHS 获取笔记保存目录。
- 将服务监听到 ${TRIM_APPDEST}/app.sock。
- 启动 server.js，并写入 PID 文件。
- 停止时先发送 TERM，超时后再发送 KILL。

脚本中使用的环境变量可参考 [环境变量](../core-concepts/environment-variables.md)。

## 配置桌面入口

将 `notepad/app/ui/config` 改为：

**notepad-demo/notepad/app/ui/config**

```json
{
  ".url": {
    "notepad.main": {
     "title": "Notepad",
     "icon": "images/icon_{0}.png",
     "type": "iframe",
      "protocol": "",
      "gatewayPrefix": "/app/notepad",
      "gatewaySocket": "app.sock",
      "url": "/app/notepad",
      "allUsers": true
    }
  }
}
```

注意：

- 入口 ID 使用 notepad 作为前缀，并与 manifest 中的 desktop_applaunchname 保持一致。
- icon 使用 {0} 占位时，系统会按尺寸选择 icon_64.png、icon_256.png 等文件。
- gatewaySocket=app.sock 对应生命周期脚本中创建的 ${TRIM_APPDEST}/app.sock。
- protocol 和 port 不参与统一网关路由。
- 通过统一网关访问时，飞牛 fnOS 会先校验 NAS 登录态，再把用户信息通过 Header 转发给应用。

入口配置的更多规则可参考 [应用入口](../core-concepts/app-entry.md)。

## 构建并生成 FPK

创建构建脚本：

**notepad-demo/scripts/build-combined.js**

```js
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const root = path.join(__dirname, "..");
const frontendDir = path.join(root, "frontend");
const backendDir = path.join(root, "backend");
const outDir = path.join(root, "dist");
const packDir = path.join(root, "notepad");
const packServerDir = path.join(packDir, "app", "server");

function run(command, cwd = process.cwd()) {
  execSync(command, { stdio: "inherit", cwd });
}

function emptyDir(dir) {
  if (fs.existsSync(dir)) {
    fs.rmSync(dir, { recursive: true, force: true });
  }
  fs.mkdirSync(dir, { recursive: true });
}

run("npm run build", frontendDir);

emptyDir(outDir);
fs.cpSync(backendDir, outDir, {
  recursive: true,
  filter: (src) => !src.endsWith("node_modules")
});

fs.mkdirSync(path.join(outDir, "public"), { recursive: true });
fs.cpSync(path.join(frontendDir, "dist"), path.join(outDir, "public"), {
  recursive: true
});

const backendPkg = JSON.parse(
  fs.readFileSync(path.join(backendDir, "package.json"), "utf8")
);

fs.writeFileSync(
  path.join(outDir, "package.json"),
  JSON.stringify({
    name: "notepad-combined",
    version: backendPkg.version || "1.0.0",
    private: true,
    main: "server.js",
    type: backendPkg.type || "commonjs",
    scripts: {
      start: "node server.js"
    },
    dependencies: backendPkg.dependencies || {}
  }, null, 2)
);

run("npm install --omit=dev", outDir);

emptyDir(packServerDir);
fs.cpSync(outDir, packServerDir, { recursive: true });

run(`fnpack build --directory ${packDir}`);
```

执行构建：

```bash
npm run build
```

成功后会生成：

```text
notepad.fpk
```

## 安装测试

将 `notepad.fpk` 安装到飞牛 fnOS 测试设备后，检查以下内容：

- 应用是否能正常安装。
- 应用卡片是否能打开 Notepad 页面。
- 不同用户输入笔记后，是否只看到自己的内容。
- 应用是否能启动、停止，并正确返回运行状态。
- 笔记内容是否写入声明的数据目录。
- 日志是否写入 TRIM_PKGVAR 下的日志文件。

如果以上检查都通过，就得到了一个可以运行的 Native 应用包。

---

- 上一页: [应用案例](../category/应用案例.md)
- 下一页: [Docker 应用案例](docker.md)
