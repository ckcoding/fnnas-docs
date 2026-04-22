# ð» ãå®æãDocker åºç¨æå»º

> Source: [https://developer.fnnas.com/docs/core-concepts/docker/](https://developer.fnnas.com/docs/core-concepts/docker/)

## åå»ºåºç¨

ä½¿ç¨ `fnpack create my-app -t docker` å½ä»¤åå»ºåºç¨ç®å½ï¼my-app è¯·èªè¡æ¿æ¢ä¸ºä½ çåºç¨åã
åå»ºåçåºç¨ç®å½ç»æå¦ä¸ï¼

```text
my-app/
âââ app/                            # ðï¸ åºç¨å¯æ§è¡æä»¶ç®å½
â   âââ docker/                     # ðï¸ Docker èµæºç®å½
â   â   âââ docker-compose.yaml     # Docker Compose ç¼ææä»¶
â   âââ ui/                         # ðï¸ åºç¨å¥å£åè§å¾
â   â   âââ images/                 # ðï¸ åºç¨å¾æ åå¾çèµæºç®å½
â   â   âââ config                  # åºç¨å¥å£éç½®æä»¶
âââ manifest                        # åºç¨ååºæ¬ä¿¡æ¯æè¿°æä»¶
âââ cmd/                            # ðï¸ åºç¨çå½å¨æç®¡çèæ¬
â   âââ main                        # åºç¨ä¸»èæ¬ï¼ç¨äºå¯å¨ãåæ­¢ãæ£æ¥åºç¨ç¶æ
â   âââ install_init                # åºç¨å®è£åå§åèæ¬
â   âââ install_callback            # åºç¨å®è£åè°èæ¬
â   âââ uninstall_init              # åºç¨å¸è½½åå§åèæ¬
â   âââ uninstall_callback          # åºç¨å¸è½½åè°èæ¬
â   âââ upgrade_init                # åºç¨æ´æ°åå§åèæ¬
â   âââ upgrade_callback            # åºç¨æ´æ°åè°èæ¬
â   âââ config_init                 # åºç¨éç½®åå§åèæ¬
â   âââ config_callback             # åºç¨éç½®åè°èæ¬
âââ config/                         # ðï¸ åºç¨éç½®ç®å½
â   âââ privilege                   # åºç¨æééç½®
â   âââ resource                    # åºç¨èµæºéç½®
âââ wizard/                         # ðï¸ åºç¨åå¯¼ç®å½
âââ LICENSE                         # åºç¨è®¸å¯è¯æä»¶
âââ ICON.PNG                        # åºç¨å 64*64 å¾æ æä»¶
âââ ICON_256.PNG                    # åºç¨å 256*256 å¾æ æä»¶
```

## 1. ç¼è¾ manifest æä»¶

å®ä¹å¿é¡»å­æ®µï¼

- appname - åºç¨çå¯ä¸æ è¯ç¬¦ï¼å°±åäººçèº«ä»½è¯å·ä¸æ ·ï¼å¨æ´ä¸ªç³»ç»ä¸­å¿é¡»æ¯å¯ä¸ç
- version - åºç¨çæ¬å·ï¼æ ¼å¼ä¸º x[.y[.z]][-build]ï¼ä¾å¦ï¼1.0.0ã2.1.3-beta
- display_name - å¨åºç¨ä¸­å¿ååºç¨è®¾ç½®ä¸­æ¾ç¤ºçåç§°ï¼ç¨æ·çå°çå°±æ¯è¿ä¸ªåå­
- desc - åºç¨çè¯¦ç»ä»ç»ï¼æ¯æ HTML æ ¼å¼ï¼å¯ä»¥åå«é¾æ¥ãå¾çç­

å¶ä»å­æ®µå¯åè [manifestæå](manifest.md) ï¼æéè¿è¡å®ä¹

## 2. ç¼è¾ docker-compose.yaml æä»¶

ç³»ç»å°æ ¹æ® `docker-compose.yaml` åå»ºåå¯å¨å®¹å¨ç¼æãè¯¦ç» compose ä½¿ç¨æ¹æ³å¯ç§»æ­¥ [Docker Compose Quickstart](https://docs.docker.com/compose/gettingstarted/)

`docker-compose.yaml` åè®¸ä½¿ç¨ç¯å¢åéï¼å¨æ§è¡åå°è¿è¡æ¿æ¢ï¼ç¸å³ç¯å¢åéå¯åè [ç¯å¢åéæå](environment-variables.md)

## 3. æ£æ¥åºç¨å¯åç¶æ

é»è®¤æåµä¸ï¼æ éå®ä¹å¯åé»è¾ï¼å ä¸º Docker åºç¨çå¯ååç±åºç¨ä¸­å¿æ§è¡ compose æ¥ç®¡çã

ç¶èï¼ä¾ç¶éè¦å®ä¹ Docker åºç¨æ¯å¦å¨è¿è¡ä¸­ï¼èæ¬ä¸­é»è®¤éæ©ç¬¬ä¸ä¸ªå®¹å¨çç¶æä½ä¸ºåºç¨çå¯åç¶æï¼å¦ä¸ç¬¦åææï¼å¯èªè¡ä¿®æ¹é«äº®é¨åã

**/cmd/main**

```shell
#!/bin/bash

FILE_PATH="${TRIM_APPDEST}/docker/docker-compose.yaml"

is_docker_running () {
    DOCKER_NAME=""

    if [ -f "$FILE_PATH" ]; then
        DOCKER_NAME=$(cat $FILE_PATH | grep "container_name" | awk -F ':' '{print $2}' | xargs)
        echo "DOCKER_NAME is set to: $DOCKER_NAME"
    fi

    if [ -n "$DOCKER_NAME" ]; then
        docker inspect $DOCKER_NAME | grep -q "\"Status\": \"running\"," || exit 1
        return
    fi
}

case $1 in
start)
    # run start command. exit 0 if success, exit 1 if failed
    # do nothing, docker application will be started by appcenter
    exit 0
    ;;
stop)
    # run stop command. exit 0 if success, exit 1 if failed
    # do nothing, docker application will be stopped by appcenter
    exit 0
    ;;
status)
    # check application status command. exit 0 if running, exit 3 if not running
    # check first container by default, you cound modify it by yourself
    if is_docker_running; then
        exit 0
    else
        exit 3
    fi
    ;;
*)
    exit 1
    ;;
esac%
```

## 4. å®ä¹ç¨æ·å¥å£

å³å®ä¹å¨é£ç fnOS ä¸çæ¡é¢å¾æ ï¼è¯¦æå¯åè [ç¨æ·å¥å£æå](app-entry.md)

## 5. æ§è¡æååæµè¯

å¨æ ¹ç®å½ï¼ä½¿ç¨ `fnpack build` å½ä»¤è¿è¡æåï¼è·å¾ `fpk` æä»¶ï¼åè [æµè¯åºç¨æå](../quick-started/test-application.md) è¿è¡å®æºæµè¯

---

- Previous: [ð¥ ãè¿é¶ãä¸­é´ä»¶æå¡](middleware.md)
- Next: [ð» ãå®æãNative åºç¨æå»º](native.md)
