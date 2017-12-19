#!/usr/bin/python
import sys, os
import time

from milkcocoa import milkcocoa

milkcocoaClient = milkcocoa.Milkcocoa.connect('BJBop-Szz','QvXkGBVhDx8Mzj7G-BTH5Sv9Lo0iPv6ED1zYzKHU')

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


