# 运行时环境

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/runtime/](https://developer.fnnas.com/docs/core-concepts/runtime/)

应用可以使用 Python、Node.js 或 Java 等打包运行时环境。请在 `manifest` 中通过 `install_dep_apps` 声明所需的运行时包。

## Python

**manifest**

```ini
install_dep_apps=python312
```

运行 Python 命令前，先将运行时路径加入 `PATH`：

```bash
export PATH=/var/apps/python312/target/bin:$PATH

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Node.js

**manifest**

```ini
install_dep_apps=nodejs_v22
```

```bash
export PATH=/var/apps/nodejs_v22/target/bin:$PATH

node -v
npm -v
```

## Java

**manifest**

```ini
install_dep_apps=java-21-openjdk
```

```bash
export PATH=/var/apps/java-21-openjdk/target/bin:$PATH

java --version
```

## 建议

- 声明应用实际使用的运行时包。
- 在生命周期脚本中调用运行时命令前，将运行时 bin 目录加入 PATH。
- 将应用自身依赖保存在应用目录或专用虚拟环境中。
- 在干净的飞牛 fnOS 设备上测试应用包，确认运行时依赖可以正确安装。

---

- 上一页: [中间件服务](middleware.md)
- 下一页: [图标](icon.md)
