# 📚 【基础】环境变量

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/environment-variables/](https://developer.fnnas.com/docs/core-concepts/environment-variables/)

> [!NOTE]
> 本文档于 **2025-12-31** 新增了部分内容。

环境变量就像是应用运行时的"工具箱"，里面装着各种有用的信息。当您的应用在飞牛 fnOS 系统中运行时，系统会自动提供这些环境变量，让您能够了解应用的状态、获取系统信息、访问各种路径等。

环境变量主要来自两个地方：

- manifest 文件：您在 manifest 中定义的字段会自动转换为环境变量
- 用户向导：用户在安装、配置等向导中的选择也会变成环境变量

## 应用相关变量

这些变量告诉您关于当前应用的各种信息：

### 基本信息

- TRIM_APPNAME - 应用的名称（来自 manifest 中的 appname）
- TRIM_APPVER - 应用的版本号（来自 manifest 中的 version）
- TRIM_OLD_APPVER - 应用升级前的版本号（仅在升级时可用）

### 路径信息

- TRIM_APPDEST - 应用可执行文件目录路径（target 文件夹）
- TRIM_PKGETC - 配置文件目录路径（etc 文件夹）
- TRIM_PKGVAR - 动态数据目录路径（var 文件夹）
- TRIM_PKGTMP - 临时文件目录路径（tmp 文件夹）
- TRIM_PKGHOME - 用户数据目录路径（home 文件夹）
- TRIM_PKGMETA - 元数据目录路径（meta 文件夹）
- TRIM_APPDEST_VOL - 应用安装的存储空间路径

### 网络和端口

- TRIM_SERVICE_PORT - 应用监听的端口号（来自 manifest 中的 service_port）

### 用户和权限

- TRIM_USERNAME - 应用专用用户名
- TRIM_GROUPNAME - 应用专用用户组名
- TRIM_UID - 应用用户 ID
- TRIM_GID - 应用用户组 ID
- TRIM_RUN_USERNAME - 当前执行脚本的用户名（可能是 root 或应用用户）
- TRIM_RUN_GROUPNAME - 当前执行脚本的用户组名
- TRIM_RUN_UID - 当前执行脚本的用户 ID
- TRIM_RUN_GID - 当前执行脚本的用户组 ID

### 数据共享

- TRIM_DATA_SHARE_PATHS - 数据共享路径列表，多个路径用冒号分隔

### 临时日志 Update!

- TRIM_TEMP_LOGFILE - 系统日志文件路径（用户可见的日志）
    - 该日志路径变量在 cmd/** 下的 `生命周期脚本` 及 `运行状态管理脚本` 执行过程中有效，包括：cmd/main、cmd/install_*、cmd/upgrade_*。配置和卸载暂不支持，即cmd/config_*、cmd/uninstall_*。
    - 应用中心执行调用对应脚本时，可以直接向 ${TRIM_TEMP_LOGFILE} 变量对应的临时路径写入日志信息，当脚本执行 `exit 1` 时，应用中心会将${TRIM_TEMP_LOGFILE}中日志信息传递给前台页面，通过Dialog对话框展示给用户New!V1.1.8+

> [!NOTE]
> - 如需了解更多关于`生命周期脚本` 及 `运行状态管理脚本` 的信息，请参考 [架构概述](framework.md) 章节内容进行学习

- TRIM_TEMP_UPGRADE_FOLDER - 升级过程的临时目录
- TRIM_PKGINST_TEMP_DIR - 安装包解压的临时目录
- TRIM_TEMP_TPKFILE - fpk 包解压目录

### CMD 脚本

- TRIM_APP_STATUS - 当前状态(INSTALL、START、UPGRADE、UNINSTALL、STOP、CONFIG等)

### 获取授权目录列表 New! V1.1.8+

- TRIM_DATA_ACCESSIBLE_PATHS - 可访问路径列表，多个路径用冒号分隔，仅返回读写/只读的目录
    - 当变更时，通过 cmd/config_init 和 cmd/config_callback应用配置流程来通知变化。应用脚本内开发者自行结合实际业务场景将路径信息通知应用进程

> [!WARNING]
> - 系统最低版本：V1.1.8
> - 注意：应用自身仍需要单独自行判断是否拥有子目录和文件的读写权限

## 系统相关变量

这些变量提供关于飞牛 fnOS 系统的信息：

### 版本信息

- TRIM_SYS_VERSION - 完整的系统版本号
- TRIM_SYS_VERSION_MAJOR - 系统主版本号
- TRIM_SYS_VERSION_MINOR - 系统次版本号
- TRIM_SYS_VERSION_BUILD - 系统构建版本号

### 系统特征

- TRIM_SYS_ARCH - 系统 CPU 架构（如 x86_64）
- TRIM_KERNEL_VERSION - 系统内核版本号
- TRIM_SYS_MACHINE_ID - 设备的唯一标识符
- TRIM_SYS_LANGUAGE - 系统语言设置

## 向导相关变量

当用户通过安装向导、配置向导等进行操作时，他们的选择会变成环境变量。这些变量没有 `TRIM_` 前缀，完全由您的向导配置决定。

例如，如果您在向导中定义了：

- 数据库端口：db_port
- 管理员密码：admin_password
- 安装路径：install_path

那么这些就会变成环境变量：

- db_port
- admin_password
- install_path

## 使用示例

下面是一个典型的应用启动脚本示例，展示了如何使用这些环境变量：

**cmd/main**

```bash
#!/bin/bash

case $1 in
start)
    echo "启动应用: $TRIM_APPNAME 版本: $TRIM_APPVER"
    echo "应用目录: $TRIM_APPDEST"
    echo "配置文件目录: $TRIM_PKGETC"
    echo "数据目录: $TRIM_PKGVAR"
    echo "服务端口: $TRIM_SERVICE_PORT"

    # 检查配置文件是否存在
    if [ ! -f "$TRIM_PKGETC/config.conf" ]; then
        echo "配置文件不存在，创建默认配置..."
        cp "$TRIM_APPDEST/config.conf.example" "$TRIM_PKGETC/config.conf"
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

stop)
    echo "停止应用..."
    pkill -f "myapp.*$TRIM_SERVICE_PORT"
    exit 0
    ;;

*)
    echo "未知命令: $1"
    exit 1
    ;;
esac
```

## 注意事项

1. 变量命名：系统提供的变量都以 TRIM_ 开头，您的向导变量不要使用这个前缀
2. 路径安全：使用路径变量时，建议先检查目录是否存在
3. 权限考虑：注意 TRIM_RUN_USERNAME 和 TRIM_USERNAME 的区别，前者是执行脚本的用户，后者是应用专用用户
4. 版本兼容：使用系统版本变量时，注意检查版本兼容性

这些环境变量让您的应用能够适应不同的安装环境，获取必要的系统信息，并响应用户的配置选择。

---

- 上一页: [📚 【基础】Manifest](manifest.md)
- 下一页: [📚 【基础】应用权限](privilege.md)
