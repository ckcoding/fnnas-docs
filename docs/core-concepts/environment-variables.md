# 环境变量

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/environment-variables/](https://developer.fnnas.com/docs/core-concepts/environment-variables/)

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

## 开放 API 认证

- `TRIM_API_TOKEN`：应用调用开放 API 时使用的认证 token，使用方式参考 调用方式

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
