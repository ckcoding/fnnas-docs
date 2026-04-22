# ð¥ ãè¿é¶ãè¿è¡æ¶ç¯å¢

> Source: [https://developer.fnnas.com/docs/core-concepts/runtime/](https://developer.fnnas.com/docs/core-concepts/runtime/)

## Python ç¯å¢

![](../../assets/static/appcenter-marketing/20250916211501441.png)

éè¿ `manifest` å£°æåºç¨ä¾èµæå®çæ¬ç Python åºç¨ï¼åºç¨ä¸­å¿å°ç¡®ä¿æ¨çåºç¨å®è£åå¯å¨æ¶æå®ç Python ç¯å¢å·²å®è£ã

**manifest**

```yaml
install_dep_apps=python312
```

å¨ `cmd` ç¸å³èæ¬æ§è¡ python å½ä»¤åï¼éé¢åéç½®ç¯å¢ï¼å°ç®æ çæ¬ç bin è·¯å¾ç½®äº PATH ç¯å¢åéæåç«¯ï¼ä»¥ç¡®ä¿å½åå½ä»¤è¡ä¼è¯è½æ­£ç¡®è°ç¨æå®çæ¬ç python å pip ç­å½ä»¤ãå¨æ­¤åºç¡ä¸ï¼ä½¿ç¨ Python åç½®ç venv æ¨¡åä¸ºæ¯ä¸ªé¡¹ç®åå»ºç¬ç«çèæç¯å¢ï¼ä»¥éç¦»é¡¹ç®ä¾èµï¼é¿åçæ¬å²çªã

```shell
# å¯éçæ¬ï¼python312ãpython311ãpython310ãpython39ãpython38
export PATH=/var/apps/python312/target/bin:$PATH

# åå»ºèæç¯å¢
python3 -m venv .venv

# æ¿æ´»èæç¯å¢
source .venv/bin/activate

# å®è£ python ç¸å³ä¾èµå° .venv
pip install -r requirements.txt
```

## Node.js ç¯å¢

![](../../assets/static/appcenter-marketing/20250916211008763.png)

éè¿ `manifest` å£°æåºç¨ä¾èµæå®çæ¬ç Node.js åºç¨ï¼åºç¨ä¸­å¿å°ç¡®ä¿æ¨çåºç¨å®è£åå¯å¨æ¶æå®ç Node.js ç¯å¢å·²å®è£ã

**manifest**

```yaml
install_dep_apps=nodejs_v22
```

å¨ `cmd` ç¸å³èæ¬æ§è¡åï¼éé¢åéç½®ç¯å¢ï¼å°ç®æ çæ¬ç bin è·¯å¾ç½®äº PATH ç¯å¢åéæåç«¯ï¼ä»¥ç¡®ä¿å½åå½ä»¤è¡ä¼è¯è½æ­£ç¡®è°ç¨æå®çæ¬ç node å npm ç­å½ä»¤ã

```shell
# å¯éçæ¬ï¼nodejs_v22ãnodejs_v20ãnodejs_v18ãnodejs_v16ãnodejs_v14
export PATH=/var/apps/nodejs_v22/target/bin:$PATH

# ç¡®è®¤nodeççæ¬
node -v

# ç¡®è®¤npmççæ¬
npm -v
```

## Java ç¯å¢

![](../../assets/static/appcenter-marketing/20250919153027253.png)

éè¿ `manifest` å£°æåºç¨ä¾èµæå®çæ¬ç Java åºç¨ï¼åºç¨ä¸­å¿å°ç¡®ä¿æ¨çåºç¨å®è£åå¯å¨æ¶æå®ç Java ç¯å¢å·²å®è£ã

**manifest**

```yaml
install_dep_apps=java-21-openjdk
```

å¨ `cmd` ç¸å³èæ¬æ§è¡åï¼éé¢åéç½®ç¯å¢ï¼å°ç®æ çæ¬ç bin è·¯å¾ç½®äº PATH ç¯å¢åéæåç«¯ï¼ä»¥ç¡®ä¿å½åå½ä»¤è¡ä¼è¯è½æ­£ç¡®è°ç¨æå®çæ¬ç java ç­å½ä»¤ã

```shell
# å¯éçæ¬ï¼java-21-openjdkãjava-17-openjdkãjava-11-openjdk
export PATH=/var/apps/java-21-openjdk/target/bin:$PATH

# ç¡®è®¤javaççæ¬
java --version
```

---

- Previous: [ð¥ ãè¿é¶ãåºç¨ä¾èµå³ç³»](dependency.md)
- Next: [ð¥ ãè¿é¶ãä¸­é´ä»¶æå¡](middleware.md)
