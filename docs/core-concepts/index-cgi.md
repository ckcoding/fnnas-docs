# index.cgi

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/index-cgi/](https://developer.fnnas.com/docs/core-concepts/index-cgi/)

`index.cgi` 是一种基于 CGI 的轻量入口。应用提供可执行的 `app/ui/index.cgi` 文件，用户打开配置好的 CGI URL 时，飞牛 fnOS 会调用该文件。

对于 CGI 入口，`protocol` 和 `port` 会被忽略。请求会沿用当前访问域名，直接按配置的路径访问。飞牛 fnOS 会在调用 CGI 入口前校验 NAS 用户登录态。

## 适用场景

`index.cgi` 适合简单静态页面，或需要兼容轻量包的场景。CGI 只处理普通 HTTP 请求，不支持 WebSocket。

当应用需要后台进程、WebSocket、流式响应、长时间请求、高流量 API 或复杂 API 时，请使用端口服务或统一网关。

## 入口配置

CGI 入口通常使用以下路径：

```text
/cgi/ThirdParty/{appname}/index.cgi/
```

示例：

**app/ui/config**

```json
{
  ".url": {
    "HelloFnos.Application": {
      "title": "Hello fnOS",
      "icon": "images/icon_{0}.png",
      "type": "iframe",
      "protocol": "http",
      "port": "8080",
      "url": "/cgi/ThirdParty/HelloFnos/index.cgi/",
      "allUsers": true
    }
  }
}
```

CGI 请求会使用当前访问域名和配置的 `url` 路径。`protocol` 和 `port` 不参与 CGI 路由。

## 文件位置

将可执行 CGI 文件放在 UI 目录中：

```text
app/ui/index.cgi
```

打包工具会在打包过程中处理可执行权限。如果在设备上手动测试，请确认该文件可以执行。

## 静态文件示例

以下示例会将 `index.cgi` 后面的请求路径映射到已安装的 `www` 目录。

这只是静态文件服务的一种实现方式。应用也可以根据自己的路由需求实现不同的 CGI 逻辑。

**app/ui/index.cgi**

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

## 安全注意事项

请将每个请求路径都视为用户输入。

- 拒绝 .. 等目录穿越路径。
- 只从预期的应用目录提供文件。
- 对缺失或非法文件返回明确状态码。
- 不要直接执行来自请求参数的命令。
- 不要将请求路径拼接到 shell 命令中执行。

---

- 上一页: [应用入口](app-entry.md)
- 下一页: [统一网关](gateway-registration.md)
