# 应用依赖

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/dependency/](https://developer.fnnas.com/docs/core-concepts/dependency/)

当应用依赖其他应用时，在 `manifest` 中使用 `install_dep_apps`。

**manifest**

```ini
install_dep_apps=database:cache
```

## 依赖顺序

声明多个依赖时，飞牛 fnOS 会从右到左安装和启用依赖。

例如，`cache` 需要先于 `database` 准备完成时，可以这样声明：

**manifest**

```ini
install_dep_apps=database:cache
```

依赖顺序应明确声明。嵌套依赖不会为当前应用递归解析。

## 版本要求

使用 `>` 声明依赖所需的最低版本：

**manifest**

```ini
install_dep_apps=database>2.2.2:cache
```

只有应用依赖某个版本引入的特定行为时，才声明版本要求。

## 嵌套依赖

依赖检查不递归。如果应用同时需要 `database` 和 `cache`，即使其中一个也依赖另一个，也应在当前应用中直接声明二者。

**manifest**

```ini
install_dep_apps=database:cache
```

## 建议

- 只声明应用直接需要的依赖。
- 在版本迭代中保持依赖名称稳定。
- 在干净设备上测试安装，确认依赖链可用。
- 依赖缺失或不可用时，显示清晰的用户可见错误信息。

---

- 上一页: [用户向导](wizard.md)
- 下一页: [中间件服务](middleware.md)
