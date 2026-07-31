# 图标

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/icon/](https://developer.fnnas.com/docs/core-concepts/icon/)

应用包需要提供包图标，应用入口也可以单独配置入口图标。包图标用于应用中心、安装包识别等场景；入口图标用于桌面图标、文件打开方式等用户入口。

## 包图标

应用包根目录需要包含两个图标文件：

- ICON.PNG：64 x 64 px
- ICON_256.PNG：256 x 256 px

示例结构：

```text
myapp/
├── ICON.PNG
├── ICON_256.PNG
├── app/
├── config/
├── cmd/
└── manifest
```

## 设计要求

- 格式：PNG 或 JPG
- 色彩空间：sRGB
- 文件大小：不超过 1024 KB
- 画布：完整正方形图片
- 圆角：图标视觉主体应使用圆角矩形风格。不要使用直角满铺的方形主体；圆角、留白和阴影应尽量与系统图标保持一致。

两个尺寸应使用一致的视觉识别。图标在 64 x 64 px 下仍需要清晰可辨，重要内容不要贴近画布边缘，也不要依赖过细的文字或装饰细节。

可以参考系统图标的圆角、留白和层次关系：

![系统设置图标示例](../../assets/site/assets/images/icon-example-system-settings-2787823b1bb660e9518d03faed4b4a47.png)

## 应用入口图标

应用入口可以引用 UI 目录下的图标，用于注册桌面图标或注册文件打开方式。推荐将入口图标放在 `app/ui/images/` 下：

```text
myapp/
└── app/
    └── ui/
        ├── config
        └── images/
            ├── icon_64.png
            └── icon_256.png
```

在 `app/ui/config` 中通过 `icon` 字段引用：

**app/ui/config**

```json
{
  ".url": {
    "myapp.main": {
      "title": "My App",
      "icon": "images/icon_{0}.png",
      "type": "iframe",
      "protocol": "http",
      "port": "8080",
      "url": "/",
      "allUsers": true
    }
  }
}
```

飞牛 fnOS 会将 `{0}` 替换为所需的图标尺寸，例如 `icon_64.png` 或 `icon_256.png`。

入口配置的更多规则可参考 [应用入口](app-entry.md)。

## 检查清单

打包前建议确认：

- 根目录包含 ICON.PNG 和 ICON_256.PNG。
- 图标文件大小不超过 1024 KB。
- 64 px 图标仍能看清主体。
- 图标主体是圆角矩形风格，而不是直角方块铺满画布。
- 如果入口配置了 images/icon_{0}.png，对应的 icon_64.png 和 icon_256.png 都已放入 UI 目录。

---

- 上一页: [运行时环境](runtime.md)
- 下一页: [应用案例](../category/应用案例.md)
