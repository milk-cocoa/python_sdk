# python_sdk
Milkcocoa python sdk


# Status

[![Circle CI](https://circleci.com/gh/milk-cocoa/python_sdk.svg?style=svg)](https://circleci.com/gh/milk-cocoa/python_sdk)

# How To Use

```
import sys
import time

import milkcocoa.milkcocoa as milkcocoa

#milkcocoaClient = milkcocoa.Milkcocoa.connect("{your-app-id}", "{{your-api-key}}")

datastore = milkcocoaClient.datastore("python")

def on_push(e):
	print e

datastore.on("push", on_push)

datastore.push({"content":"Hello"})

while(True):
	time.sleep(1)
```

### コントリビューター募集中

Milkcocoa Python SDKのコントリビューターになって頂ける方を募集しています。
興味がある方は、以下のメールアドレスにお気軽に連絡下さい。

contact@mlkcca.com
