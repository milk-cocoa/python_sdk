#!/usr/bin/python
import sys, os
import time

from milkcocoa import milkcocoa

milkcocoaClient = milkcocoa.Milkcocoa.connectWithApiKey("vuei9dh5mu3", "57P5lBcZny6AlQEn", "DM66u0smok1BUjHAZlU9T57kBcQUv5OKIFMkvTQ1", useSSL=False)

datastore = milkcocoaClient.datastore("python")

def on_push(e):
    os._exit(0)

datastore.on("send", on_push)

datastore.send({"content":"Hello"})

time.sleep(1)
time.sleep(1)
time.sleep(1)
print 'error'
os._exit(1)


