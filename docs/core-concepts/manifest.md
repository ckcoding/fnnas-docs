# 📚 【基础】Manifest

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/manifest/](https://developer.fnnas.com/docs/core-concepts/manifest/)

> [!NOTE]
> 本文档于 **2025-12-31** 重新调整了内容结构，并新增了部分内容。

manifest 文件就像是应用的"身份证"，它告诉飞牛 fnOS 系统您的应用是谁、需要什么、怎么运行。这个文件必须放在应用包的根目录下，文件名就叫 `manifest`（没有扩展名）。

## 基本信息

这些是每个应用都必须提供的基本信息：

### 应用标识

- `appname` - 应用的唯一标识符，就像人的身份证号一样，在整个系统中必须是唯一的
- `version` - 应用版本号，格式为 x[.y[.z]][-build]，例如：1.0.0、2.1.3-beta
- `display_name` - 在应用中心和应用设置中显示的名称，用户看到的就是这个名字
- `desc` - 应用的详细介绍，支持 HTML 格式，可以包含链接、图片等

### 系统要求 Update!

- **`arch`** - 架构类型，目前固定为 `x86_64`废弃
- `platform` - 架构类型，缺省时默认值： x86，（⚠️注意：不支持多个值填写）New!V1.1.8+
    - 声明为 x86 时，应用仅支持 x86 架构
    - 声明为 arm 时，应用仅支持 arm 架构
    - 声明为 loongarch 时，应用仅支持 loongarch 架构（当前暂未支持）
    - 声明为 risc-v 时，应用仅支持 risc-v 架构（当前暂未支持）
    - 声明为 all 时，表示应用支持所有架构，不区分平台，所有平台都可以下载安装。例如Docker应用。（即将支持）
- `source` - 应用来源，固定为 thirdparty

## 开发者信息

这些信息帮助用户了解应用的开发者和发布者：

- `maintainer` - 应用开发者或开发团队名称
- `maintainer_url` - 开发者网站或联系方式
- `distributor` - 应用发布者（可能与开发者不同）
- `distributor_url` - 发布者网站

## 安装和运行控制

### 系统兼容性

- `os_min_version` - 支持的最低系统版本，例如：0.9.0
- `os_max_version` - 支持的最高系统版本，例如：0.9.100

### 应用控制

- `ctl_stop` - 是否显示启动/停止功能，默认为 true
    - 设置为 false 时，应用中心将隐藏启动、停止按钮和运行状态
    - 适用于那些需要无进程应用或不应该被用户手动控制的应用

### 安装位置

- `install_type` - 安装类型，默认为空
    - 设置为 root 时，应用会安装到系统分区 /usr/local/apps/@appcenter/
    - 为空时，用户可以在安装向导中选择存储位置 /vol${x}/@appcenter/

### 依赖管理

- `install_dep_apps` - 依赖应用列表
    - 格式：app1>2.2.2:app2:app3
    - 系统会按照列表顺序自动安装依赖应用
    - 版本号前的 > 表示最低版本要求

## 用户界面

### 桌面集成

- `desktop_uidir` - UI 组件目录路径
    - 相对于应用根目录的路径，默认为 ui
    - 这个目录存放应用的 Web 界面文件
- `desktop_applaunchname` - 应用中心启动入口
    - 用户点击应用卡片上的"打开"按钮时，系统会启动这个 entry ID，对应 {desktop_uidir}/config 文件中定义的某个入口

## 端口管理

### 端口检查

- `service_port` - 应用监听的端口号
    - 系统会在启动应用前检查这个端口是否被占用
    - 目前只支持单个端口设置
- `checkport` - 是否启用端口检查，默认为 true
    - 设置为 false 时，系统不会检查端口占用情况
    - 适用于不需要固定端口的应用

## 权限控制

- `disable_authorization_path` - 是否禁用授权目录功能，默认为 false
    - 设置为 true 时，应用设置页面不会显示授权目录操作
    - 适用于不需要访问特定系统目录的应用

## 应用更新

- `changelog` - 应用更新日志
    - 用于应用升级时展示更新日志内容
    - 应用中心可用更新页面展示的更新日志内容，在应用详情页更新时将展示为"新功能"介绍

## 示例

下面是一个典型的 manifest 文件示例：

```text
appname=myapp
version=1.0.0
display_name=我的应用
desc=这是一个示例应用，展示了 manifest 文件的基本用法
arch=x86_64
source=thirdparty

maintainer=张三
maintainer_url=https://example.com
distributor=示例公司
distributor_url=https://company.com

os_min_version=0.9.0

desktop_uidir=ui
desktop_applaunchname=myapp.APPLICATION

service_port=8080
checkport=true

install_dep_apps=mariaDB:redis
```

这个文件定义了应用的基本信息、开发者信息、系统要求、UI 配置、端口设置和依赖关系。系统会根据这些信息来正确安装、配置和运行您的应用。

---

- 上一页: [📚 【基础】架构概述](framework.md)
- 下一页: [📚 【基础】环境变量](environment-variables.md)
