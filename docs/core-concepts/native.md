# ð» ãå®æãNative åºç¨æå»º

> Source: [https://developer.fnnas.com/docs/core-concepts/native/](https://developer.fnnas.com/docs/core-concepts/native/)

## ä¸ä¸ªç®åç Notepad åºç¨

> [!TIP]
> ç¤ºä¾ä»£ç å¯ä»¥ç¹å» [æ­¤å¤](https://static.fnnas.com/appcenter-marketing/20250917183504284.zip) ä¸è½½

æä»¬ä½¿ç¨ Vide Coding å®ç°äºä¸ä¸ªç®æç Notepad ç¨åºï¼å®æ¯æå¨æå¡ç«¯ä¿å­ç¬è®°åå®¹ï¼å¨æµè§å¨ä¸­è¿è¡æ¥çåç¼è¾ã

ç¸å³ææ¯æ å¦ä¸ï¼

- åç«¯ä½¿ç¨ NodeJS + express å¼å
- åç«¯ä½¿ç¨ React + vite å¼å

ä¸è½½è§£ååï¼å¯ä»¥çå°ä»£ç ç®å½ç»æå¦ä¸ï¼

```text
notepad/
âââ backend/
â   âââ server.js
â   âââ package.json
âââ frontend/
â   âââ public/
â   â   âââ styles.css
â   âââ src/
â   â   âââ main.jsx
â   âââ index.html
â   âââ package.json
â   âââ vite.config.mjs
âââ scripts/
â   âââ build-combined.js
âââ package-lock.json
âââ package.json
âââ README.md
```

è¯·èªè¡åå¤å¥½ NodeJS ç¯å¢ï¼ç¶åå¨ç»ç«¯æ§è¡å¦ä¸å½ä»¤ï¼ä»¥å®ææ¬å°è¿è¡

```shell
npm install --workspaces
npm run start
```

ä¸åé¡ºå©çè¯ï¼ä½ å·²ç»å¯ä»¥å¨æµè§å¨è®¿é® [http://localhost:5001](http://localhost:5001) æ¥ä½éªè¯¥åºç¨äº

ä¸ºäºå¨é£ç fnOS ä¸è¿è¡ï¼æä»¬è¿éè¦å°åºç¨çåç«¯ååç«¯éè¿ä»¥ä¸å½ä»¤è¿è¡æåï¼å®æåï¼ä½ å°±è½å¨ `dist/` çå°æç»çå¯æ§è¡æä»¶äº

```shell
npm run build
```

æ¥ä¸æ¥ï¼æä»¬éè¦å°è¿è¡åºç¨æå

## åå»ºé£ç fnOS åºç¨æåç®å½

å¨ `notepad/` ç®å½ä¸æ§è¡ `fnpack create fnnas.notepad` å½ä»¤åå»ºåºç¨æåç®å½ï¼è¿æ¶åçç®å½ç»æåºè¯¥å¦ä¸ï¼

```text
notepad/
âââ backend/
âââ dist/
â   âââ node_modules/
â   âââ public/
â   â   âââ assets/
â   â   âââ index.html
â   â   âââ styles.css
â   âââ server.js
â   âââ package.json
â   âââ package-lock.json
âââ fnnas.notepad/
â   âââ app/
â   âââ manifest
â   âââ cmd/
â   â   âââ main
â   â   âââ install_init
â   â   âââ install_callback
â   â   âââ uninstall_init
â   â   âââ uninstall_callback
â   â   âââ upgrade_init
â   â   âââ upgrade_callback
â   â   âââ config_init
â   â   âââ config_callback
â   âââ config/
â   â   âââ privilege
â   â   âââ resource
â   âââ wizard/
â   âââ LICENSE
â   âââ ICON.PNG
â   âââ ICON_256.PNG
âââ frontend/
âââ scripts/
âââ package-lock.json
âââ package.json
âââ README.md
```

### å¤å¶ç¼è¯äº§ç©

`notepad/fnnas.notepad/app/` ç®å½ç¨æ¥å­æ¾åºç¨çå¨é¨å¯æ§è¡æä»¶åä¾èµã

å¨ `notepad/fnnas.notepad/app/` ç®å½ä¸åå»º `server/`ï¼å¹¶å¤å¶ `notepad/dist/` ç®å½ä¸çå¨é¨åå®¹å° `server/` ç®å½ä¸

### ç¼è¾åºç¨åºæ¬ä¿¡æ¯

**notepad/fnnas.notepad/manifest**

```yaml
appname=fnnas.notepad
version=0.0.1
desc=A simple notepad
arch=x86_64
display_name=Notepad
maintainer=someone
distributor=someone
desktop_uidir=ui
desktop_applaunchname=fnnas.notepad.Application
source=thirdparty
```

### ç¼è¾åºç¨æé

å®ä¹åºç¨è¿è¡çæéï¼åºç¨å°ä»¥ `fnnas.notepad` ç¨æ·èº«ä»½è¿è¡

**notepad/fnnas.notepad/config/privilege**

```json
{
    "defaults": {
        "run-as": "package"
    },
    "username": "fnnas.notepad",
    "groupname": "fnnas.notepad"
}
```

### ç¼è¾åºç¨éç½®

æä»¬å¸æå°ç¬è®°åå®¹æ¾å¨ç¨æ·å¯ä»¥æ¥çåç¼è¾çå±äº«ç®å½ï¼æä»¥å®ä¹data-shareå±æ§ï¼å¦ä¸ï¼

**notepad/fnnas.notepad/config/resource**

```json
{
    "data-share": {
        "shares": [
            {
                "name": "fnnas.notepad",
                "permission": {
                    "rw": [
                        "fnnas.notepad"
                    ]
                }
            }
        ]
    }
}
```

### ç¼è¾åºç¨å¯åèæ¬

å®ä¹åºç¨çå¯å¨ååæ­¢é»è¾

**notepad/fnnas.notepad/cmd/main**

```bash
#!/bin/bash

LOG_FILE="${TRIM_PKGVAR}/info.log"
PID_FILE="${TRIM_PKGVAR}/app.pid"

export PATH=/var/apps/nodejs_v22/target/bin:$PATH
# data directory to write note.txt
DATA_DIR="${TRIM_DATA_SHARE_PATHS%%:*}"
# write the command to start your program here
CMD="DATA_DIR=${DATA_DIR} PORT=5001 node ${TRIM_APPDEST}/server/server.js"

log_msg() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> ${LOG_FILE}
}

start_process() {
    if status; then
        return 0
    fi

    log_msg "Starting process ..."
    # env >> ${LOG_FILE}
    # run the nodejs process
    bash -c "${CMD}" >> ${LOG_FILE} 2>&1 &
    # write pid to pidfile
    printf "%s" "$!" > ${PID_FILE}
    # log_msg "${CMD}"
    # log_msg "pid = $!"
    return 0
}

stop_process() {
    log_msg "Stopping process ..."

    if [ -r "${PID_FILE}" ]; then
        pid=$(head -n 1 "${PID_FILE}" | tr -d '[:space:]')

        log_msg "pid=${pid}"
        if ! check_process "${pid}"; then
            # process not exist, delete pidfile
            rm -f "${PID_FILE}"
            log_msg "remove pid file 1"
            return
        fi

        log_msg "send TERM signal to PID:${pid}..."
        kill -TERM ${pid} >> ${LOG_FILE} 2>&1

        local count=0
        while check_process "${pid}" && [ $count -lt 10 ]; do
            sleep 1
            count=$((count + 1))
            log_msg "waiting process terminal... (${count}s/10s)"
        done

        if check_process "${pid}"; then
            log_msg "send KILL signal to PID:${pid}..."
            kill -KILL "${pid}"
            sleep 1
            rm -f "${PID_FILE}"
        else
            log_msg "process killed... "
        fi
    fi

    return 0
}

check_process() {
    local pid=$1
    if kill -0 "${pid}" 2>/dev/null; then
        return 0  # process exist
    else
        return 1  # process not exist
    fi
}

status() {
    if [ -f "${PID_FILE}" ]; then
        pid=$(head -n 1 "${PID_FILE}" | tr -d '[:space:]')
        if check_process "${pid}"; then
            return 0
        else
            # Process is not running but pidfile exists - clean it up
            rm -f "${PID_FILE}"
        fi
    fi

    return 1
}

case $1 in
start)
    # run start command. exit 0 if success, exit 1 if failed
    start_process
    ;;
stop)
    # run stop command. exit 0 if success, exit 1 if failed
    stop_process
    ;;
status)
    # check application status command. exit 0 if running, exit 3 if not running
    if status; then
        exit 0
    else
        exit 3
    fi
    ;;
*)
    exit 1
    ;;
esac
```

### ç¼è¾æ¡é¢å¾æ 

```text
notepad/
âââ backend/
âââ dist/
âââ fnnas.notepad/
â   âââ app/
â   â   âââ server/
â   â   âââ ui
â   â       âââ images
â   â       â   âââ icon_64.png
â   â       â   âââ icon_256.png
â   â       âââ config
â   âââ manifest
â   âââ cmd/
â   âââ config/
â   âââ wizard/
â   âââ LICENSE
â   âââ ICON.PNG
â   âââ ICON_256.PNG
âââ frontend/
âââ scripts/
âââ package-lock.json
âââ package.json
âââ README.md
```

configæä»¶è¯´æï¼

**notepad/fnnas.notepad/app/ui/config**

```json
{
    ".url": {
        "fnnas.notepad.Application": {
            "title": "Notepad",
            "icon": "images/icon_{0}.png",
            "type": "url",
            "protocol": "http",
            "port": "5001"
        }
    }
}
```

æ°å¢ä¸¤ä¸ªå¾æ æä»¶ï¼åè¾¨çåå«æ¯ 64x64 å 256x256ã

## æåæ fpk

ä½¿ç¨ `fnpack` CLI å·¥å·æååºç¨

```bash
cd fnnas.notepad
fnpack build
```

ç¶åä½ å¯ä»¥å¨ `fnnas.notepad` ç®å½ä¸çå° `fnnas.notepad.fpk` æä»¶ï¼æ¥ä¸æ¥ä½ å°±å¯ä»¥å°é£ç fnOS ä¸æµè¯åºç¨äº

### éæç¼è¾

å¦ææä»¬å¸ææ¯æ¬¡ `npm run build` ç¼è¯é¡¹ç®æ¶ï¼é½èªå¨åå»º `fpk` æä»¶ï¼åå¯ä»¥å¨ç¼è¯èæ¬ä¸­è¡¥å `fnpack build` é»è¾ã

å¨æ¬é¡¹ç®ä¸­ï¼å¯ä»¥å¨ `notepad/scripts/build-combined.js` çæåè¡¥å `fnpack build` é»è¾ï¼å¦ä¸æç¤º:

```javascript
const packDir = path.join(root, 'fnnas.notepad')
const packServerDir = path.join(packDir, 'app', 'server');
run(`rm -rf ${packServerDir}`)
run(`mkdir ${packServerDir}`)
run(`cp -r ${outDir}/* ${packServerDir}/`)
run(`fnpack build -d ${packDir}`)
```

---

- Previous: [ð» ãå®æãDocker åºç¨æå»º](docker.md)
- Next: [ð ãè§èãå¾æ  Icon](icon.md)
