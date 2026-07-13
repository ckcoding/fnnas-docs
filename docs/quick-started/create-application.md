# 创建应用

> 原始页面: [https://developer.fnnas.com/docs/quick-started/create-application/](https://developer.fnnas.com/docs/quick-started/create-application/)

创建名为 `HelloFnos` 的最小飞牛 fnOS 应用包。该包包含一个通过 `index.cgi` 访问的静态页面，因此不需要应用端口。

---

## 1. 创建项目

```bash
fnpack create HelloFnos
```

本页涉及的关键文件：

- manifest：应用包基础信息
- config/privilege：运行用户模式
- app/www：静态文件
- app/ui/config：桌面入口
- app/ui/index.cgi：静态文件的 CGI 入口

## 2. 添加静态页面

创建 `app/www/index.html`：

**./app/www/index.html**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Hello fnOS</title>
  <style>
    body {
      min-height: 100vh;
      display: grid;
      place-items: center;
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #eef6ff;
      color: #1f2937;
    }
    main {
      text-align: center;
    }
    h1 {
      margin-bottom: 12px;
      font-size: 40px;
    }
  </style>
</head>
<body>
  <main>
    <h1>Hello fnOS</h1>
    <p>Hello fnOS 应用正在运行。</p>
  </main>
</body>
</html>
```

## 3. 配置 manifest

编辑 `manifest`：

**./manifest**

```ini
appname="HelloFnos"
version="1.0.0"
display_name="Hello fnOS"
desc="一个最小的飞牛 fnOS 应用。"
maintainer="Your Name"
maintainer_url="https://example.com"
source="thirdparty"
platform="all"
ctl_stop=false
```

当前应用可适配不同设备架构，因此 `platform` 设置为 `all`。如果应用包含原生二进制或特定架构依赖，请将 `platform` 设置为支持的架构。

`ctl_stop=false` 会隐藏启动和停止控制，因为当前应用只提供静态页面，不运行后台服务。

全部字段请参考 [Manifest](../core-concepts/manifest.md)。

## 4. 配置权限

编辑 `config/privilege`：

**./config/privilege**

```json
{
  "defaults": {
    "run-as": "package"
  },
  "username": "hellofnos",
  "groupname": "hellofnos"
}
```

`package` 表示使用 `username` 和 `groupname` 定义的专用应用用户和用户组运行应用。共享文件夹、Docker 项目、外部运行时和其他资源应在 `config/resource` 中声明。

参考 [应用权限](../core-concepts/privilege.md) 和 [应用资源](../core-concepts/resource.md)。

## 5. 配置桌面入口

创建 `app/ui/config`：

**./app/ui/config**

```json
{
  ".url": {
    "HelloFnos.Application": {
      "title": "Hello fnOS",
      "icon": "images/icon_{0}.png",
      "type": "iframe",
      "url": "/cgi/ThirdParty/HelloFnos/index.cgi/",
      "allUsers": true
    }
  }
}
```

添加入口引用的图标文件，例如 `app/ui/images/icon_64.png` 和 `app/ui/images/icon_256.png`。

CGI 入口不声明端口。服务类应用通常通过应用端口或统一网关暴露 UI。

参考 [应用入口](../core-concepts/app-entry.md)。

## 6. 添加 CGI 入口

创建 `app/ui/index.cgi`：

**./app/ui/index.cgi**

```bash
#!/bin/bash

BASE_PATH="/var/apps/HelloFnos/target/www"
URI_NO_QUERY="${REQUEST_URI%%\?*}"
REL_PATH="/"

case "$URI_NO_QUERY" in
  *index.cgi*)
    REL_PATH="${URI_NO_QUERY#*index.cgi}"
    ;;
esac

if [ -z "$REL_PATH" ] || [ "$REL_PATH" = "/" ]; then
  REL_PATH="/index.html"
fi

TARGET_FILE="${BASE_PATH}${REL_PATH}"

if echo "$TARGET_FILE" | grep -q '\.\.'; then
  echo "Status: 400 Bad Request"
  echo "Content-Type: text/plain; charset=utf-8"
  echo ""
  echo "Bad Request"
  exit 0
fi

if [ ! -f "$TARGET_FILE" ]; then
  echo "Status: 404 Not Found"
  echo "Content-Type: text/plain; charset=utf-8"
  echo ""
  echo "404 Not Found"
  exit 0
fi

case "${TARGET_FILE##*.}" in
  html|htm) mime="text/html; charset=utf-8" ;;
  css) mime="text/css; charset=utf-8" ;;
  js) mime="application/javascript; charset=utf-8" ;;
  png) mime="image/png" ;;
  jpg|jpeg) mime="image/jpeg" ;;
  svg) mime="image/svg+xml" ;;
  *) mime="application/octet-stream" ;;
esac

echo "Content-Type: $mime"
echo ""
cat "$TARGET_FILE"
```

`BASE_PATH` 必须与安装后的应用路径一致。对于 `HelloFnos`，静态文件安装在 `/var/apps/HelloFnos/target/www`。

参考 [index.cgi](../core-concepts/index-cgi.md)。

## 7. 打包应用

在项目目录中运行 `fnpack`：

```bash
fnpack build
```

将生成的 `.fpk` 文件安装到飞牛 fnOS 测试设备。

## 下一步

继续阅读 [测试应用](test-application.md)。

---

- 上一页: [准备工作](prerequisites.md)
- 下一页: [测试应用](test-application.md)
