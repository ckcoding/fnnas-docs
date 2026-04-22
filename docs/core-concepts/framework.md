# 📚 【基础】架构概述

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/framework/](https://developer.fnnas.com/docs/core-concepts/framework/)

> [!NOTE]
> 本文档于 **2025-12-31** 重新调整了内容结构，并新增了部分内容。

## 应用目录结构

当您的应用安装到飞牛 fnOS 系统后，会在系统中创建如下的目录结构：

```text
/var/apps/[appname]
├── cmd
│   ├── install_callback
│   ├── install_init
│   ├── main
│   ├── uninstall_callback
│   ├── uninstall_init
│   ├── upgrade_init
│   ├── upgrade_callback
│   ├── config_init
│   └── config_callback
├── config
│   ├──privilege
│   └──resource
├── ICON_256.PNG
├── ICON.PNG
├── LICENSE
├── manifest
├── etc->/vol[volume_number]/@appconf/[appname]
├── home->/vol[volume_number]/@apphome/[appname]
├── target->/vol[volume_number]/@appcenter/[appname]
├── tmp->/vol[volume_number]/@apptemp/[appname]
├── var->/vol[volume_number]/@appdata/[appname]
├── shares
│   ├──datashare1->/vol[volume_number]/@appshare/datashare1
│   └──datashare2->/vol[volume_number]/@appshare/datashare2
└── wizard
    ├── install
    ├── uninstall
    ├── upgrade
    └── config
```

### 核心文件说明

**应用标识文件：**

- manifest - 应用的"身份证"，定义了应用的基本信息和运行属性
- config/privilege - 应用的"权限清单"，声明应用需要哪些系统权限
- config/resource - 应用的"能力声明"，定义应用可以使用的扩展功能

**界面资源：**

- ICON.PNG - 应用中心显示的小图标（64x64 像素）
- ICON_256.PNG - 应用详情页显示的大图标（256x256 像素）
- LICENSE - 用户安装前需要同意的隐私协议（可选）

### 目录功能说明

**开发者定义目录：**

- cmd - 存放应用生命周期管理的脚本文件
- wizard - 存放用户交互向导的配置文件

**系统自动创建目录：**

- target - 应用可执行文件的存放位置
- etc - 静态配置文件存放位置
- var - 运行时动态数据存放位置
- tmp - 临时文件存放位置
- home - 用户数据文件存放位置
- meta - 应用元数据存放位置
- shares - 数据共享目录（根据 resource 配置自动创建）

## 应用生命周期管理

飞牛 fnOS 系统通过调用 `cmd` 目录中的脚本来管理您的应用。这些脚本就像是应用的"管家"，负责处理应用的安装、启动、停止、更新等各个阶段。

### 应用安装流程

安装过程分为三个阶段：安装前准备、文件解压、安装后处理。您可以在 `install_init` 和 `install_callback` 这两个节点添加自定义逻辑，比如环境检查、依赖安装等。如果配置了 `wizard/install` 向导，还可以获取用户的配置输入。

### 应用卸载流程

卸载应用时，系统会删除以下目录：`target`、`tmp`、`home`、`etc`，但会保留 `var` 和 `shares` 目录（保护用户数据）。

如果您希望提供完全删除选项，可以在 `wizard/uninstall` 向导中让用户选择是否保留数据。当用户选择不保留时，您可以在 `cmd/uninstall_callback` 中清理剩余的数据和目录。

如果卸载时应用仍在运行，系统会先停止应用，然后再执行卸载流程：

### 应用更新流程

更新流程与安装流程类似，同样提供了 `upgrade_init` 和 `upgrade_callback` 两个节点。您可以在这里处理数据库升级、配置迁移等逻辑。如果配置了 `wizard/upgrade` 向导，还可以获取用户的更新配置。

如果更新时应用正在运行，系统会先停止应用，执行更新，然后重新启动应用：

### 应用配置流程

用户可以在 **系统设置** - **应用设置** 中查看和修改您的应用配置。可配置的范围由 `wizard/config` 文件定义。

当用户修改配置并保存后，系统会更新环境变量。您可以在 `config_init` 和 `config_callback` 中监听这些变化，并相应地调整应用的运行逻辑。

## 应用运行状态管理 Update!

这是一个典型的应用运行状态管理脚本基本结构：

**cmd/main**

```bash
#!/bin/bash

case $1 in
start)
    # 启动应用的命令，成功返回 0，失败返回 1
    exit 0
    ;;
stop)
    # 停止应用的命令，成功返回 0，失败返回 1
    exit 0
    ;;
status)
    # 检查应用运行状态，运行中返回 0，未运行返回 3
    exit 0
    ;;
*)
    exit 1
    ;;
esac
```

### 应用状态监控

系统需要准确知道您的应用是否正在运行。为此，系统会定期调用 `cmd/main` 脚本（传入 `status` 参数）来检查应用状态：

- 脚本返回 exit 0 表示应用正在运行
- 脚本返回 exit 3 表示应用未运行

> [!NOTE]
> **系统会在以下时机调用状态检查：**
>
> - 应用启动前检查一次
> - 应用运行期间定期轮询检查

### 应用启动流程

启动应用前，系统会先检查应用是否已经在运行。如果应用未运行，系统会调用 `cmd/main` 脚本（传入 `start` 参数）来启动应用。在这个阶段，您可以执行启动逻辑，比如检查配置文件、启动后台进程等。

### 应用停止流程

停止应用前，系统同样会先检查应用是否已经停止。如果应用仍在运行，系统会调用 `cmd/main` 脚本（传入 `stop` 参数）来停止应用。在这个阶段，您可以执行停止逻辑，比如保存当前状态、优雅地关闭后台进程等。

## 应用错误异常展示处理 New! V1.1.8+

> [!NOTE]
> 通过向 **`TRIM_TEMP_LOGFILE`** 环境变量（用户可见系统日志文件路径）写入应用错误日志信息并返回通用错误代码时，系统会自动将错误日志在前端展示为用户可见的内容（Dialog对话框形式）。

### 脚本中错误处理

在应用启动、安装、更新等过程中遇到错误时，可以向 **`TRIM_TEMP_LOGFILE`** 写入错误信息，然后退出脚本并返回错误码 **`1`**。例如：

**伪代码，实际脚本中需要结合应用具体业务逻辑场景！**

```bash
echo "Error: Something went wrong" > $TRIM_TEMP_LOGFILE
exit 1
```

### 模拟自定义异常信息返回案例

当应用启动过程中发生错误时，如：依赖配置文件缺失，可以按照以下方式处理：

**cmd/main**

```bash
#!/bin/bash

case $1 in
start)
    # 检查配置文件是否存在
    if [ ! -f "$TRIM_PKGETC/config.conf" ]; then
        echo "配置文件不存在, 应用启动失败！" > "${TRIM_TEMP_LOGFILE}"
        exit 1
    fi

    # 启动应用
    cd "$TRIM_APPDEST"
    ./myapp --config "$TRIM_PKGETC/config.conf" \
            --data "$TRIM_PKGVAR" \
            --port "$TRIM_SERVICE_PORT" \
            --user "$TRIM_USERNAME" \
            --log "$TRIM_TEMP_LOGFILE" &

    echo "应用启动完成"
    exit 0
    ;;
stop)
    echo "停止应用..."
    pkill -f "myapp.*$TRIM_SERVICE_PORT"
    exit 0
    ;;
status)
    # 检查应用是否在运行
    if pgrep -f "myapp.*$TRIM_SERVICE_PORT" > /dev/null; then
        echo "应用正在运行"
        exit 0
    else
        echo "应用未运行"
        exit 3
    fi
    ;;
*)
    exit 1
    ;;
esac
```

> [!WARNING]
> - 请不要使用 `echo` 命令直接输出错误信息，而是写入 `TRIM_TEMP_LOGFILE` 文件中。
> - 请不要使用 `exit` 命令直接退出脚本，而是返回错误码 `1`。
> - 如果不写入 `TRIM_TEMP_LOGFILE` 环境变量，直接 `exit 1` 则系统将展示标准错误信息：`执行XX脚本出错且原因未知`

![标准错误信息对话框](../../assets/site/assets/images/2025-12-31_034412_167-16ee914b3707a322f000ddb96aaba839.png)

---

- 上一页: [📘　开发指南](../category/开发指南.md)
- 下一页: [📚 【基础】Manifest](manifest.md)
