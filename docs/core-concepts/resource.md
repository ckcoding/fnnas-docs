# 应用资源

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/resource/](https://developer.fnnas.com/docs/core-concepts/resource/)

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
