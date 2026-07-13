# 用户向导

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/wizard/](https://developer.fnnas.com/docs/core-concepts/wizard/)

向导用于在安装、升级、卸载或配置时收集用户输入。向导收集到的值会作为环境变量提供给生命周期脚本。

只有当应用确实需要用户提供无法安全自动检测或默认处理的信息时，才使用向导。表单应聚焦于安装、运行或配置应用所必需的值。

## 向导文件

飞牛 fnOS 支持四种向导文件：

- `wizard/install`：安装时显示。
- `wizard/upgrade`：升级时显示。
- `wizard/uninstall`：卸载时显示。
- `wizard/config`：安装后从应用设置中显示。用户可以继续修改应用配置，提交后的值会继续作为环境变量提供给应用使用。

## 基本结构

每个向导文件都是一个由步骤组成的 JSON 数组。

- `stepTitle`：步骤标题。
- `items`：该步骤中显示的表单项。
- `field`：字段名。收集到的值会成为同名环境变量。

**wizard/install**

```json
[
  {
    "stepTitle": "Setup",
    "items": [
      {
        "type": "text",
        "field": "wizard_username",
        "label": "Username",
        "initValue": "admin",
        "rules": [
          {
            "required": true,
            "message": "Enter a username"
          }
        ]
      }
    ]
  }
]
```

字段 `wizard_username` 会变成名为 `wizard_username` 的环境变量。

## 字段类型

| 类型 | 用途 |
| --- | --- |
| `text` | 短文本、端口、路径、用户名等普通值 |
| `password` | 不应明文显示的密钥或令牌 |
| `radio` | 少量互斥选项 |
| `checkbox` | 多选项 |
| `select` | 较长的互斥选项列表 |
| `switch` | 布尔风格选项 |
| `tips` | 只读提示文本 |

带选项字段示例：

```json
{
  "type": "select",
  "field": "wizard_database_type",
  "label": "Database",
  "initValue": "sqlite",
  "options": [
    {
      "label": "SQLite",
      "value": "sqlite"
    },
    {
      "label": "PostgreSQL",
      "value": "postgresql"
    }
  ]
}
```

提示文本示例：

```json
{
  "type": "tips",
  "helpText": "Review the configuration before continuing."
}
```

## 校验规则

通过 `rules` 数组添加校验规则。

```json
{
  "type": "text",
  "field": "wizard_port",
  "label": "Service port",
  "rules": [
    {
      "required": true,
      "message": "Enter a port"
    },
    {
      "pattern": "^[0-9]+$",
      "message": "Use numbers only"
    }
  ]
}
```

常见规则：

- `required`：必填。
- `min` 和 `max`：长度或数值范围。
- `len`：固定长度。
- `pattern`：正则表达式。

## 使用向导值

向导值会作为环境变量提供给生命周期脚本。可以用于生成配置文件、选择安装模式、设置端口或路径，以及控制可选功能。

**cmd/install_callback**

```bash
#!/bin/bash

echo "Database type: $wizard_database_type"
echo "Service port: $wizard_port"
```

脚本中应将向导值按字符串处理，并在使用前再次校验。

## 字段命名

- 使用稳定的字段名。修改字段名会改变环境变量名。
- 自定义字段建议使用 wizard_ 前缀，例如 wizard_port。
- 自定义向导字段不要使用 TRIM_ 前缀。该前缀保留给系统变量。
- 尽量兼容已发布版本使用过的字段名。

## 设计建议

- 只询问应用安装、运行或配置所需的值。
- 尽可能提供合理默认值。
- 使用简短标签和清晰的校验信息。
- 密钥类输入使用 password。
- 不要将密钥写入日志。
- 在生命周期脚本中使用前，再次校验输入值。

---

- 上一页: [统一网关](gateway-registration.md)
- 下一页: [应用依赖](dependency.md)
