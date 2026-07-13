# 飞牛开发文档合集

这个文件由脚本自动生成，用于把整套 Markdown 文档合并成单文件版本，方便全文检索、归档或导入知识库。

- 文档索引: [docs/README.md](docs/README.md)

## 目录

- [欢迎加入飞牛应用开发者平台](docs/guide.md)
- [🚀　快速开始](docs/category/快速开始.md)
- [📘　开发指南](docs/category/开发指南.md)
- [🧩　应用案例](docs/category/应用案例.md)
- [🛠️　开发工具](docs/category/️开发工具.md)
- [📝　更新日志](docs/category/更新日志.md)
- [准备工作](docs/quick-started/prerequisites.md)
- [应用框架](docs/core-concepts/framework.md)
- [fnpack](docs/cli/fnpack.md)
- [创建应用](docs/quick-started/create-application.md)
- [测试应用](docs/quick-started/test-application.md)
- [上架应用](docs/quick-started/publish-application.md)
- [Manifest](docs/core-concepts/manifest.md)
- [环境变量](docs/core-concepts/environment-variables.md)
- [应用权限](docs/core-concepts/privilege.md)
- [应用资源](docs/core-concepts/resource.md)
- [应用入口](docs/core-concepts/app-entry.md)
- [index.cgi](docs/core-concepts/index-cgi.md)
- [统一网关](docs/core-concepts/gateway-registration.md)
- [用户向导](docs/core-concepts/wizard.md)
- [应用依赖](docs/core-concepts/dependency.md)
- [中间件服务](docs/core-concepts/middleware.md)
- [运行时环境](docs/core-concepts/runtime.md)
- [图标](docs/core-concepts/icon.md)
- [Native 应用案例](docs/examples/native.md)
- [Docker 应用案例](docs/examples/docker.md)
- [appcenter-cli](docs/cli/appcentercli.md)
- [2026-07-05](docs/update-log/20260705.md)
- [2026-05-09](docs/update-log/20260509.md)
- [2025-12-31](docs/update-log/20251231.md)
- [2025-12-16](docs/update-log/20251216.md)

---

## 欢迎加入飞牛应用开发者平台

飞牛 fnOS 是一款年轻而强大的 NAS 操作系统。自2024年8月开放公测以来，截止2025年8月公测一周年之际，系统装机量已经超过 **90万**，APP设备数也已突破 **120万**。

我们的目标很简单：把飞牛 fnOS 打造成 **“存储系统界的 Windows”**。

我们相信，丰富的应用生态是实现这一目标的关键要素，而优秀的开发者是生态的核心驱动力。我们将以服务好开发者为导向，持续建设开发者平台，从而让更多飞牛用户受益。

---

## 为什么在飞牛 fnOS 上开发应用？

我们的用户覆盖家庭与中小企业，围绕娱乐、数据管理、备份协作等需求，存在大量可落地的应用机会。无论是面向大众的产品，还是解决小众但刚需的问题，只要是对用户有价值的应用，我们都欢迎。

用户之所以选择 NAS 与飞牛 fnOS，我们认为核心是以下原因，供您参考：

### 1. 数据安全与隐私

- 数据在本地自主管理，避免不必要的外部依赖
- 可控的访问与授权，满足个人与企业的隐私诉求

### 2. 私有本地服务器，场景丰富

- 家庭娱乐中心：支持在不同设备里播放 NAS 中的照片、视频与音乐，包括手机、平板、电脑、TV 等设备
- 本地 AI 与算力：部署智能相册等本地应用，享受 AI 的便利，同时数据不外流
- 备份与同步枢纽：手机与电脑自动/定时备份，并提供版本快照功能，实现历史回溯

### 3. 企业级能力与扩展

- 文件共享与协作：支持多人文件共享和权限精细化管理，实现团队间的高效协作
- 数字化办公：可将 NAS 作为数字化办公的存储容器，不仅容量无限传输极速，同时满足数据安全与合规性
- 定制工作台：通过应用中心和Docker快速部署各种应用服务，为企业运作效率提速

---

## 学习路径

通过本文档，你可以系统掌握：

### 1. 开发指南

- 完整流程：从创建、打包到发布
- 核心概念：应用架构与运行机制
- 最佳实践：稳定性、权限与资源管控

### 2. 开发工具

- fnpack：应用打包工具
- appcenter-cli：应用中心命令行工具

---

## 开始飞牛 fnOS 开发之旅

- 阅读 快速开始 掌握开发测试流程
- 查看 开发指南 理解应用架构
- 学习 CLI 工具 提升开发效率

---

- 下一页: [🚀　快速开始](category/快速开始.md)

---

## 🚀　快速开始

跟随以下步骤，快速实现一个应用开发和测试发布
## 本页内容

- [准备工作](../quick-started/prerequisites.md): 在开发飞牛 fnOS 应用前，准备测试设备、开发机、访问权限和工具
- [创建应用](../quick-started/create-application.md): 创建一个最小飞牛 fnOS 应用包
- [测试应用](../quick-started/test-application.md): 安装并验证飞牛 fnOS 应用包
- [上架应用](../quick-started/publish-application.md): 准备发布飞牛 fnOS 应用

---

- 上一页: [欢迎加入](../guide.md)
- 下一页: [准备工作](../quick-started/prerequisites.md)

---

## 📘　开发指南

学习应用的架构与运行机制、应用设计规范和核心开发概念。
## 本页内容

- [应用框架](../core-concepts/framework.md): 理解飞牛 fnOS 应用目录和生命周期
- [Manifest](../core-concepts/manifest.md): 定义应用元数据、兼容范围和运行方式
- [环境变量](../core-concepts/environment-variables.md): 使用运行时提供的环境变量
- [应用权限](../core-concepts/privilege.md): 定义应用运行用户和权限模型
- [应用资源](../core-concepts/resource.md): 声明应用资源和系统集成
- [应用入口](../core-concepts/app-entry.md): 定义用户打开和访问应用的方式
- [index.cgi](../core-concepts/index-cgi.md): 通过 index.cgi 提供轻量 UI
- [统一网关](../core-concepts/gateway-registration.md): 通过统一网关注册应用路由并使用网关鉴权
- [用户向导](../core-concepts/wizard.md): 定义安装、升级、卸载和配置表单
- [应用依赖](../core-concepts/dependency.md): 声明应用依赖
- [中间件服务](../core-concepts/middleware.md): 在飞牛 fnOS 应用中使用中间件服务
- [运行时环境](../core-concepts/runtime.md): 使用打包运行时环境
- [图标](../core-concepts/icon.md): 准备应用图标

---

- 上一页: [上架应用](../quick-started/publish-application.md)
- 下一页: [应用框架](../core-concepts/framework.md)

---

## 🧩　应用案例

通过完整案例学习如何构建、打包和测试应用。
## 本页内容

- [Native 应用案例](../examples/native.md): 从零创建一个可运行的 Native 应用包
- [Docker 应用案例](../examples/docker.md): 从零创建一个可运行的 Docker 应用包

---

- 上一页: [图标](../core-concepts/icon.md)
- 下一页: [Native 应用案例](../examples/native.md)

---

## 🛠️　开发工具

了解飞牛 fnOS 应用开发常用命令行工具。
## 本页内容

- [fnpack](../cli/fnpack.md): 创建和打包飞牛 fnOS 应用
- [appcenter-cli](../cli/appcentercli.md): 通过命令行管理应用安装和测试

---

- 上一页: [Docker 应用案例](../examples/docker.md)
- 下一页: [fnpack](../cli/fnpack.md)

---

## 📝　更新日志

查看开发者文档的主要更新记录。
## 本页内容

- [2026-07-05](../update-log/20260705.md): 2026-07-05 文档更新记录
- [2026-05-09](../update-log/20260509.md): 2026-05-09 文档更新记录
- [2025-12-31](../update-log/20251231.md): 2025-12-31 文档更新记录
- [2025-12-16](../update-log/20251216.md): 2025-12-16 文档更新记录

---

- 上一页: [appcenter-cli](../cli/appcentercli.md)
- 下一页: [2026-07-05](../update-log/20260705.md)

---

## 准备工作

在创建第一个飞牛 fnOS 应用前，你需要准备两个环境：

- 一台用于安装和运行应用的 飞牛 fnOS 测试设备
- 一台用于编写代码、创建应用包并连接测试设备的 开发电脑

这一页只关注创建和测试第一个应用所需的最小准备。

---

## 1. 准备并检查飞牛 fnOS 测试设备

建议尽量使用专门的测试设备。开发过程中，你可能会频繁安装、卸载、重启和修改应用，因此不建议使用存放重要个人或业务数据的设备作为开发测试机。

> [!TIP]
> 你可以从 [飞牛官网](https://www.fnnas.com/download?key=fnos) 下载最新安装镜像。安装步骤可参考 [飞牛 fnOS 安装指南](https://help.fnnas.com/articles/fnosV1/start/install-os)。

开始应用开发前，请确保测试设备已完成初始化，并且可以通过浏览器访问。

先确认几个必需项：

- 初始化状态：设备已完成首次初始化流程
- 管理员账号：可以使用管理员账号登录
- 网络访问：开发电脑可以访问飞牛 fnOS 设备
- 存储可用性：设备已有可用于安装应用的存储空间

飞牛 fnOS 支持主流 x86 和 ARM 架构硬件。对于第一个应用，你只需要知道当前用哪台设备测试。等到构建特定架构应用，或应用对资源有更高要求时，再根据目标设备选择构建目标和依赖。

## 2. 准备开发电脑

你可以在自己的电脑上本地开发，然后将打包好的应用安装到飞牛 fnOS 上测试。需要更贴近目标设备环境时，也可以使用远程开发方式。

开发电脑应准备：

- 代码编辑器或 IDE
- 终端环境
- 到飞牛 fnOS 测试设备的网络访问

应用需要的运行时可以按需安装，例如 Node.js、Python、Java、Go 或其他 Linux 兼容工具。

## 3. 准备访问权限

应用测试通常需要飞牛 fnOS 设备的管理员权限。

你可能需要管理员权限来完成：

- 安装和卸载本地应用包
- 使用仅用于测试的安装入口
- 查看日志并排查运行问题

如果是多人协作开发，请提前约定使用哪台测试设备、哪个账号以及哪个存储空间。

## 4. 准备 CLI 工具

飞牛 fnOS 应用开发主要会用到两个工具：

- fnpack：创建应用项目，并将应用打包为 .fpk 文件
- appcenter-cli：在飞牛 fnOS 设备上安装本地包、管理应用测试，并处理应用中心相关流程

常见流程是：

1. 在开发电脑上使用 fnpack 创建项目并打包应用
2. 将 .fpk 包复制或部署到飞牛 fnOS 测试设备
3. 使用 appcenter-cli 或应用中心安装并测试应用包

## 检查清单

继续之前，请确认：

- 已准备飞牛 fnOS 测试设备
- 设备已完成初始化
- 至少一个存储空间可用
- 你拥有管理员权限
- 开发电脑可以通过网络访问设备
- 已了解 fnpack 和 appcenter-cli

准备完成后，继续阅读 [创建应用](create-application.md)。

---

- 上一页: [🚀　快速开始](../category/快速开始.md)
- 下一页: [创建应用](create-application.md)

---

## 应用框架

飞牛 fnOS 应用包包含元数据、配置文件、生命周期脚本、UI 资源和应用运行文件。

安装后，飞牛 fnOS 会在 `/var/apps/{appname}` 下创建应用目录结构。

## 安装后的目录

```text
/var/apps/{appname}
├── cmd/
│   ├── install_init
│   ├── install_callback
│   ├── main
│   ├── upgrade_init
│   ├── upgrade_callback
│   ├── uninstall_init
│   ├── uninstall_callback
│   ├── config_init
│   └── config_callback
├── config/
│   ├── privilege
│   └── resource
├── manifest
├── ICON.PNG
├── ICON_256.PNG
├── target -> /vol{n}/@appcenter/{appname}
├── etc    -> /vol{n}/@appconf/{appname}
├── var    -> /vol{n}/@appdata/{appname}
├── tmp    -> /vol{n}/@apptemp/{appname}
├── home   -> /vol{n}/@apphome/{appname}
├── meta
├── shares/
└── wizard/
    ├── install
    ├── upgrade
    ├── uninstall
    └── config
```

## 关键目录

- `target`：已安装的应用文件和运行资源。
- `etc`：应用配置。
- `var`：需要在应用重启后保留的运行数据。
- `tmp`：临时文件。
- `home`：应用用户数据。
- `shares`：在 config/resource 中声明的共享目录。
- `cmd`：生命周期脚本。
- `wizard`：安装、升级、卸载或配置时使用的用户表单。

请使用 `TRIM_APPDEST`、`TRIM_PKGETC`、`TRIM_PKGVAR` 等环境变量，不要硬编码路径。参考 [环境变量](environment-variables.md)。

## 生命周期脚本

飞牛 fnOS 会在安装、启动、更新、配置变更和卸载过程中调用 `cmd/` 下的脚本。

| 脚本 | 作用 |
| --- | --- |
| `install_init` | 安装文件应用前执行。 |
| `install_callback` | 安装文件应用后执行。 |
| `main` | 处理 `start`、`stop` 和 `status`。 |
| `upgrade_init` | 升级前执行。 |
| `upgrade_callback` | 升级后执行。 |
| `uninstall_init` | 卸载前执行。 |
| `uninstall_callback` | 卸载清理后执行。 |
| `config_init` | 配置变更应用前执行。 |
| `config_callback` | 配置变更应用后执行。 |

脚本应尽量具备可重复执行能力。开发和恢复过程中，安装、升级和配置流程都可能被重新执行。

## 安装流程

需要在应用首次启动前完成的检查和初始化，可放在该流程中处理。

## 升级流程

升级脚本适合处理数据迁移、配置迁移和兼容性检查。

如果应用正在运行，飞牛 fnOS 可能会在升级前停止应用，并在升级完成后重新启动。

## 卸载流程

卸载逻辑应尊重用户数据。如果应用允许用户选择保留或删除数据，可在 `wizard/uninstall` 中收集选择，并在卸载脚本中执行。

## 配置流程

当用户配置变更需要更新文件、重启服务或通知应用进程时，可使用该流程。

## 运行控制

`cmd/main` 负责处理应用运行状态。

**cmd/main**

```bash
#!/bin/bash

case "$1" in
  start)
    # Start the application service.
    exit 0
    ;;

  stop)
    # Stop the application service.
    exit 0
    ;;

  status)
    # Return 0 when running, 3 when not running.
    exit 0
    ;;

  *)
    exit 1
    ;;
esac
```

退出码：

- 0：成功，或在 status 中表示正在运行。
- 1：失败。
- 3：在 status 中表示未运行。

静态应用可以在 `manifest` 中设置 `ctl_stop=false`，隐藏运行控制。

## 用户可见错误

生命周期脚本可以在返回失败码前，将清晰的错误信息写入 `TRIM_TEMP_LOGFILE`。

**cmd/main**

```bash
if [ ! -f "$TRIM_PKGETC/config.conf" ]; then
  echo "Missing configuration file." > "$TRIM_TEMP_LOGFILE"
  exit 1
fi
```

这类信息应简短并可执行。它们可能会在安装、启动、升级或配置流程中展示给用户。

---

- 上一页: [📘　开发指南](../category/开发指南.md)
- 下一页: [Manifest](manifest.md)

---

## fnpack

`fnpack` 用于创建飞牛 fnOS 应用项目，并将应用打包为可安装的 `.fpk` 文件。开发者可以在本地开发机使用，也可以在飞牛 fnOS 设备上使用。

## 下载

根据开发机系统下载对应版本：

- Windows x86: fnpack-1.2.3-windows-amd64
- Linux x86: fnpack-1.2.3-linux-amd64
- Linux ARM: fnpack-1.2.3-linux-arm64
- macOS Intel: fnpack-1.2.3-darwin-amd64
- macOS Apple Silicon: fnpack-1.2.3-darwin-arm64

Linux 或 macOS 可安装到系统路径：

```bash
chmod +x fnpack-1.2.3-linux-amd64
sudo mv fnpack-1.2.3-linux-amd64 /usr/local/bin/fnpack
fnpack --help
```

## 创建项目

创建普通应用项目：

```bash
fnpack create <appname>
```

创建不包含桌面入口的服务类项目：

```bash
fnpack create <appname> --without-ui true
```

创建 Docker 应用项目：

```bash
fnpack create <appname> --template docker
```

创建不包含桌面入口的 Docker 服务类项目：

```bash
fnpack create <appname> --template docker --without-ui true
```

Docker 模板会生成 `docker-compose.yaml`、基础资源声明和生命周期脚本框架。打包前需要根据应用实际运行方式检查并调整这些文件。

## 项目结构

```text
myapp/
├── app/
│   ├── ui/
│   │   ├── config
│   │   └── images/
│   └── docker/
│       └── docker-compose.yaml
├── cmd/
│   ├── main
│   ├── install_init
│   ├── install_callback
│   ├── upgrade_init
│   ├── upgrade_callback
│   ├── uninstall_init
│   ├── uninstall_callback
│   ├── config_init
│   └── config_callback
├── config/
│   ├── privilege
│   └── resource
├── wizard/
├── manifest
├── ICON.PNG
└── ICON_256.PNG
```

## 打包项目

在应用目录中执行：

```bash
cd myapp
fnpack build
```

指定其他目录进行打包：

```bash
fnpack build --directory <path>
```

## 打包检查

`fnpack` 会在生成 `.fpk` 前检查必要文件和基础格式。

| 路径 | 类型 | 要求 |
| --- | --- | --- |
| `manifest` | 文件 | 存在，并包含必要字段 |
| `config/privilege` | 文件 | 存在，并使用合法 JSON |
| `config/resource` | 文件 | 存在，并使用合法 JSON |
| `ICON.PNG` | 文件 | 存在 |
| `ICON_256.PNG` | 文件 | 存在 |
| `app/` | 目录 | 存在 |
| `cmd/` | 目录 | 存在 |
| `wizard/` | 目录 | 存在 |
| `app/{desktop_uidir}/` | 目录 | 声明 `desktop_uidir` 时必须存在 |

## 使用建议

- 将打包目录放在应用源码附近，便于版本管理和自动化构建。
- 在发布构建脚本中加入 fnpack build。
- 发布前在飞牛 fnOS 测试设备上安装生成的 .fpk 并完成基础验证。

---

- 上一页: [🛠️　开发工具](../category/️开发工具.md)
- 下一页: [appcenter-cli](appcentercli.md)

---

## 创建应用

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

---

## 测试应用

将 `.fpk` 包安装到飞牛 fnOS 测试设备，并验证桌面入口。

---

## 1. 安装应用包

### 通过应用中心安装

适用于本地验证。

打开应用中心，进入手动安装入口，并选择 `HelloFnos.fpk`。

![应用中心手动安装入口](../../assets/static/appcenter-marketing/20250829100144099.png)

手动安装仅用于本地测试，不应作为公开分发方式。

### 使用 appcenter-cli 安装

适用于脚本化安装或 CI 流程。

在飞牛 fnOS 设备上运行：

```bash
appcenter-cli install-fpk HelloFnos.fpk
```

包含安装向导的应用包可指定环境变量文件：

```bash
appcenter-cli install-fpk HelloFnos.fpk --env config.env
```

## 2. 打开应用

从飞牛 fnOS 桌面打开 **Hello fnOS**。

页面应显示：

```text
Hello fnOS 应用正在运行。
```

如果入口无法打开，检查：

- app/ui/config：入口 URL 应为 /cgi/ThirdParty/HelloFnos/index.cgi/
- app/ui/index.cgi：BASE_PATH 应指向 /var/apps/HelloFnos/target/www
- app/www/index.html：目标页面应存在于应用包中

## 3. 开发中重复测试

修改应用包后：

1. 运行 fnpack build
2. 安装新的 .fpk 文件
3. 再次打开桌面入口

包含后台服务的应用，还需要检查进程状态、端口和运行日志。可继续阅读 [应用架构](../core-concepts/framework.md)、[Native 应用案例](../examples/native.md) 或 [Docker 应用案例](../examples/docker.md)。

## 下一步

继续阅读 [发布应用](publish-application.md)。

---

- 上一页: [创建应用](create-application.md)
- 下一页: [上架应用](publish-application.md)

---

## 上架应用

提交应用到应用中心前，请准备发布材料，并在计划支持的环境中完成测试。

---

## 1. 提交方式

开发者后台上线前，可以通过应用中心开发者先锋交流群提交应用。

加入流程：

1. 加入任意飞牛粉丝群。可从 飞牛官网 进入，右上角关注飞牛，并在 微信群 分类中扫码加入。
2. 在群内联系飞牛社区主理人，加入应用中心开发者先锋交流群。
3. 根据工作人员指引提交应用信息、应用包和测试材料。

开发者后台上线后，请以后续平台流程为准。

## 2. 准备发布材料

大部分应用信息都定义在 `manifest` 中，包括应用名称、描述、版本、维护者、支持的系统版本范围、平台和更新说明。上架前请确保这些字段准确。

准备 `manifest` 之外的发布材料：

- 通过 fnpack 生成的最终 .fpk 包
- 应用图标
- 截图

截图应展示真实应用界面和核心流程，不应使用占位页面或开发阶段的临时设计图。

## 3. 发布前测试

不要只依赖一次成功安装。请在计划支持的飞牛 fnOS 版本和硬件架构上测试应用。

重点关注用户实际会遇到的体验：

- 应用可以按预期安装、打开和运行
- 主要流程可以完成，不会出现非预期错误
- 用户创建或导入的数据可以正确保存、读取、更新和删除
- 用户无法访问未授权的数据或操作
- 本地 API、网络端口和后台任务只暴露应用真正需要的能力

如果应用依赖外部服务、数据库、硬件设备或大模型，也需要测试依赖不可用、配置错误或资源不足时的表现。

## 下一步

回顾打包和测试文档：

- 创建应用
- 测试应用
- Manifest
- fnpack

---

- 上一页: [测试应用](test-application.md)
- 下一页: [📘　开发指南](../category/开发指南.md)

---

## Manifest

`manifest` 文件用于描述应用包。它放在应用包根目录下，没有文件扩展名。

飞牛 fnOS 会使用这个文件识别应用、在应用中心中展示应用、检查兼容性，并准备运行环境。

## 基础信息

- `appname`：应用唯一标识。
- `version`：应用版本，例如 1.0.0 或 2.1.3-beta。
- `display_name`：显示在应用中心、应用设置和用户界面中的名称。
- `desc`：应用描述。必要时可以使用 HTML 内容。
- `source`：应用来源。第三方应用使用 thirdparty。

## 平台支持

- `platform`：应用包支持的硬件架构。
    - x86：支持 x86 设备。
    - arm：支持 ARM 设备。
    - all：同时支持 x86 和 ARM 设备。仅当应用包不包含特定架构二进制时使用。

## 开发者信息

- `maintainer`：开发者或团队名称。
- `maintainer_url`：开发者网站或联系方式。
- `distributor`：发布者名称。如果与开发者不同，可单独填写。
- `distributor_url`：发布者网站或联系方式。

## 兼容范围

- `os_min_version`：支持的最低飞牛 fnOS 版本。
- `os_max_version`：支持的最高飞牛 fnOS 版本。如果应用存在明确的兼容上限，可填写该字段。

请根据实际测试过的版本设置这些字段，不要声明超过应用真实支持能力的范围。

## 运行控制

- `ctl_stop`：控制应用中心是否显示启动和停止操作。
    - true：显示启动、停止和运行状态。
    - false：隐藏这些控制项。

静态页面、配置型应用，或不应由用户手动启动和停止的应用，可使用 `ctl_stop=false`。

## 安装

- **`install_type`**：安装目标。
    - 空值：安装时由用户选择存储位置。
    - root：安装到系统分区。
- **`install_dep_apps`**：依赖应用。
    - 多个依赖使用 : 分隔。
    - 使用 > 声明最低版本，例如 database>2.2.2:cache。

## 桌面集成

- `desktop_uidir`：相对于应用目录的 UI 目录，默认值为 ui。
- `desktop_applaunchname`：当应用存在多个入口时，用于指定从应用中心应用卡片打开的入口 ID。该 ID 应与 {desktop_uidir}/config 中定义的入口一致。

## 端口

- `service_port`：应用服务端口。
- `checkport`：控制飞牛 fnOS 是否在启动应用前检查端口，默认值为 true。

不监听固定端口的应用可以省略 `service_port`，或在适合的情况下设置 `checkport=false`。

## 授权

- `disable_authorization_path`：控制应用设置页是否显示授权目录设置。
    - false：用户可以配置授权目录。
    - true：隐藏授权目录设置。

仅当应用不需要用户选择文件或目录访问权限时，才使用 `true`。

## 更新说明

- `changelog`：应用更新时或应用中心更新相关界面中展示的更新说明。

更新说明应保持简洁，并面向用户表达。

## 示例

**manifest**

```ini
appname=HelloFnos
version=1.0.0
display_name=Hello fnOS
desc=一个最小的飞牛 fnOS 应用。
source=thirdparty
platform=all

maintainer=Example Team
maintainer_url=https://example.com

os_min_version=1.2.0

desktop_uidir=ui
desktop_applaunchname=HelloFnos.Application

ctl_stop=false
checkport=false
```

对于服务类应用，还需要声明服务端口，并根据是否允许用户在应用中心中启动和停止应用来设置 `ctl_stop`。

---

- 上一页: [应用框架](framework.md)
- 下一页: [环境变量](environment-variables.md)

---

## 环境变量

飞牛 fnOS 会向生命周期脚本和应用进程提供环境变量。应用可以用它们定位目录、读取包信息，并获取用户配置。

环境变量主要来自：

- manifest 字段
- 安装、配置和升级向导
- 系统运行上下文
- 应用资源和权限设置

## 应用信息

- `TRIM_APPNAME`：来自 manifest.appname 的应用名称。
- `TRIM_APPVER`：当前应用版本。
- `TRIM_OLD_APPVER`：升级过程中的旧版本。
- `TRIM_APP_STATUS`：当前操作，例如 INSTALL、START、UPGRADE、UNINSTALL、STOP 或 CONFIG。

## 应用路径

- `TRIM_APPDEST`：已安装的 target 目录。
- `TRIM_PKGETC`：应用配置目录。
- `TRIM_PKGVAR`：运行时数据目录。
- `TRIM_PKGTMP`：临时目录。
- `TRIM_PKGHOME`：应用用户数据目录。
- `TRIM_PKGMETA`：元数据目录。
- `TRIM_APPDEST_VOL`：应用安装所在的存储空间路径。

尽量使用这些变量，而不是在脚本中硬编码路径。

## 用户和权限上下文

- `TRIM_USERNAME`：专用应用用户。
- `TRIM_GROUPNAME`：专用应用用户组。
- `TRIM_UID`：应用用户 ID。
- `TRIM_GID`：应用用户组 ID。
- `TRIM_RUN_USERNAME`：当前执行脚本的用户。
- `TRIM_RUN_GROUPNAME`：当前执行脚本的用户组。
- `TRIM_RUN_UID`：当前执行脚本的 UID。
- `TRIM_RUN_GID`：当前执行脚本的 GID。

`TRIM_USERNAME` 表示应用用户。`TRIM_RUN_USERNAME` 表示当前脚本的执行用户，在特权操作中可能不同。

## 网络和资源

- `TRIM_SERVICE_PORT`：manifest.service_port 声明的服务端口。
- `TRIM_DATA_SHARE_PATHS`：config/resource 声明的数据共享路径，多个路径使用 : 分隔。
- `TRIM_DATA_ACCESSIBLE_PATHS`：用户授权的可访问路径，多个路径使用 : 分隔。

共享数据目录也可以通过 `/var/apps/myapp/share/` 下的软链访问。

使用这些路径读写文件前，应用仍应验证文件权限。

## 日志和临时文件

- `TRIM_TEMP_LOGFILE`：生命周期脚本用于输出用户可见错误信息的临时日志文件。
- `TRIM_TEMP_UPGRADE_FOLDER`：升级过程临时目录。
- `TRIM_PKGINST_TEMP_DIR`：安装时的临时解压目录。
- `TRIM_TEMP_TPKFILE`：应用包解压目录。

生命周期脚本失败时，请在以非零状态退出前，将清晰的错误信息写入 `TRIM_TEMP_LOGFILE`。

## 系统上下文

- `TRIM_SYS_VERSION`：完整飞牛 fnOS 版本。
- `TRIM_SYS_VERSION_MAJOR`：系统主版本。
- `TRIM_SYS_VERSION_MINOR`：系统次版本。
- `TRIM_SYS_VERSION_BUILD`：构建号。
- `TRIM_SYS_ARCH`：系统 CPU 架构。
- `TRIM_KERNEL_VERSION`：内核版本。
- `TRIM_SYS_MACHINE_ID`：设备唯一标识。
- `TRIM_SYS_LANGUAGE`：系统语言。

系统变量适合用于诊断和兼容性检查。不要让实际行为与 `manifest` 声明的支持范围冲突。

## 向导变量

向导中收集的值会变成环境变量。这些变量不使用 `TRIM_` 前缀。

例如，名为 `db_port` 的向导字段会变成：

```text
db_port
```

向导变量名称应清晰并保持稳定，因为生命周期脚本和应用服务可能会依赖它们。

## 示例

**cmd/main**

```bash
#!/bin/bash

case "$1" in
  start)
    echo "Starting $TRIM_APPNAME $TRIM_APPVER"
    echo "App directory: $TRIM_APPDEST"
    echo "Config directory: $TRIM_PKGETC"
    echo "Data directory: $TRIM_PKGVAR"

    if [ ! -f "$TRIM_PKGETC/config.conf" ]; then
      cp "$TRIM_APPDEST/config.conf.example" "$TRIM_PKGETC/config.conf"
    fi

    cd "$TRIM_APPDEST"
    ./myapp \
      --config "$TRIM_PKGETC/config.conf" \
      --data "$TRIM_PKGVAR" \
      --port "$TRIM_SERVICE_PORT" \
      --log "$TRIM_TEMP_LOGFILE" &
    ;;

  status)
    if pgrep -f "myapp.*$TRIM_SERVICE_PORT" > /dev/null; then
      exit 0
    fi
    exit 3
    ;;

  stop)
    pkill -f "myapp.*$TRIM_SERVICE_PORT"
    ;;

  *)
    echo "Unknown command: $1" > "$TRIM_TEMP_LOGFILE"
    exit 1
    ;;
esac
```

## 建议

- 自定义向导变量不要使用 TRIM_ 前缀。
- 使用路径变量前，先检查目录是否存在。
- Shell 脚本中引用变量时加引号。
- 将向导值和来自请求的值视为不可信输入。
- 使用 TRIM_TEMP_LOGFILE 输出清晰的用户可见错误信息。

---

- 上一页: [Manifest](manifest.md)
- 下一页: [应用权限](privilege.md)

---

## 应用权限

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

---

## 应用资源

`config/resource` 用于声明应用需要的系统资源和集成能力。这个文件应只包含应用实际使用的能力。

## 共享数据目录

当应用需要提供可由用户在文件管理器中访问的共享目录时，使用 `data-share`。

**config/resource**

```json
{
  "data-share": {
    "shares": [
      {
        "name": "myapp/documents"
      },
      {
        "name": "myapp/backups"
      }
    ]
  }
}
```

- `name`：共享路径名称。
- `permission`：可选字段，用于给其他用户或应用配置访问权限。大多数共享目录不需要配置。

安装应用时，飞牛 fnOS 会自动创建声明的共享目录。这些目录使用 Windows ACL 权限模型，而不是 POSIX ACL。系统会自动为应用运行用户授予所需的 ACL 访问权限。

应用可以通过 `TRIM_DATA_SHARE_PATHS` 环境变量获取已创建的共享目录路径，也可以通过 `/var/apps/myapp/share/` 下的软链访问对应目录，例如 `/var/apps/myapp/share/documents`。

适合将用户需要查看、导入、导出或在应用外管理的内容放入共享目录。建议使用应用名称作为统一的顶级目录，例如 `myapp`，再按用途定义子目录，例如 `myapp/documents`、`myapp/backups`。这样用户看到的共享内容更集中，也能减少和其他应用的命名冲突。

只有在其他应用或系统用户需要访问该共享目录时，才需要配置 `permission`：

**config/resource**

```json
{
  "data-share": {
    "shares": [
      {
        "name": "myapp/documents",
        "permission": {
          "rw": ["other_app_user"],
          "ro": ["report_reader"]
        }
      }
    ]
  }
}
```

- `rw`：拥有读写权限的用户。
- `ro`：拥有只读权限的用户。

## 系统链接

当应用需要将命令、库或配置文件暴露到标准系统位置时，使用 `usr-local-linker`。

**config/resource**

```json
{
  "usr-local-linker": {
    "bin": [
      "bin/myapp-cli"
    ],
    "lib": [
      "lib/mylib.so"
    ],
    "etc": [
      "etc/myapp.conf"
    ]
  }
}
```

- `bin`：链接到 /usr/local/bin/。
- `lib`：链接到 /usr/local/lib/。
- `etc`：链接到 /usr/local/etc/。

只应暴露其他命令或应用确实需要使用的稳定接口。对于可执行文件，应避免使用 `cli`、`server`、`tool` 等通用名称。建议使用带有应用标识的命令名，例如 `myapp-cli`，以减少和系统命令或其他应用的注册冲突。

## Docker 项目

当应用通过 Docker Compose 运行时，使用 `docker-project`。

项目结构：

```text
myapp/
├── app/
│   └── docker/
│       └── docker-compose.yaml
├── manifest
├── cmd/
└── config/
    └── resource
```

资源声明：

**config/resource**

```json
{
  "docker-project": {
    "projects": [
      {
        "name": "myapp-stack",
        "path": "docker"
      }
    ]
  }
}
```

- `name`：Docker Compose 项目名称。
- `path`：相对于 app 目录的路径，该目录应包含 docker-compose.yaml。

Docker 项目适合多服务应用、依赖数据库或缓存的应用，以及需要受控运行环境的应用。

## 建议

- 只声明应用实际需要的资源。
- 资源名称应在版本之间保持稳定。
- 不要将内部工具或内部数据目录作为共享资源暴露。
- 用户可见的共享目录应在应用界面或更新说明中说明。

---

- 上一页: [应用权限](privilege.md)
- 下一页: [应用入口](app-entry.md)

---

## 应用入口

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

---

## index.cgi

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

---

## 统一网关

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

---

## 用户向导

向导用于在安装、升级、卸载或配置时收集用户输入。向导收集到的值会作为环境变量提供给生命周期脚本。

只有当应用确实需要用户提供无法安全自动检测或默认处理的信息时，才使用向导。表单应聚焦于安装、运行或配置应用所必需的值。

## 向导文件

飞牛 fnOS 支持四种向导文件：

- `wizard/install`：安装时显示。
- `wizard/upgrade`：升级时显示。
- `wizard/uninstall`：卸载时显示。
- `wizard/config`：安装后从应用设置中显示。用户可以继续修改应用配置，提交后的值会继续作为环境变量提供给应用使用。

## 基本结构

每个向导文件都是一个由步骤组成的 JSON 数组。

- `stepTitle`：步骤标题。
- `items`：该步骤中显示的表单项。
- `field`：字段名。收集到的值会成为同名环境变量。

**wizard/install**

```json
[
  {
    "stepTitle": "Setup",
    "items": [
      {
        "type": "text",
        "field": "wizard_username",
        "label": "Username",
        "initValue": "admin",
        "rules": [
          {
            "required": true,
            "message": "Enter a username"
          }
        ]
      }
    ]
  }
]
```

字段 `wizard_username` 会变成名为 `wizard_username` 的环境变量。

## 字段类型

| 类型 | 用途 |
| --- | --- |
| `text` | 短文本、端口、路径、用户名等普通值 |
| `password` | 不应明文显示的密钥或令牌 |
| `radio` | 少量互斥选项 |
| `checkbox` | 多选项 |
| `select` | 较长的互斥选项列表 |
| `switch` | 布尔风格选项 |
| `tips` | 只读提示文本 |

带选项字段示例：

```json
{
  "type": "select",
  "field": "wizard_database_type",
  "label": "Database",
  "initValue": "sqlite",
  "options": [
    {
      "label": "SQLite",
      "value": "sqlite"
    },
    {
      "label": "PostgreSQL",
      "value": "postgresql"
    }
  ]
}
```

提示文本示例：

```json
{
  "type": "tips",
  "helpText": "Review the configuration before continuing."
}
```

## 校验规则

通过 `rules` 数组添加校验规则。

```json
{
  "type": "text",
  "field": "wizard_port",
  "label": "Service port",
  "rules": [
    {
      "required": true,
      "message": "Enter a port"
    },
    {
      "pattern": "^[0-9]+$",
      "message": "Use numbers only"
    }
  ]
}
```

常见规则：

- `required`：必填。
- `min` 和 `max`：长度或数值范围。
- `len`：固定长度。
- `pattern`：正则表达式。

## 使用向导值

向导值会作为环境变量提供给生命周期脚本。可以用于生成配置文件、选择安装模式、设置端口或路径，以及控制可选功能。

**cmd/install_callback**

```bash
#!/bin/bash

echo "Database type: $wizard_database_type"
echo "Service port: $wizard_port"
```

脚本中应将向导值按字符串处理，并在使用前再次校验。

## 字段命名

- 使用稳定的字段名。修改字段名会改变环境变量名。
- 自定义字段建议使用 wizard_ 前缀，例如 wizard_port。
- 自定义向导字段不要使用 TRIM_ 前缀。该前缀保留给系统变量。
- 尽量兼容已发布版本使用过的字段名。

## 设计建议

- 只询问应用安装、运行或配置所需的值。
- 尽可能提供合理默认值。
- 使用简短标签和清晰的校验信息。
- 密钥类输入使用 password。
- 不要将密钥写入日志。
- 在生命周期脚本中使用前，再次校验输入值。

---

- 上一页: [统一网关](gateway-registration.md)
- 下一页: [应用依赖](dependency.md)

---

## 应用依赖

当应用依赖其他应用时，在 `manifest` 中使用 `install_dep_apps`。

**manifest**

```ini
install_dep_apps=database:cache
```

## 依赖顺序

声明多个依赖时，飞牛 fnOS 会从右到左安装和启用依赖。

例如，`cache` 需要先于 `database` 准备完成时，可以这样声明：

**manifest**

```ini
install_dep_apps=database:cache
```

依赖顺序应明确声明。嵌套依赖不会为当前应用递归解析。

## 版本要求

使用 `>` 声明依赖所需的最低版本：

**manifest**

```ini
install_dep_apps=database>2.2.2:cache
```

只有应用依赖某个版本引入的特定行为时，才声明版本要求。

## 嵌套依赖

依赖检查不递归。如果应用同时需要 `database` 和 `cache`，即使其中一个也依赖另一个，也应在当前应用中直接声明二者。

**manifest**

```ini
install_dep_apps=database:cache
```

## 建议

- 只声明应用直接需要的依赖。
- 在版本迭代中保持依赖名称稳定。
- 在干净设备上测试安装，确认依赖链可用。
- 依赖缺失或不可用时，显示清晰的用户可见错误信息。

---

- 上一页: [用户向导](wizard.md)
- 下一页: [中间件服务](middleware.md)

---

## 中间件服务

应用可以使用 Redis、MinIO 或 RabbitMQ 等中间件服务。请在 `manifest` 中通过 `install_dep_apps` 声明所需服务。

## Redis

**manifest**

```ini
install_dep_apps=redis
```

Python 示例：

```python
import redis

pool = redis.ConnectionPool(
    host="127.0.0.1",
    port=6379,
    db=1,
    decode_responses=True,
    max_connections=10,
)

client = redis.Redis(connection_pool=pool)
client.lpush("my_list", "item1", "item2")
items = client.lrange("my_list", 0, -1)
print(items)
```

建议使用独立数据库编号或 key 前缀，避免与其他应用冲突。

## MinIO

**manifest**

```ini
install_dep_apps=minio
```

Python 示例：

```python
from minio import Minio

client = Minio(
    endpoint="127.0.0.1:9000",
    access_key="your_access_key",
    secret_key="your_secret_key",
    secure=False,
)

bucket_name = "my-bucket"

if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
```

请安全保存访问密钥，不要在应用包中硬编码生产凭据。

## RabbitMQ

**manifest**

```ini
install_dep_apps=rabbitmq
```

Python 示例：

```python
import pika

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="127.0.0.1",
        port=5672,
        virtual_host="/",
        credentials=credentials,
    )
)

channel = connection.channel()
channel.queue_declare(queue="my_queue", durable=True)
channel.basic_publish(exchange="", routing_key="my_queue", body=b"hello")
connection.close()
```

请使用应用专属的队列、交换机和路由键。

## 建议

- 只声明应用实际需要的中间件服务。
- 在干净的飞牛 fnOS 设备上测试安装。
- 服务不可用时，显示清晰的用户可见错误信息。
- 不要将凭据提交到源码仓库或打包模板中。
- 为数据库、桶、队列和 key 使用命名空间。

---

- 上一页: [应用依赖](dependency.md)
- 下一页: [运行时环境](runtime.md)

---

## 运行时环境

应用可以使用 Python、Node.js 或 Java 等打包运行时环境。请在 `manifest` 中通过 `install_dep_apps` 声明所需的运行时包。

## Python

**manifest**

```ini
install_dep_apps=python312
```

运行 Python 命令前，先将运行时路径加入 `PATH`：

```bash
export PATH=/var/apps/python312/target/bin:$PATH

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Node.js

**manifest**

```ini
install_dep_apps=nodejs_v22
```

```bash
export PATH=/var/apps/nodejs_v22/target/bin:$PATH

node -v
npm -v
```

## Java

**manifest**

```ini
install_dep_apps=java-21-openjdk
```

```bash
export PATH=/var/apps/java-21-openjdk/target/bin:$PATH

java --version
```

## 建议

- 声明应用实际使用的运行时包。
- 在生命周期脚本中调用运行时命令前，将运行时 bin 目录加入 PATH。
- 将应用自身依赖保存在应用目录或专用虚拟环境中。
- 在干净的飞牛 fnOS 设备上测试应用包，确认运行时依赖可以正确安装。

---

- 上一页: [中间件服务](middleware.md)
- 下一页: [图标](icon.md)

---

## 图标

应用包需要提供包图标，应用入口也可以单独配置入口图标。包图标用于应用中心、安装包识别等场景；入口图标用于桌面图标、文件打开方式等用户入口。

## 包图标

应用包根目录需要包含两个图标文件：

- ICON.PNG：64 x 64 px
- ICON_256.PNG：256 x 256 px

示例结构：

```text
myapp/
├── ICON.PNG
├── ICON_256.PNG
├── app/
├── config/
├── cmd/
└── manifest
```

## 设计要求

- 格式：PNG 或 JPG
- 色彩空间：sRGB
- 文件大小：不超过 1024 KB
- 画布：完整正方形图片
- 圆角：图标视觉主体应使用圆角矩形风格。不要使用直角满铺的方形主体；圆角、留白和阴影应尽量与系统图标保持一致。

两个尺寸应使用一致的视觉识别。图标在 64 x 64 px 下仍需要清晰可辨，重要内容不要贴近画布边缘，也不要依赖过细的文字或装饰细节。

可以参考系统图标的圆角、留白和层次关系：

![系统设置图标示例](../../assets/site/assets/images/icon-example-system-settings-2787823b1bb660e9518d03faed4b4a47.png)

## 应用入口图标

应用入口可以引用 UI 目录下的图标，用于注册桌面图标或注册文件打开方式。推荐将入口图标放在 `app/ui/images/` 下：

```text
myapp/
└── app/
    └── ui/
        ├── config
        └── images/
            ├── icon_64.png
            └── icon_256.png
```

在 `app/ui/config` 中通过 `icon` 字段引用：

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

飞牛 fnOS 会将 `{0}` 替换为所需的图标尺寸，例如 `icon_64.png` 或 `icon_256.png`。

入口配置的更多规则可参考 [应用入口](app-entry.md)。

## 检查清单

打包前建议确认：

- 根目录包含 ICON.PNG 和 ICON_256.PNG。
- 图标文件大小不超过 1024 KB。
- 64 px 图标仍能看清主体。
- 图标主体是圆角矩形风格，而不是直角方块铺满画布。
- 如果入口配置了 images/icon_{0}.png，对应的 icon_64.png 和 icon_256.png 都已放入 UI 目录。

---

- 上一页: [运行时环境](runtime.md)
- 下一页: [🧩　应用案例](../category/应用案例.md)

---

## Native 应用案例

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

- 上一页: [🧩　应用案例](../category/应用案例.md)
- 下一页: [Docker 应用案例](docker.md)

---

## Docker 应用案例

当应用已经容器化，或更适合以一个或多个容器交付并由 Docker Compose 管理时，可以使用 Docker 应用模板。

这一页从零创建一个 `hello-docker` 示例应用，并将它打包成可以安装运行的 `.fpk` 文件。示例应用使用 `nginx:alpine` 启动一个 Web 页面，用户可以从飞牛 fnOS 桌面入口打开它。

本案例使用：

- 应用包名：hello-docker
- Docker 镜像：nginx:alpine
- 服务端口：8080
- 访问方式：端口入口

如果应用只是一个简单的 Node.js、Python、Go 或二进制服务，也可以参考 [Native 应用案例](native.md)。

## 创建 Docker 应用项目

创建应用包目录：

```bash
fnpack create hello-docker --template docker
cd hello-docker
```

生成后的目录大致如下：

```text
hello-docker/
├── app/
│   ├── docker/
│   │   └── docker-compose.yaml
│   └── ui/
│       ├── config
│       └── images/
├── cmd/
│   └── main
├── config/
│   ├── privilege
│   └── resource
├── wizard/
├── manifest
├── ICON.PNG
└── ICON_256.PNG
```

其中：

- app/docker/docker-compose.yaml 存放 Docker Compose 编排文件。
- config/resource 声明 Docker 项目资源。
- cmd/main 负责返回应用运行状态。
- app/ui/config 用于注册桌面图标或其他入口。

## 编辑 manifest

将 `manifest` 改为：

**hello-docker/manifest**

```ini
appname=hello-docker
version=1.0.0
display_name=Hello Docker
desc=A minimal Docker application.
source=thirdparty
platform=all
maintainer=Example Team
distributor=Example Team
desktop_uidir=ui
desktop_applaunchname=hello-docker.main
service_port=8080
checkport=true
ctl_stop=true
```

说明：

- platform=all 适用于不包含平台相关二进制的应用包。镜像本身仍需要支持目标设备架构。
- service_port=8080 表示应用在宿主机上使用的访问端口。
- desktop_applaunchname=hello-docker.main 指向应用卡片打开的入口 ID。
- ctl_stop=true 表示应用中心显示启动、停止和运行状态。

更多字段可参考 [Manifest](../core-concepts/manifest.md)。

## 准备页面文件

创建一个要由 nginx 提供的页面：

```bash
mkdir -p app/docker/html
```

写入页面文件：

**hello-docker/app/docker/html/index.html**

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hello Docker</title>
    <style>
      body {
        margin: 0;
        font-family: sans-serif;
        display: grid;
        min-height: 100vh;
        place-items: center;
        background: #f5f7fb;
        color: #1f2937;
      }
      main {
        text-align: center;
      }
    </style>
  </head>
  <body>
    <main>
      <h1>Hello Docker</h1>
      <p>This page is served by nginx inside a Docker container.</p>
    </main>
  </body>
</html>
```

## 编写 Docker Compose

将 `app/docker/docker-compose.yaml` 改为：

**hello-docker/app/docker/docker-compose.yaml**

```yaml
services:
  web:
    image: nginx:alpine
    container_name: hello-docker-web
    restart: unless-stopped
    ports:
      - "${TRIM_SERVICE_PORT}:80"
    volumes:
      - "${TRIM_APPDEST}/docker/html:/usr/share/nginx/html:ro"
```

这个 Compose 文件会：

- 使用 nginx:alpine 启动 Web 服务。
- 将容器端口 80 映射到 manifest.service_port 声明的端口。
- 将应用包中的 app/docker/html 目录挂载到 nginx 的网页目录。

Compose 文件可以使用飞牛 fnOS 提供的环境变量。常用变量包括：

- TRIM_SERVICE_PORT：manifest.service_port 声明的服务端口。
- TRIM_APPDEST：应用安装后的目标目录。
- TRIM_PKGVAR：应用运行时数据目录。
- TRIM_DATA_SHARE_PATHS：config/resource 声明的数据共享路径。

更多变量可参考 [环境变量](../core-concepts/environment-variables.md)。

> [!NOTE]
> 如果应用要同时支持 x86 和 ARM 设备，请确认使用的镜像支持对应架构。应用包可以声明 `platform=all`，但镜像不支持目标架构时，容器仍然无法启动。

## 声明 Docker 项目资源

将 `config/resource` 改为：

**hello-docker/config/resource**

```json
{
  "docker-project": {
    "projects": [
      {
        "name": "hello-docker",
        "path": "docker"
      }
    ]
  }
}
```

字段说明：

- docker-project.projects[].name：Docker Compose 项目名称，应保持稳定。
- docker-project.projects[].path：相对于 app/ 目录的路径。这里指向 app/docker/。

如果应用需要让用户在文件管理器中访问数据，再额外声明 `data-share`。更多资源声明可参考 [应用资源](../core-concepts/resource.md)。

## 权限配置

Docker 应用通常由容器承载主要进程，`config/privilege` 不用于指定容器内进程身份。这里保留默认的 package 配置，主要用于保持包结构完整，也便于后续应用形态调整或补充本地脚本。

将 `config/privilege` 改为：

**hello-docker/config/privilege**

```json
{
  "defaults": {
    "run-as": "package"
  },
  "username": "hello-docker",
  "groupname": "hello-docker"
}
```

如果应用额外包含本地脚本或原生进程，再根据实际需要调整权限配置。更多说明可参考 [应用权限](../core-concepts/privilege.md)。

## 运行状态检查

Docker 应用的启动和停止由飞牛 fnOS 根据 Docker 项目资源处理。`cmd/main` 中的 `start` 和 `stop` 通常不需要额外操作，但 `status` 仍需要准确判断应用是否正在运行。

将 `cmd/main` 改为：

**hello-docker/cmd/main**

```bash
#!/bin/bash

CONTAINER_NAME="hello-docker-web"

is_running() {
  docker inspect "$CONTAINER_NAME" 2>/dev/null | grep -q '"Status": "running"'
}

case "$1" in
  start)
    exit 0
    ;;
  stop)
    exit 0
    ;;
  status)
    if is_running; then
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

选择状态检查容器时，建议使用最能代表应用可用性的容器。这个示例只有一个容器，所以直接检查 `hello-docker-web`。

## 配置桌面入口

将 `app/ui/config` 改为：

**hello-docker/app/ui/config**

```json
{
  ".url": {
    "hello-docker.main": {
      "title": "Hello Docker",
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

注意：

- 入口 ID 使用 hello-docker 作为前缀，并与 manifest 中的 desktop_applaunchname 保持一致。
- port 应与 manifest.service_port 和 Compose 端口映射保持一致。
- 入口配置的更多规则可参考 应用入口。

## 打包和验证

在应用包目录执行：

```bash
fnpack build
```

成功后会生成：

```text
hello-docker.fpk
```

将 `hello-docker.fpk` 安装到飞牛 fnOS 测试设备后，检查以下内容：

- 应用是否能正常安装。
- Docker 镜像是否能拉取。
- 容器是否按预期启动和停止。
- cmd/main status 是否能正确返回运行状态。
- 应用卡片是否能打开 Hello Docker 页面。
- 目标设备架构是否被镜像支持。

**可选：改用统一网关**

Docker 应用也可以使用统一网关，而不是直接暴露宿主机端口。做法是将应用安装目录 `${TRIM_APPDEST}` 挂载到容器内，让容器中的服务在该目录下创建 Unix Socket。

入口配置中使用 `gatewayPrefix` 和 `gatewaySocket`：

**hello-docker/app/ui/config**

```json
{
  ".url": {
    "hello-docker.main": {
      "title": "Hello Docker",
      "icon": "images/icon_{0}.png",
      "type": "iframe",
      "protocol": "",
      "gatewayPrefix": "/app/hello-docker",
      "gatewaySocket": "app.sock",
      "url": "/app/hello-docker",
      "allUsers": true
    }
  }
}
```

Compose 中将 `${TRIM_APPDEST}` 挂载到容器内，并把 Socket 路径传给服务：

**hello-docker/app/docker/docker-compose.yaml**

```yaml
services:
  web:
    image: my-app:latest
    container_name: hello-docker-web
    restart: unless-stopped
    volumes:
      - "${TRIM_APPDEST}:/app/target:rw"
    environment:
      GATEWAY_SOCKET: /app/target/app.sock
```

容器内的 Web 服务需要监听 `/app/target/app.sock`。宿主机上对应的 Socket 路径为：

```text
/var/apps/hello-docker/target/app.sock
```

统一网关会把 `/app/hello-docker` 下的请求转发到这个 Socket。`protocol` 和 `port` 不参与统一网关路由。

如果应用只通过统一网关提供访问入口，可以不依赖 `manifest.service_port` 和端口入口；如果应用同时提供独立端口访问和统一网关访问，则需要分别维护端口映射和网关 Socket。

更多规则可参考 [统一网关](../core-concepts/gateway-registration.md)。

**排查要点**

- 入口打不开：检查 manifest.service_port、docker-compose.yaml 中映射到宿主机的端口，以及 app/ui/config 中入口的 port 是否一致。
- 状态一直显示未运行：确认 cmd/main 中的 CONTAINER_NAME 与 Compose 文件中的 container_name 一致。没有写 container_name 时，Docker Compose 会生成项目相关的容器名称，脚本中需要按实际名称检查。
- 镜像无法启动：确认目标设备可以拉取镜像，并确认镜像支持设备架构。nginx:alpine 是多架构镜像，适合作为入门示例；实际应用镜像也需要做同样检查。

---

- 上一页: [Native 应用案例](native.md)
- 下一页: [🛠️　开发工具](../category/️开发工具.md)

---

## appcenter-cli

`appcenter-cli` 是飞牛 fnOS 设备上的应用中心命令行工具，适合本地调试、重复安装测试和自动化流程。普通手动测试建议优先通过应用中心界面完成。

## 安装 FPK 包

```bash
appcenter-cli install-fpk myapp.fpk
```

如果应用包含安装向导，可以通过环境变量文件传入配置：

```bash
appcenter-cli install-fpk myapp.fpk --env config.env
```

环境变量文件示例：

**config.env**

```ini
wizard_admin_username=admin
wizard_database_type=sqlite
wizard_app_port=8080
wizard_agree_terms=true
```

包含账号、密码、Token 等敏感信息的环境变量文件，不应提交到代码仓库。

## 从本地目录安装

开发过程中，如果应用项目已经位于飞牛 fnOS 测试设备上，可以直接从项目目录安装：

```bash
cd /path/to/myapp
appcenter-cli install-local
```

该命令会完成本地打包和安装，适合快速验证当前开发版本。

## 默认安装位置

查看当前默认安装位置：

```bash
appcenter-cli default-volume
```

设置默认安装位置：

```bash
appcenter-cli default-volume 1
```

## 应用管理

查看已安装应用：

```bash
appcenter-cli list
```

启动应用：

```bash
appcenter-cli start myapp
```

停止应用：

```bash
appcenter-cli stop myapp
```

## 使用建议

- 手动安装和交互式测试优先使用应用中心界面。
- 需要重复安装、脚本化测试或 CI 流程时，再使用 appcenter-cli。
- 测试包含向导的应用时，提前准备环境变量文件。
- 发布前建议在干净的飞牛 fnOS 测试设备上安装 .fpk 并完成验证。

---

- 上一页: [fnpack](fnpack.md)
- 下一页: [📝　更新日志](../category/更新日志.md)

---

## 2026-07-05

本次更新优化了文档结构和应用案例，方便开发者更快理解应用开发流程。

## 主要变化

- fnpack 更新至 V1.2.3。
- 新增 llms.txt 和 llms-full.txt，方便 AI 工具读取文档索引和完整内容。
- 优化部分描述，提升文档整体一致性。

---

- 上一页: [📝　更新日志](../category/更新日志.md)
- 下一页: [2026-05-09](20260509.md)

---

## 2026-05-09

本次更新补充统一网关相关文档，用于说明应用如何复用飞牛 fnOS 访问域名提供服务。

## 主要变化

- 新增统一网关文档，介绍通过 gatewayPrefix 和 gatewaySocket 注册应用访问路径。
- 补充统一网关的登录态校验说明，以及网关转发给应用的用户信息 Header。
- 补充 WebSocket 接入方式，说明长连接请求如何通过统一网关转发到应用服务。

## 适用场景

统一网关适合需要复用系统访问域名、接入 NAS 登录态、提供 API 或支持 WebSocket 的应用。简单静态页面或兼容已有包时，也可以继续使用 `index.cgi`。

---

- 上一页: [2026-07-05](20260705.md)
- 下一页: [2025-12-31](20251231.md)

---

## 2025-12-31

本次更新调整了文档组织方式，并补充多架构、环境变量和打包工具相关说明。

## 主要变化

- 增加文档更新日志分类，便于查看不同阶段的文档变化。
- 调整部分文档结构，使阅读顺序更接近应用开发流程。
- 增加 New、Update 等文档标记，用于提示新增或更新内容。

## 开发概念

- 环境变量文档新增授权目录列表相关说明。
- 应用入口配置支持使用环境变量。
- 应用入口 protocol 字段支持为空，由系统根据当前访问方式自适应处理。
- manifest 中废弃原 arch 字段，改用 platform 表示应用支持的架构范围。

## 工具更新

- fnpack 更新至 V1.2.0。
- 补充打包前校验规则。
- 新增 Linux ARM 版本下载。

---

- 上一页: [2026-05-09](20260509.md)
- 下一页: [2025-12-16](20251216.md)

---

## 2025-12-16

本次更新主要优化文档结构、搜索能力和入门示例。

## 主要变化

- 修复暗色主题下首页和 Footer 的显示问题。
- 优化首页一级分类命名，让新开发者可以按顺序阅读，熟悉流程的开发者也能快速定位内容。
- 在页面右上角加入全局搜索，支持文档内容检索。
- 调整 创建应用 文档位置，并更新为更容易理解的入门案例。

## 内容更新

- manifest 新增应用更新相关说明，并增加 change_log 字段。
- fnpack 更新至 V1.0.4，补充命令说明和注释。
- Docker 应用文档补充注释并优化说明。
- 入门示例调整为 HTML、JavaScript、CSS 静态页面，降低初次阅读门槛。

---

- 上一页: [2025-12-31](20251231.md)
