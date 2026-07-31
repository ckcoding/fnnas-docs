# Docker 应用案例

> 原始页面: [https://developer.fnnas.com/docs/examples/docker/](https://developer.fnnas.com/docs/examples/docker/)

当应用已经容器化，或更适合以一个或多个容器交付并由 Docker Compose 管理时，可以使用 Docker 应用模板。

这一页从零创建一个 `hello-docker` 示例应用，并将它打包成可以安装运行的 `.fpk` 文件。示例应用使用 `nginx:alpine` 启动一个 Web 页面，用户可以从飞牛 fnOS 桌面入口打开它。

本案例使用：

- 应用包名：hello-docker
- Docker 镜像：nginx:alpine
- 服务端口：8080
- 访问方式：端口入口

如果应用只是一个简单的 Node.js、Python、Go 或二进制服务，也可以参考 [Native 应用案例](native.md)。

## 创建 Docker 应用项目

创建应用包目录：

```bash
fnpack create hello-docker --template docker
cd hello-docker
```

生成后的目录大致如下：

```text
hello-docker/
├── app/
│   ├── docker/
│   │   └── docker-compose.yaml
│   └── ui/
│       ├── config
│       └── images/
├── cmd/
│   └── main
├── config/
│   ├── privilege
│   └── resource
├── wizard/
├── manifest
├── ICON.PNG
└── ICON_256.PNG
```

其中：

- app/docker/docker-compose.yaml 存放 Docker Compose 编排文件。
- config/resource 声明 Docker 项目资源。
- cmd/main 负责返回应用运行状态。
- app/ui/config 用于注册桌面图标或其他入口。

## 编辑 manifest

将 `manifest` 改为：

**hello-docker/manifest**

```ini
appname=hello-docker
version=1.0.0
display_name=Hello Docker
desc=A minimal Docker application.
source=thirdparty
platform=all
maintainer=Example Team
distributor=Example Team
desktop_uidir=ui
desktop_applaunchname=hello-docker.main
service_port=8080
checkport=true
ctl_stop=true
```

说明：

- platform=all 适用于不包含平台相关二进制的应用包。镜像本身仍需要支持目标设备架构。
- service_port=8080 表示应用在宿主机上使用的访问端口。
- desktop_applaunchname=hello-docker.main 指向应用卡片打开的入口 ID。
- ctl_stop=true 表示应用中心显示启动、停止和运行状态。

更多字段可参考 [Manifest](../core-concepts/manifest.md)。

## 准备页面文件

创建一个要由 nginx 提供的页面：

```bash
mkdir -p app/docker/html
```

写入页面文件：

**hello-docker/app/docker/html/index.html**

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hello Docker</title>
    <style>
      body {
        margin: 0;
        font-family: sans-serif;
        display: grid;
        min-height: 100vh;
        place-items: center;
        background: #f5f7fb;
        color: #1f2937;
      }
      main {
        text-align: center;
      }
    </style>
  </head>
  <body>
    <main>
      <h1>Hello Docker</h1>
      <p>This page is served by nginx inside a Docker container.</p>
    </main>
  </body>
</html>
```

## 编写 Docker Compose

将 `app/docker/docker-compose.yaml` 改为：

**hello-docker/app/docker/docker-compose.yaml**

```yaml
services:
  web:
    image: nginx:alpine
    container_name: hello-docker-web
    restart: unless-stopped
    ports:
      - "${TRIM_SERVICE_PORT}:80"
    volumes:
      - "${TRIM_APPDEST}/docker/html:/usr/share/nginx/html:ro"
```

这个 Compose 文件会：

- 使用 nginx:alpine 启动 Web 服务。
- 将容器端口 80 映射到 manifest.service_port 声明的端口。
- 将应用包中的 app/docker/html 目录挂载到 nginx 的网页目录。

Compose 文件可以使用飞牛 fnOS 提供的环境变量。常用变量包括：

- TRIM_SERVICE_PORT：manifest.service_port 声明的服务端口。
- TRIM_APPDEST：应用安装后的目标目录。
- TRIM_PKGVAR：应用运行时数据目录。
- TRIM_DATA_SHARE_PATHS：config/resource 声明的数据共享路径。

更多变量可参考 [环境变量](../core-concepts/environment-variables.md)。

> [!NOTE]
> 如果应用要同时支持 x86 和 ARM 设备，请确认使用的镜像支持对应架构。应用包可以声明 `platform=all`，但镜像不支持目标架构时，容器仍然无法启动。

## 声明 Docker 项目资源

将 `config/resource` 改为：

**hello-docker/config/resource**

```json
{
  "docker-project": {
    "projects": [
      {
        "name": "hello-docker",
        "path": "docker"
      }
    ]
  }
}
```

字段说明：

- docker-project.projects[].name：Docker Compose 项目名称，应保持稳定。
- docker-project.projects[].path：相对于 app/ 目录的路径。这里指向 app/docker/。

如果应用需要让用户在文件管理器中访问数据，再额外声明 `data-share`。更多资源声明可参考 [应用资源](../core-concepts/resource.md)。

## 权限配置

Docker 应用通常由容器承载主要进程，`config/privilege` 不用于指定容器内进程身份。这里保留默认的 package 配置，主要用于保持包结构完整，也便于后续应用形态调整或补充本地脚本。

将 `config/privilege` 改为：

**hello-docker/config/privilege**

```json
{
  "defaults": {
    "run-as": "package"
  },
  "username": "hello-docker",
  "groupname": "hello-docker"
}
```

如果应用额外包含本地脚本或原生进程，再根据实际需要调整权限配置。更多说明可参考 [应用权限](../core-concepts/privilege.md)。

## 运行状态检查

Docker 应用的启动和停止由飞牛 fnOS 根据 Docker 项目资源处理。`cmd/main` 中的 `start` 和 `stop` 通常不需要额外操作，但 `status` 仍需要准确判断应用是否正在运行。

将 `cmd/main` 改为：

**hello-docker/cmd/main**

```bash
#!/bin/bash

CONTAINER_NAME="hello-docker-web"

is_running() {
  docker inspect "$CONTAINER_NAME" 2>/dev/null | grep -q '"Status": "running"'
}

case "$1" in
  start)
    exit 0
    ;;
  stop)
    exit 0
    ;;
  status)
    if is_running; then
      exit 0
    fi
    exit 3
    ;;
  *)
    echo "Unknown command: $1" > "$TRIM_TEMP_LOGFILE"
    exit 1
    ;;
esac
```

选择状态检查容器时，建议使用最能代表应用可用性的容器。这个示例只有一个容器，所以直接检查 `hello-docker-web`。

## 配置桌面入口

将 `app/ui/config` 改为：

**hello-docker/app/ui/config**

```json
{
  ".url": {
    "hello-docker.main": {
      "title": "Hello Docker",
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

注意：

- 入口 ID 使用 hello-docker 作为前缀，并与 manifest 中的 desktop_applaunchname 保持一致。
- port 应与 manifest.service_port 和 Compose 端口映射保持一致。
- 入口配置的更多规则可参考 应用入口。

## 打包和验证

在应用包目录执行：

```bash
fnpack build
```

成功后会生成：

```text
hello-docker.fpk
```

将 `hello-docker.fpk` 安装到飞牛 fnOS 测试设备后，检查以下内容：

- 应用是否能正常安装。
- Docker 镜像是否能拉取。
- 容器是否按预期启动和停止。
- cmd/main status 是否能正确返回运行状态。
- 应用卡片是否能打开 Hello Docker 页面。
- 目标设备架构是否被镜像支持。

**可选：改用统一网关**

Docker 应用也可以使用统一网关，而不是直接暴露宿主机端口。做法是将应用安装目录 `${TRIM_APPDEST}` 挂载到容器内，让容器中的服务在该目录下创建 Unix Socket。

入口配置中使用 `gatewayPrefix` 和 `gatewaySocket`：

**hello-docker/app/ui/config**

```json
{
  ".url": {
    "hello-docker.main": {
      "title": "Hello Docker",
      "icon": "images/icon_{0}.png",
      "type": "iframe",
      "protocol": "",
      "gatewayPrefix": "/app/hello-docker",
      "gatewaySocket": "app.sock",
      "url": "/app/hello-docker",
      "allUsers": true
    }
  }
}
```

Compose 中将 `${TRIM_APPDEST}` 挂载到容器内，并把 Socket 路径传给服务：

**hello-docker/app/docker/docker-compose.yaml**

```yaml
services:
  web:
    image: my-app:latest
    container_name: hello-docker-web
    restart: unless-stopped
    volumes:
      - "${TRIM_APPDEST}:/app/target:rw"
    environment:
      GATEWAY_SOCKET: /app/target/app.sock
```

容器内的 Web 服务需要监听 `/app/target/app.sock`。宿主机上对应的 Socket 路径为：

```text
/var/apps/hello-docker/target/app.sock
```

统一网关会把 `/app/hello-docker` 下的请求转发到这个 Socket。`protocol` 和 `port` 不参与统一网关路由。

如果应用只通过统一网关提供访问入口，可以不依赖 `manifest.service_port` 和端口入口；如果应用同时提供独立端口访问和统一网关访问，则需要分别维护端口映射和网关 Socket。

更多规则可参考 [统一网关](../core-concepts/gateway-registration.md)。

**排查要点**

- 入口打不开：检查 manifest.service_port、docker-compose.yaml 中映射到宿主机的端口，以及 app/ui/config 中入口的 port 是否一致。
- 状态一直显示未运行：确认 cmd/main 中的 CONTAINER_NAME 与 Compose 文件中的 container_name 一致。没有写 container_name 时，Docker Compose 会生成项目相关的容器名称，脚本中需要按实际名称检查。
- 镜像无法启动：确认目标设备可以拉取镜像，并确认镜像支持设备架构。nginx:alpine 是多架构镜像，适合作为入门示例；实际应用镜像也需要做同样检查。

---

- 上一页: [Native 应用案例](native.md)
- 下一页: [开发工具](../category/开发工具.md)
