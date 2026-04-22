# 📋　准备工作

> 原始页面: [https://developer.fnnas.com/docs/quick-started/prerequisites/](https://developer.fnnas.com/docs/quick-started/prerequisites/)

> [!TIP]
> 你可以从 [飞牛官网](https://www.fnnas.com/download?key=fnos) 下载飞牛 fnOS 安装镜像进行安装！飞牛 fnOS 既支持物理机安装，也支持虚拟机安装

关于飞牛 fnOS 的底层架构：

- Linux 内核版本: 当前飞牛 fnOS 最新内核版本为 6.12.18
- 系统架构支持: 当前飞牛 fnOS 仅支持 x86_64 (AMD64) 设备安装，即应用的编译选项也需要选择 x86_64

## 系统要求

> [!WARNING]
> 为了数据安全考虑，不建议在有重要数据存储的或有其他正常用途的飞牛 fnOS 设备上进行开发和测试

在应用测试阶段，为了实机测试你的应用，确保应用的运行正常，你需要先准备一台已安装飞牛 fnOS 的设备。

- 系统版本: 飞牛 fnOS 0.9.27 及以上版本
- 存储空间: 至少创建一个存储空间，可用于安装应用
- 管理员权限: 拥有该设备的管理权限，只有管理员才能操作应用安装、卸载，以及更改系统设置等

在开发阶段，你既可以在本地开发，也可以使用远程方式在飞牛 fnOS 设备上开发。当使用远程方式在飞牛 fnOS 设备上开发时，不仅能保证环境的一致性，结合 `appcenter-cli install-local` 命令，可以实现应用快速安装，提升调试效率。

## 应用技术栈

fnOS 基于 Linux 内核（Debian 发行版）深度开发，支持多种技术栈的应用运行，你可以根据自己擅长的语言进行选择。

- 服务开发语言: Node.js、Python、Java、Go 以及 Linux 运行时支持的其他语言
- 前端开发语言: Html/Javascript/CSS 以及现代桌面和移动浏览器引擎支持的其他语言和框架

## CLI 工具

- fnpack: 应用打包工具
- appcenter-cli: 应用中心命令行工具（已在飞牛 fnOS 环境中预装）

---

- 上一页: [🚀　快速开始](../category/快速开始.md)
- 下一页: [✨　创建应用](create-application.md)
