import os
import inspect
import json
import paho.mqtt.client as mqtt

class Milkcocoa:
	def __init__(self, app_id, username):
		self.host = app_id + ".mlkcca.com"
		self.app_id = app_id;
		self.username = username;
		self.datastores = {}
		self.client = mqtt.Client()
		self.client.username_pw_set(self.username, self.app_id)
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message
		ca_cert = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../../ca.cert")))
		self.client.tls_set(ca_cert)
		self.client.connect(self.host, 8883, 36)
		self.client.loop_start()

	def on_connect(self, mqttc, client, userdata, rc):
		print("Connected with result code "+str(rc))
	
	def on_message(self, mqttc, obj, msg):
		topic_arr = msg.topic.split("/")
		topic_arr.pop(0)
		event = topic_arr.pop()
		self.datastores["/".join(topic_arr)].fire(event, str(msg.payload))
	
	def datastore(self, path):
		self.datastores[path] = DataStore(self, path)
		return self.datastores[path]

	@staticmethod
	def connect(app_id):
		return Milkcocoa(app_id, "sdammy")

	@staticmethod
	def connectWithApiKey(app_id, key, secret):
		return Milkcocoa(app_id, "k"+key+":"+secret)

class DataStore:
	def __init__(self, milkcocoa, path):
		self.milkcocoa = milkcocoa
		self.client = milkcocoa.client
		self.path = path

	def push(self, data_element):
		self.client.publish(self.milkcocoa.app_id + "/" + self.path + "/push", json.dumps({'params':data_element}));

	def send(self, data_element):
		self.client.publish(self.milkcocoa.app_id + "/" + self.path + "/send", json.dumps({'params':data_element}));
	
	def on(self, event, cb):
		self.client.subscribe(self.milkcocoa.app_id + "/" + self.path + "/" + event, 0)
		if event == "push":
			self.on_push = cb
		elif event == "send":
			self.on_send = cb

	def fire(self, event, payload):
		value = json.loads(payload)["params"]
		if event == "push":
			self.on_push({"value":value})
		elif event == "send":
			self.on_send({"value":value})
