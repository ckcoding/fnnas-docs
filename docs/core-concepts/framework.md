# 应用框架

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/framework/](https://developer.fnnas.com/docs/core-concepts/framework/)

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

- 上一页: [开发指南](../category/开发指南.md)
- 下一页: [Manifest](manifest.md)
