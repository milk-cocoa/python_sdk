#!/usr/bin/python
import sys, os
import time

try:
    import milkcocoa.milkcocoa as milkcocoa
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import milkcocoa.milkcocoa as milkcocoa

#milkcocoaClient = milkcocoa.Milkcocoa.connectWithApiKey("vuei9dh5mu3", "57P5lBcZny6AlQEn", "DM66u0smok1BUjHAZlU9T57kBcQUv5OKIFMkvTQ1", useSSL=False)
milkcocoaClient = milkcocoa.Milkcocoa.connect("vuei9dh5mu3", useSSL=True, blocking=False);

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


