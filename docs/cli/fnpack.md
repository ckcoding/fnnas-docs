# fnpack

> 原始页面: [https://developer.fnnas.com/docs/cli/fnpack/](https://developer.fnnas.com/docs/cli/fnpack/)

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

- 上一页: [开发工具](../category/开发工具.md)
- 下一页: [appcenter-cli](appcentercli.md)
