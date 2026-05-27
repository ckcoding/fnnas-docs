# 🔥 【进阶】统一网关注册

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/gateway-registration/](https://developer.fnnas.com/docs/core-concepts/gateway-registration/)

统一网关用于为应用提供稳定的访问入口。应用接入后，无需新增端口监听，用户可以通过系统地址和应用路径访问服务。

例如当前系统 Web UI 访问地址是 `http://192.168.1.10:5666/`，则应用访问地址可以是 `http://192.168.1.10:5666/app/{appname}`

> [!WARNING]
> 统一网关注册能力需要 fnOS **V1.1.3100** 及以上版本支持。

> [!NOTE]
> 统一网关会在转发请求前完成登录态校验，自动拒绝非法访问。HTTP 和 WebSocket 请求均可通过统一网关接入。

## 接入方式

在应用入口配置 `app/ui/config` 中声明 `gatewayPrefix` 和 `gatewaySocket` 即可接入统一网关。

满足以下条件时，系统会为该入口注册网关路由：

- gatewayPrefix 不为空且符合格式规范
- gatewaySocket 不为空

## 字段说明

- `gatewayPrefix` - 应用注册到网关的访问前缀
    - 格式为 /app/{appname}/{customPath} 或 /app/{appname}
    - {appname}为应用包名
    - {customPath} 为自定义路径，非必须，推荐使用简短、稳定的业务路径
    - 需确认本字段未包含 .，如有请使用 - 替换
- `gatewaySocket` - 应用接收网关请求的 Socket 文件名
    - 只填写文件名，例如 app.sock
    - 不需要填写完整路径
    - Socket 文件应放在应用 target 目录下，可使用环境变量 ${TRIM_APPDEST} 获取该路径

## 配置示例

**app/ui/config**

```json
{
    ".url": {
        "trim.app": {
            "title": "应用A",
            "desc": "应用A",
            "icon": "images/icon_{0}.png",
            "type": "iframe",
            "protocol": "",
            "gatewaySocket": "app.sock",
            "gatewayPrefix": "/app/trim-app",
            "url": "/app/trim-app",
            "allUsers": true
        }
    }
}
```

以上配置会注册访问入口：

```text
/app/trim-app
```

匹配该前缀的请求会转发到：

```text
/var/apps/trim.app/target/app.sock
```

## WebSocket 使用说明

WebSocket 服务可以复用同一个 `gatewayPrefix` 和 `gatewaySocket`。网关会将匹配前缀的 WebSocket Upgrade 请求转发到应用 Socket，应用按普通 WebSocket 服务处理连接即可。

建议将 WebSocket 路由放在应用网关前缀下的固定子路径中，例如：

```text
/app/trim-app/ws
```

### WebSocket 配置示例

**app/ui/config**

```json
{
    ".url": {
        "trim.chat": {
            "title": "聊天应用",
            "desc": "聊天应用",
            "icon": "images/icon_{0}.png",
            "type": "iframe",
            "protocol": "",
            "gatewaySocket": "chat.sock",
            "gatewayPrefix": "/app/trim-chat",
            "url": "/app/trim-chat",
            "allUsers": true
        }
    }
}
```

以上配置中：

- HTTP 访问入口为 /app/trim-chat
- WebSocket 建议使用 /app/trim-chat/ws
- 请求会转发到 /var/apps/trim.chat/target/chat.sock

### 前端连接示例

前端建议根据当前页面协议自动选择 `ws` 或 `wss`：

**WebSocket 连接示例**

```js
const wsProtocol = window.location.protocol === "https:" ? "wss:" : "ws:";
const wsUrl = `${wsProtocol}//${window.location.host}/app/trim-chat/ws`;

const socket = new WebSocket(wsUrl);

socket.onopen = () => {
  socket.send(JSON.stringify({ type: "ping" }));
};

socket.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log(message);
};
```

### 应用侧要求

- WebSocket 服务应监听 gatewaySocket 对应的 Unix Socket。
- WebSocket 路由建议固定为网关前缀下的子路径，例如 /ws。
- 不要使用客户端传入的用户 ID 判断身份，应使用登录认证中说明的 X-Trim-* Header。
- 建立连接后，建议将连接与当前用户 UID 绑定，后续消息按该用户身份处理。

---

- 上一页: [📚 【基础】用户向导](wizard.md)
- 下一页: [🔥 【进阶】登录认证](gateway-authentication.md)
