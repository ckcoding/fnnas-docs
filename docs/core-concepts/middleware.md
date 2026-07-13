# 中间件服务

> 原始页面: [https://developer.fnnas.com/docs/core-concepts/middleware/](https://developer.fnnas.com/docs/core-concepts/middleware/)

应用可以使用 Redis、MinIO 或 RabbitMQ 等中间件服务。请在 `manifest` 中通过 `install_dep_apps` 声明所需服务。

## Redis

**manifest**

```ini
install_dep_apps=redis
```

Python 示例：

```python
import redis

pool = redis.ConnectionPool(
    host="127.0.0.1",
    port=6379,
    db=1,
    decode_responses=True,
    max_connections=10,
)

client = redis.Redis(connection_pool=pool)
client.lpush("my_list", "item1", "item2")
items = client.lrange("my_list", 0, -1)
print(items)
```

建议使用独立数据库编号或 key 前缀，避免与其他应用冲突。

## MinIO

**manifest**

```ini
install_dep_apps=minio
```

Python 示例：

```python
from minio import Minio

client = Minio(
    endpoint="127.0.0.1:9000",
    access_key="your_access_key",
    secret_key="your_secret_key",
    secure=False,
)

bucket_name = "my-bucket"

if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
```

请安全保存访问密钥，不要在应用包中硬编码生产凭据。

## RabbitMQ

**manifest**

```ini
install_dep_apps=rabbitmq
```

Python 示例：

```python
import pika

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="127.0.0.1",
        port=5672,
        virtual_host="/",
        credentials=credentials,
    )
)

channel = connection.channel()
channel.queue_declare(queue="my_queue", durable=True)
channel.basic_publish(exchange="", routing_key="my_queue", body=b"hello")
connection.close()
```

请使用应用专属的队列、交换机和路由键。

## 建议

- 只声明应用实际需要的中间件服务。
- 在干净的飞牛 fnOS 设备上测试安装。
- 服务不可用时，显示清晰的用户可见错误信息。
- 不要将凭据提交到源码仓库或打包模板中。
- 为数据库、桶、队列和 key 使用命名空间。

---

- 上一页: [应用依赖](dependency.md)
- 下一页: [运行时环境](runtime.md)
