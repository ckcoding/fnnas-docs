# ð¥ ãè¿é¶ãä¸­é´ä»¶æå¡

> Source: [https://developer.fnnas.com/docs/core-concepts/middleware/](https://developer.fnnas.com/docs/core-concepts/middleware/)

## redis

![](../../assets/static/appcenter-marketing/20250918175215505.png)

å¦æä½ çåºç¨éè¦ä¾èµ redisï¼è¯·å¨ `manifest` ç `install_dep_apps` å­æ®µä¸­æ·»å redisï¼åºç¨ä¸­å¿å°ç¡®ä¿æ¨çåºç¨å®è£åå¯å¨æ¶ redis æå¡å·²å¨è¿è¡ã

**manifest**

```yaml
install_dep_apps=redis
```

Python ä½¿ç¨ç¤ºä¾

```python
import redis

def main():
    # åå»ºè¿æ¥æ± ï¼æå®é»è¾æ°æ®åºï¼å¦ db=1ï¼ï¼é²æ­¢å²çª
    # é»è®¤éç½®ä¸ç redis å¯éè¿ host 127.0.0.1 å port 6739 è¿æ¥
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1, decode_responses=True, max_connections=10)

    # ä»è¿æ¥æ± è·åè¿æ¥
    client = redis.Redis(connection_pool=pool)

    # ä½¿ç¨è¿æ¥
    client.lpush('my_list', 'item1', 'item2')
    items = client.lrange('my_list', 0, -1)
    print(items)  # è¾åº: ['item2', 'item1']

    # ä¸éè¦æå¨å³é­è¿æ¥ï¼è¿æ¥æ± ä¼ç®¡ç
    # ä½å¨ç¨åºéåºåï¼å¯ä»¥å³é­è¿æ¥æ±
    # pool.disconnect()
    # å¦éåæ¢æ°æ®åºï¼å¯éæ°åå»ºè¿æ¥æ± å¹¶æå®ä¸åç db åæ°

if __name__ == "__main__":
    main()
```

## MinIO

![](../../assets/static/appcenter-marketing/20250918175141281.png)

MinIO æ¯ä¸ä¸ªé«æ§è½ãäºåççå¼æºå¯¹è±¡å­å¨ç³»ç»ï¼å®å¨å¼å®¹ Amazon S3 APIï¼ä¸æ¯æç§æåé¨ç½²ã

å¦æä½ çåºç¨éè¦ä¾èµMinIOï¼è¯·å¨ `manifest` ç `install_dep_apps` å­æ®µä¸­æ·»å minioï¼åºç¨ä¸­å¿å°ç¡®ä¿æ¨çåºç¨å®è£åå¯å¨æ¶ MinIO æå¡å·²å¨è¿è¡ã

**manifest**

```yaml
install_dep_apps=minio
```

Python ä½¿ç¨ç¤ºä¾

```python
import minio
from minio import Minio
from minio.error import S3Error

# 1. åå§åå®¢æ·ç«¯
# é»è®¤éç½®ä¸ç MinIO å¯éè¿ host 127.0.0.1 å port 9000 è¿æ¥
client = Minio(
    endpoint="127.0.0.1:9000",
    access_key="your_access_key",   # æ¿æ¢ä¸ºä½ ç MinIO ç®¡çåç¨æ·å æ Access Key
    secret_key="your_secret_key",   # æ¿æ¢ä¸ºä½ ç MinIO ç®¡çåå¯ç  æ Secret Key
    secure=False                    # æ¬å°æµè¯éå¸¸ä¸º False
)

# 2. å®ä¹æ¡¶å
bucket_name = "my-bucket"

# åå»º Bucket ç¤ºä¾
def main():
    try:
        # æ£æ¥æ¡¶æ¯å¦å­å¨ï¼å¦æä¸å­å¨ååå»ºå®
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' å·²åå»º.")
        else:
            print(f"Bucket '{bucket_name}' å·²å­å¨.")
    except S3Error as err:
        print("åå»º Bucket æ¶åçéè¯¯:", err)

if __name__ == "__main__":
    main()
```

æå¼ MinIO ç®¡çåå°ï¼ç¡®è®¤ my-bucket è¢«æååå»ºï¼

![](../../assets/static/appcenter-marketing/20250918185922659.png)

## RabbitMQ

![](../../assets/static/appcenter-marketing/20250923182750061.png)

å¦æä½ çåºç¨éè¦ä¾èµ RabbitMQï¼è¯·å¨ `manifest` ç `install_dep_apps` å­æ®µä¸­æ·»å rabbitmqï¼åºç¨ä¸­å¿å°ç¡®ä¿æ¨çåºç¨å®è£åå¯å¨æ¶ RabbitMQ æå¡å·²å¨è¿è¡ã

**manifest**

```yaml
install_dep_apps=rabbitmq
```

Python ä½¿ç¨ç¤ºä¾

```python
import sys
import time
import uuid
import pika

HOST = "127.0.0.1"
PORT = 5672
VHOST = "/"
USERNAME = "guest"
PASSWORD = "guest"
QUEUE = "ai_rabbitmq_connectivity_test_queue"
TIMEOUT_SECONDS = 8.0

def run_demo() -> int:
    connection = None
    channel = None

    print(f"è¿æ¥: {HOST}:{PORT} vhost='{VHOST}' ç¨æ·='{USERNAME}'")
    try:
        credentials = pika.PlainCredentials(USERNAME, PASSWORD)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=HOST,
            port=PORT,
            virtual_host=VHOST,
            credentials=credentials,
            ssl_options=None,
            connection_attempts=2,
            retry_delay=1.0,
            socket_timeout=max(5.0, TIMEOUT_SECONDS),
            blocked_connection_timeout=max(5.0, TIMEOUT_SECONDS),
            heartbeat=30,
        ))
        channel = connection.channel()

        # å£°ææµè¯éåï¼éæä¹ãèªå¨å é¤ï¼
        channel.queue_declare(queue=QUEUE, durable=False, auto_delete=True)
        print(f"éåå·²å£°æ: {QUEUE}")

        # åéä¸æ¡æµè¯æ¶æ¯
        correlation_id = str(uuid.uuid4())
        body_text = f"rabbitmq demo - {correlation_id}"
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE,
            body=body_text.encode("utf-8"),
            properties=pika.BasicProperties(
                content_type="text/plain",
                delivery_mode=1,
                correlation_id=correlation_id,
            ),
        )
        print("æ¶æ¯å·²åé")

        # ç®åè½®è¯¢æåæ¶æ¯
        deadline = time.monotonic() + TIMEOUT_SECONDS
        while time.monotonic() < deadline:
            method_frame, properties, body = channel.basic_get(queue=QUEUE, auto_ack=True)
            if method_frame:
                got = body.decode("utf-8", errors="replace") if body else ""
                ok = (getattr(properties, "correlation_id", None) == correlation_id) and (got == body_text)
                print("æ¶å°:", got)
                print("æ ¡éª:", "éè¿" if ok else "ä¸å¹é")
                return 0 if ok else 1
            time.sleep(0.2)

        print(f"å¨ {TIMEOUT_SECONDS}s åæªæ¶å°æ¶æ¯", file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover
        print("åçéè¯¯:", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 1
    finally:
        try:
            if channel and channel.is_open:
                try:
                    channel.queue_delete(queue=QUEUE)
                except Exception:
                    pass
        finally:
            if connection and connection.is_open:
                try:
                    connection.close()
                except Exception:
                    pass

if __name__ == "__main__":
    sys.exit(run_demo())
```

## MariaDB

å³å°ä¸çº¿...

---

- Previous: [ð¥ ãè¿é¶ãè¿è¡æ¶ç¯å¢](runtime.md)
- Next: [ð» ãå®æãDocker åºç¨æå»º](docker.md)
