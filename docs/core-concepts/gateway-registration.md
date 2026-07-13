# 统一网关

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/gateway-registration/](https://developer.fnnas.com/docs/core-concepts/gateway-registration/)

统一网关为应用提供飞牛 fnOS 访问域名下的稳定系统 URL。发送到网关路径的请求会先由飞牛 fnOS 校验，再转发到应用本地 Unix Socket。

当应用需要复用系统访问域名，同时运行长期服务、支持 WebSocket 或提供 API 时，可以使用统一网关。独立服务访问仍然可以使用端口服务，小型静态页面或简单包兼容场景也可以使用 `index.cgi`。

## 选择访问模型

| 能力 | `index.cgi` | 统一网关 |
| --- | --- | --- |
| 简单静态页面 | 适合 | 支持 |
| 常驻服务 | 不推荐 | 适合 |
| WebSocket | 不支持 | 支持 |
| NAS 登录态 | 调用 CGI 前校验 | 转发到服务前校验，并提供用户 Header |
| 性能 | 每次请求启动 CGI 进程 | 转发到长期运行的服务 |
| 代码适配成本 | 静态页面或简单包通常改造较少 | 服务需要适配网关路由和鉴权 |
| 运行方式 | 每次请求启动 CGI 进程 | 转发到应用服务 |
| 常见路径 | `/cgi/ThirdParty/{appname}/index.cgi/` | `/app/{appname}` |

当应用需要暴露自己的独立服务端口，且不需要接入 NAS 登录态时，可以使用端口服务。

## 工作方式

1. 应用通过 gatewayPrefix 注册公开路径。
2. 应用服务监听 gatewaySocket 声明的 Unix Socket。
3. 用户打开网关路径，例如 /app/myapp。
4. 飞牛 fnOS 校验用户会话。
5. 飞牛 fnOS 将请求转发到 /var/apps/myapp/target/app.sock。
6. 应用在需要用户上下文时读取网关转发的用户 Header。

## 入口配置

在 `app/ui/config` 中声明网关入口：

**app/ui/config**

```json
{
  ".url": {
    "myapp.main": {
      "title": "My App",
      "icon": "images/icon_{0}.png",
      "type": "iframe",
      "protocol": "",
      "gatewayPrefix": "/app/myapp",
      "gatewaySocket": "app.sock",
      "url": "/app/myapp",
      "allUsers": true
    }
  }
}
```

该配置会注册：

```text
/app/myapp
```

请求会转发到：

```text
/var/apps/myapp/target/app.sock
```

统一网关入口由 `gatewayPrefix` 和 `gatewaySocket` 决定。`protocol` 和 `port` 会被忽略，不参与统一网关路由。

## 字段规则

- **`protocol`**：统一网关入口会忽略该字段。
- **`port`**：统一网关入口会忽略该字段。
- **`gatewayPrefix`**
    - 使用 /app/{appname} 或 /app/{appname}/{customPath}。
    - 路径应在版本之间保持稳定。
    - 使用简单、URL 安全的名称。公开路径中避免使用点号。
- **`gatewaySocket`**
    - 只填写 Socket 文件名，例如 app.sock。
    - Socket 文件应放在已安装应用的 target 目录下。
    - 脚本中可使用 ${TRIM_APPDEST} 定位该目录。

## 应用要求

- 应用服务应监听 gatewaySocket 声明的 Unix Socket。
- Docker 应用也可以使用统一网关。将 ${TRIM_APPDEST} 挂载到容器内，并让容器中的服务在该目录下创建对应的 Socket。
- HTTP 和 WebSocket 路由应保持在声明的 gatewayPrefix 下。
- 不要信任客户端传入的用户 ID。请使用飞牛 fnOS 转发的网关鉴权 Header。
- 读取文件或执行用户相关操作前，请验证请求路径和输入。

## 会话校验和用户 Header

应用通过统一网关访问时，飞牛 fnOS 会先校验用户会话，再将请求转发给应用。

网关确认用户已登录。应用仍然需要负责自己的业务鉴权规则。

请求通过认证后，网关会通过 Header 转发用户信息：

| Header | 说明 | 示例 |
| --- | --- | --- |
| `X-Trim-Userid` | 当前用户 UID | `1000` |
| `X-Trim-Isadmin` | 当前用户是否为管理员 | `true` 或 `false` |
| `X-Trim-Username` | 当前用户名 | `admin` |

转发到应用的请求示例：

**Forwarded request**

```http
GET /app/myapp/list HTTP/1.1
X-Trim-Userid: 1000
X-Trim-Isadmin: true
X-Trim-Username: admin
```

应用侧使用：

**Node.js**

```js
function getGatewayUser(req) {
  return {
    uid: req.headers["x-trim-userid"],
    isAdmin: req.headers["x-trim-isadmin"] === "true",
    username: req.headers["x-trim-username"]
  };
}
```

这些值可以作为网关提供的可信身份上下文使用，但应用仍需要执行自己的业务鉴权。

## WebSocket

WebSocket 可以复用同一个网关前缀和 Socket。建议将 WebSocket 路由放在稳定的子路径下，例如：

```text
/app/myapp/ws
```

前端示例：

**WebSocket connection**

```js
const wsProtocol = window.location.protocol === "https:" ? "wss:" : "ws:";
const wsUrl = `${wsProtocol}//${window.location.host}/app/myapp/ws`;

const socket = new WebSocket(wsUrl);

socket.onopen = () => {
  socket.send(JSON.stringify({ type: "ping" }));
};

socket.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log(message);
};
```

通过网关建立的 WebSocket 连接，也会在连接建立时获得同样的身份上下文。连接建立后，应将连接绑定到 `X-Trim-Userid`。

不要信任 WebSocket 消息中由客户端发送的用户 ID。

## 鉴权和安全

网关校验登录状态，不负责业务权限。应用仍应执行以下规则：

- 用户只能访问自己的数据。
- 管理接口需要管理员身份。
- 高风险操作需要明确的权限检查。
- 文件路径和记录 ID 需要结合当前用户进行校验。

如果应用通过网关提供文件访问，请限制文件访问范围：

- 标准化请求路径。
- 拒绝 .. 目录穿越。
- 只从预期目录提供文件。
- 不暴露密钥、数据库、配置文件或私有日志。

OAuth 回调等公开回调路径应保持窄而明确。未鉴权路径只开放所需的 HTTP 方法和数据。

---

- 上一页: [index.cgi](index-cgi.md)
- 下一页: [用户向导](wizard.md)
