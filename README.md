# python_sdk
Milkcocoa python sdk


# Status

[![Circle CI](https://circleci.com/gh/milk-cocoa/python_sdk.svg?style=svg)](https://circleci.com/gh/milk-cocoa/python_sdk)

# How To Use

```
import sys
import time

import milkcocoa.milkcocoa as milkcocoa

#milkcocoaClient = milkcocoa.Milkcocoa.connectWithApiKey("{your-app-id}", "57P5lBcZny6AlQEn", "DM66u0smok1BUjHAZlU9T57kBcQUv5OKIFMkvTQ1")
milkcocoaClient = milkcocoa.Milkcocoa.connect("{your-app-id}");

datastore = milkcocoaClient.datastore("python")

def on_push(e):
	print e

datastore.on("push", on_push)

datastore.push({"content":"Hello"})

while(True):
	time.sleep(1)
```