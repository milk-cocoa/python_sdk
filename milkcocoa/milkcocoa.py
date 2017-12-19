from __future__ import print_function
import os
import inspect
import json
import paho.mqtt.client as mqtt
import thread

__all__ = [
    'Milkcocoa', 'DataStore'
]


class Milkcocoa:
    def __init__(self, app_id, username, useSSL=True, blocking=False):
        self.host = "pubsub1.mlkcca.com"
        self.app_id = app_id
        self.username = username
        self.datastores = {}
        self.client = mqtt.Client()
        self.client._strict_protocol = False
        self.client.username_pw_set(self.username, self.app_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.create_thread_for_message
        # self.client.on_subscribe = self.on_subscribe
        # self.client.on_log = self.on_log
        port = 1883
        if useSSL:
            port = 8883
            ca_cert = os.path.realpath(os.path.abspath(
                os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "../ca.cert")))
            self.client.tls_set(ca_cert)
        self.client.connect(self.host, port, 36)
        if not blocking:
            self.client.loop_start()

    def loop_forever(self):
        self.client.loop_forever()

    def on_connect(self, mqttc, client, userdata, rc):
        print("Connected with result code " + str(rc))

    def create_thread_for_message(self,mqttc,obj, msg):
        thread.start_new_thread(self.on_message,(mqttc,obj,msg))

    def on_message(self, mqttc, obj, msg):
        topic_arr = msg.topic.split("/")
        topic_arr.pop(0)
        event = topic_arr.pop()
        self.datastores["/".join(topic_arr)].fire(event, str(msg.payload))
        
    def on_subscribe(self, client, userdata, mid, granted_qos):
        print(granted_qos)

    def on_log(self, client, userdata, level, buf):
        print(buf)

    def datastore(self, path):
        self.datastores[path] = DataStore(self, path)
        return self.datastores[path]

    @staticmethod
    def connect(app_id, key, useSSL=True, blocking=False):
        return Milkcocoa(app_id, "k" + key, useSSL=useSSL, blocking=blocking)


class DataStore:
    def __init__(self, milkcocoa, path):
        self.milkcocoa = milkcocoa
        self.client = milkcocoa.client
        self.path = path

    def push(self, data_element):
        self.client.publish(self.milkcocoa.app_id + "/" + self.path + "/push", json.dumps({'params': data_element}))

    def send(self, data_element):
        self.client.publish(self.milkcocoa.app_id + "/" + self.path + "/send", json.dumps({'params': data_element}))

    def on(self, event, cb):

        self.client.subscribe(self.milkcocoa.app_id + "/" + self.path + "/_" + event[0], 0)
        if event == "push":
            self.on_push = cb
        elif event == "send":
            self.on_send = cb

    def fire(self, event, payload):
        value = json.loads(payload)["params"]
        if event == "_p":
            self.on_push({"value": value})
        elif event == "_s":
            self.on_send({"value": value})
