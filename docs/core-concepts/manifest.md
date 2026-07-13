# Manifest

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/manifest/](https://developer.fnnas.com/docs/core-concepts/manifest/)

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
