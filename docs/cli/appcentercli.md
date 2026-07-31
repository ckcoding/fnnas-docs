# appcenter-cli

> 原始页面: [https://developer.fnnas.com/docs/cli/appcentercli/](https://developer.fnnas.com/docs/cli/appcentercli/)

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
