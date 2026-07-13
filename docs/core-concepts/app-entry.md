# 应用入口

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/app-entry/](https://developer.fnnas.com/docs/core-concepts/app-entry/)

应用入口定义用户如何从飞牛 fnOS 打开应用，常用于注册桌面图标和注册文件打开方式。默认情况下，入口配置写在 `app/ui/config` 中。

一个应用可以为不同用户任务提供一个或多个入口。本文使用端口服务作为示例，说明如何注册桌面图标，以及如何注册文件打开方式。CGI 和统一网关访问请参考 [index.cgi](index-cgi.md) 和 [统一网关](gateway-registration.md)。

## 入口文件

如果 `manifest` 中使用 `desktop_uidir=ui`，入口配置文件为：

```text
app/ui/config
```

常见结构：

```text
myapp/
├── app/
│   └── ui/
│       ├── config
│       └── images/
│           ├── icon_64.png
│           └── icon_256.png
├── manifest
└── config/
```

入口定义在 `.url` 字段下。入口 ID 应保持稳定，并使用 `appname` 作为前缀，例如 `myapp.main`。

当应用存在多个入口时，可以在 `manifest` 中使用 `desktop_applaunchname` 指定应用中心应用卡片打开的入口。

## 字段

- `title`：用户看到的入口名称。
- `icon`：相对于 UI 目录的图标路径。可使用 {0} 表示不同尺寸的图标，例如 images/icon_{0}.png。
- `type`：打开方式。
    - iframe：在飞牛 fnOS 桌面窗口内打开。
    - url：在浏览器标签页或外部 Web 视图中打开。
- `protocol`：http、https，或使用空字符串交给系统自适应处理。
- `port`：服务端口。需要使用向导中收集的端口时，可以使用 ${wizard_port}。
- `url`：入口打开的路径。需要使用向导中收集的路径时，可以使用 ${wizard_path}。
- `allUsers`：控制入口是否对所有用户可见。
- `fileTypes`：文件入口支持的文件扩展名。
- `noDisplay`：在桌面隐藏入口，但保留文件操作入口。
- `control`：可选字段，用于定义应用设置中的入口设置行为。
    - control.accessPerm=editable：用户可以编辑该设置。
    - control.accessPerm=readonly：用户可以查看但不能编辑。
    - control.accessPerm=hidden：隐藏该设置。

## 注册桌面图标

下面的示例会注册一个桌面图标，用于在飞牛 fnOS 桌面窗口中打开应用服务：

**app/ui/config**

```json
{
  ".url": {
    "myapp.main": {
      "title": "My App",
      "icon": "images/icon_{0}.png",
      "type": "iframe",
      "protocol": "http",
      "port": "8080",
      "url": "/",
      "allUsers": true
    }
  }
}
```

需要在飞牛 fnOS 桌面窗口内打开应用时，使用 `iframe`。需要完整浏览器能力时，使用 `url`。

## 可见性示例

如果某个入口只应对管理员可见，可以使用 `allUsers=false` 和 `control.accessPerm=readonly`：

**app/ui/config**

```json
{
  ".url": {
    "myapp.admin": {
      "title": "Admin Console",
      "icon": "images/admin_{0}.png",
      "type": "iframe",
      "protocol": "http",
      "port": "8080",
      "url": "/admin",
      "allUsers": false,
      "control": {
        "accessPerm": "readonly"
      }
    }
  }
}
```

## 注册文件打开方式

当应用可以从文件管理器右键菜单打开或处理文件时，可以注册文件打开方式。

**app/ui/config**

```json
{
  ".url": {
    "myapp.editor": {
      "title": "Text Editor",
      "icon": "images/editor_{0}.png",
      "type": "iframe",
      "protocol": "http",
      "port": "8080",
      "url": "/edit",
      "allUsers": true,
      "fileTypes": ["txt", "md", "json"],
      "noDisplay": true
    }
  }
}
```

用户通过该入口打开文件时，飞牛 fnOS 会在 URL 后追加 `path` 查询参数。

```text
http://localhost:8080/edit?path=/vol1/Users/admin/Documents/example.txt
```

请将文件路径视为用户输入。读取或修改文件前，需要验证访问权限。

## 访问模型

本文使用端口服务作为示例，因为它最适合展示桌面入口和文件入口的基础定义方式。

- 端口服务：入口打开应用自己的服务端口。这种方式和 NAS 用户登录态无关，适合独立服务。
- CGI：当应用需要一个轻量入口，并在系统访问域名下通过 NAS 登录态校验访问时，参考 index.cgi。
- 统一网关：当应用需要复用系统访问域名、支持 WebSocket，或获取网关提供的用户上下文时，参考 统一网关。

## 入口设计

入口应保持克制。每个入口都应该对应一个明确的用户任务。

- 使用清晰、符合预期的名称。
- 入口 ID 使用应用名称作为前缀。
- 仅限管理员使用的应用，建议同时使用 allUsers=false 和 control.accessPerm=readonly。
- 只声明应用确实支持的文件类型。

---

- 上一页: [应用资源](resource.md)
- 下一页: [index.cgi](index-cgi.md)
