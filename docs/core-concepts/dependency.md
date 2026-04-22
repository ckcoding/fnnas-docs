# 🔥 【进阶】应用依赖关系

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/dependency/](https://developer.fnnas.com/docs/core-concepts/dependency/)

在飞牛 fnOS 应用生态中，应用之间可能存在依赖关系。理解和管理这些依赖关系对于应用的正确运行至关重要。

## 声明依赖关系

应用依赖是指一个应用需要其他应用先安装并运行才能正常工作。在 `manifest` 文件中，通过 `install_dep_apps` 字段来声明应用依赖。

**manifest**

```yaml
version=1.0.0
install_dep_apps=dep2:dep1
```

## 依赖管理

### 依赖检查逻辑

应用中心在应用安装、启用、停用、卸载、更新等流程中，会自动检查依赖关系：

1. 安装和启用流程：检查依赖应用是否已安装和已启用，如果未安装则自动安装，如果未启用则自动启用
2. 停用和卸载流程：检查是否有其他应用依赖当前应用，如果有则提示自动停用
3. 更新流程： 检查是否有其他应用依赖当前应用，如果有则提示更新期间自动停用

### 依赖顺序

当存在多个依赖时，执行自动安装和自动启用的顺序是从后往前一个一个执行。

```yaml
# 正确的依赖顺序，安装时将先安装dep1，后安装dep2
install_dep_apps=dep2:dep1

# 错误的依赖顺序，如果dep2依赖于dep1，可能导致问题
install_dep_apps=dep1:dep2
```

### 嵌套依赖处理

应用中心仅对一层依赖进行检查，不做递归检查。如果 **应用A** 依赖 **应用B**，但不直接依赖于 **应用C**，同时 **应用B** 又依赖 **应用C**，则需要在 **应用A** 中同时声明依赖 **应用B** 和 **应用C**：

```yaml
# 嵌套依赖的平铺定义
install_dep_apps=depB:depC
```

---

- 上一页: [📚 【基础】用户向导](wizard.md)
- 下一页: [🔥 【进阶】运行时环境](runtime.md)
