# 应用权限

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/privilege/](https://developer.fnnas.com/docs/core-concepts/privilege/)

`config/privilege` 定义应用以哪个用户身份运行。应使用能满足应用需求的最小权限。

大多数应用应使用专用包用户运行。

## 包用户

**config/privilege**

```json
{
  "defaults": {
    "run-as": "package"
  },
  "username": "myapp_user",
  "groupname": "myapp_group"
}
```

- `run-as`：运行身份。使用 package 表示专用应用用户。
- `username`：专用用户名。省略时，飞牛 fnOS 会根据 manifest.appname 生成。
- `groupname`：专用用户组名。省略时，飞牛 fnOS 会根据 manifest.appname 生成。
- `join-groups`：可选字段，用于添加到应用用户的附加用户组。

使用 `run-as=package` 时，应用进程会以专用应用用户运行。默认情况下，这可以将应用与系统级权限隔离。

## 附加用户组

当应用需要访问由系统用户组权限控制的资源时，可以使用 `join-groups`。

例如，需要访问视频设备、GPU 渲染或硬件加速媒体输出的应用，可能需要通过 `video` 或 `render` 等系统用户组获得对应访问能力。这时可以将 `join-groups` 配置为 `["video", "render"]`。

**config/privilege**

```json
{
  "defaults": {
    "run-as": "package"
  },
  "username": "media_app",
  "groupname": "media_app",
  "join-groups": ["required_system_group"]
}
```

应用仍然以包用户身份运行。`join-groups` 只是将该用户加入指定用户组，以便访问这些用户组允许的资源。

只加入应用确实需要的用户组。每增加一个用户组，应用进程可访问的资源范围都会扩大。

## Root 模式

普通应用运行时不建议使用 Root 模式。以 root 身份运行应用，会放大 Web 处理逻辑、API、后台任务和第三方依赖中的安全风险。

**config/privilege**

```json
{
  "defaults": {
    "run-as": "root"
  },
  "username": "myapp_user",
  "groupname": "myapp_group"
}
```

只有生命周期脚本确实需要执行特权准备任务时，才使用 Root 模式，例如准备系统集成，或访问包用户无法处理的设备。

长期运行并对外提供访问的进程，应尽可能以非 root 用户运行。Root 生命周期脚本可以使用 `runuser` 或同类命令，将服务进程切换到包用户：

**cmd/main**

```bash
runuser -u "$TRIM_USERNAME" -- /var/apps/myapp/target/server/myapp
```

选择 Root 模式前，请先确认是否可以通过资源声明、附加用户组、用户授权或更窄的服务设计来完成同样目标。

## 用户文件访问

应用默认不会获得用户文件的广泛访问权限。需要读取或写入用户数据时，应由用户明确授权目录访问。

目录访问通常有两种方式：

- 用户在应用设置中授权目录。
- 应用在 config/resource 中声明共享数据目录。

共享目录配置请参考 [应用资源](resource.md)。

## 运行用户检查

生命周期脚本可在需要时读取运行用户变量：

**cmd/main**

```bash
#!/bin/bash

echo "Current runtime user: $TRIM_RUN_USERNAME"
echo "Application user: $TRIM_USERNAME"
```

这类检查适合用于诊断。鉴权逻辑应基于明确的应用逻辑和系统提供的访问控制。

## 权限建议

- 默认使用 run-as=package。
- 仅在访问特定用户组保护的资源时使用 join-groups。
- 避免让长期运行或面向用户访问的进程使用 Root 模式。
- 只有没有更窄方案时才请求 Root 模式，并在启动用户可访问服务前降权。
- 仅在业务流程需要时请求用户文件访问。
- 除非用户授权共享位置，否则应用数据应保存在应用目录内。
- 将文件路径、请求参数和用户 ID 都视为不可信输入。

---

- 上一页: [环境变量](environment-variables.md)
- 下一页: [应用资源](resource.md)
