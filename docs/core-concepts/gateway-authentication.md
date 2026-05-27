# 🔥 【进阶】登录认证

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/gateway-authentication/](https://developer.fnnas.com/docs/core-concepts/gateway-authentication/)

应用通过统一网关注册后，用户访问时，网关会负责校验用户登录态，并将当前用户信息透传给应用。

> [!WARNING]
> 登录认证能力需要 fnOS **V1.1.3100** 及以上版本支持。

## 认证规则

默认情况下，用户访问经过统一网关的业务请求需要携带有效的系统登录态。统一网关认证通过后，请求才会转发到应用。认证失败的请求不会进入应用服务。

> [!WARNING]
> 统一网关只能确认用户已经登录。应用仍然需要根据自己的业务规则判断用户是否有权限访问具体数据或执行具体操作。

## 用户信息 Header

认证通过后，网关会在转发请求中增加以下 Header：

| Header | 说明 | 示例 |
| --- | --- | --- |
| `X-Trim-Userid` | 当前登录用户的 UID | 1000 |
| `X-Trim-Isadmin` | 当前用户是否为管理员 | true/false |
| `X-Trim-Username` | 当前登录用户名 | admin |

应用可以使用这些 Header 识别当前用户。

**转发到应用的请求示例**

```http
GET /app/trim.app/list HTTP/1.1
X-Trim-Userid: 1000
X-Trim-Isadmin: true
X-Trim-Username: admin
```

## 应用侧示例

**Node.js 示例**

```js
function getGatewayUser(req) {
  return {
    uid: req.headers["x-trim-Userid"],
    isAdmin: req.headers["x-trim-isadmin"] === "true",
    username: req.headers["x-trim-username"]
  };
}
```

应用可以基于 `uid`、`isAdmin` 和 `username` 做业务权限判断。

## 权限判断

应用应继续保留自己的权限判断逻辑。常见场景包括：

- 用户数据隔离时，对应用户的请求只能访问自己的数据
- 提供仅管理员才能访问的管理接口
- 高风险操作需要单独增加校验权限

## WebSocket

WebSocket 服务也应通过统一网关访问。连接建立时，网关会先校验登录态，再将用户信息透传给应用。

应用建立连接后，应将连接与 `X-Trim-Userid` 绑定，后续消息不要信任客户端主动上报的用户 ID。

## 静态文件

如果应用通过统一网关提供静态文件访问，仍需要在应用侧做好路径限制。

建议：

- 对请求路径做标准化处理
- 禁止 .. 访问上级目录，避免目录穿透。
- 限制可访问目录范围
- 不暴露配置文件、密钥、数据库等敏感文件
- 对可下载文件类型做白名单控制

## 不鉴权接口

公开资源、OAuth 回调等特殊接口如果确实不需要登录态，应单独设计路径，并保持最小暴露范围。

不鉴权接口建议满足以下要求：

- 只开放必要路径
- 只允许必要 HTTP 方法
- 不返回用户敏感信息
- 不提供写入、删除等高风险能力

---

- 上一页: [🔥 【进阶】统一网关注册](gateway-registration.md)
- 下一页: [🔥 【进阶】应用依赖关系](dependency.md)
