# ⚙️　appcenter-cli

> 原始页面: [https://developer.fnnas.com/docs/cli/appcentercli/](https://developer.fnnas.com/docs/cli/appcentercli/)

`appcenter-cli` 是飞牛 fnOS 系统预装的应用中心管理工具，它让您能够通过命令行来管理应用的安装、配置和系统设置。无论您是开发者还是系统管理员，这个工具都能帮助您更高效地管理应用。

## 安装应用

### 通过 fpk 文件安装

使用 `appcenter-cli install-fpk` 命令可以安装打包好的应用文件：

```bash
# 基本安装命令
appcenter-cli install-fpk myapp.fpk

# 指定环境变量文件进行静默安装
appcenter-cli install-fpk myapp.fpk --env config.env
```

#### 环境变量文件格式

当应用包含安装向导时，您可以通过环境变量文件来跳过交互式配置。环境变量文件使用简单的键值对格式：

**config.env**

```yaml
# 应用配置
wizard_admin_username=admin
wizard_admin_password=mypassword123
wizard_database_type=sqlite
wizard_app_port=8080

# 系统设置
wizard_agree_terms=true
```

#### 设置默认安装位置

如果您的系统有多个存储空间，可以设置默认的安装位置：

```bash
# 查看当前默认存储空间
appcenter-cli default-volume

# 设置存储空间1为默认安装位置
appcenter-cli default-volume 1

# 设置存储空间2为默认安装位置
appcenter-cli default-volume 2
```

### 从本地目录安装

当您在开发环境中测试应用时，可以直接从应用目录安装，无需先打包成 fpk 文件：

```bash
# 在应用开发目录中执行
cd /path/to/myapp
appcenter-cli install-local
```

这个命令会自动完成打包和安装过程，大大提升开发测试效率。

## 系统管理

### 手动安装功能

当您需要与团队成员分享应用时，可以临时开启手动安装功能：

```bash
# 查看当前状态
appcenter-cli manual-install

# 开启手动安装功能
appcenter-cli manual-install enable

# 关闭手动安装功能
appcenter-cli manual-install disable
```

开启后，其他用户就可以通过应用中心的手动安装入口来安装您分享的 fpk 文件。

### 应用管理

```bash
# 查看已安装的应用列表
appcenter-cli list

# 启动应用
appcenter-cli start myapp

# 停止应用
appcenter-cli stop myapp
```

## 最佳实践

### 安装前准备

1. 检查存储空间：确保有足够的存储空间安装应用
2. 准备配置文件：为包含向导的应用准备环境变量文件
3. 验证 fpk 文件：确保 fpk 文件完整且未损坏

### 开发工作流

1. 本地开发：使用 install-local 快速测试
2. 打包测试：使用 install-fpk 测试打包版本
3. 配置管理：使用环境变量文件管理不同环境的配置

### 安全考虑

- 手动安装功能仅在需要时开启，使用完毕后及时关闭
- 环境变量文件包含敏感信息，注意文件权限管理
- 生产环境安装前先在测试环境验证

通过合理使用 `appcenter-cli`，您可以更高效地管理飞牛 fnOS 应用，提升开发和部署效率。

---

- 上一页: [📦　fnpack](fnpack.md)
- 下一页: [🔄　文档更新日志](../category/文档更新日志.md)
