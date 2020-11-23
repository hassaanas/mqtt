#!/usr/bin/env python
# Usage: mqtt-client-sub-hs.py brokerAddress topicName

import sys
import time
import paho.mqtt.client as mqtt

broker_address = sys.argv[1]
if broker_address == "ibm":
	broker_address = "5yalfo.messaging.internetofthings.ibmcloud.com"
payloadType = sys.argv[2]
#topic = "iot-2/type/test/id/4321/evt/status/fmt/" + payloadType
topic = "iot-2/evt/status/fmt/" + payloadType # For IBM Devices, Event topic format: iot-2/evt/_eventid/fmt/_formatstring
#qos = 0

# ---------- IBM IoT API Parameters ------------ #
port = 8883 # -p
cafile = "C:\\Users\\eisahds\\Documents\\Hassaan\\project-mqtt\\messaging.pem"
userName = "a-5yalfo-sfeu7mrh3t" # -u : username. For IBM, API key goes here.
password = "K9XA*VbrEx&kV1YxTJ" # -P : provide a password. For IBM, Authentication Token goes here.
userID = "a:5yalfo:test2" # -i : id to use for this client.
# -----------------------------------------------#

# ----------------- Functions ------------------ #
def on_connect(client, userdata, flags, rc):
	if rc==0:
		print("Connection successful.")
	else:
		print("Connection failed with return code = ",rc)

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain,'\n')
# -----------------------------------------------#

client = mqtt.Client(client_id=userID, clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.tls_set(ca_certs=None, certfile=None, keyfile=cafile, ciphers=None)
client.username_pw_set(userName, password=password)

print("Connecting to Broker: '",broker_address,"' at Port: '",port,"'")
client.on_connect=on_connect
client.on_message = on_message
client.connect(broker_address,port)
client.loop_start() #start the loop
time.sleep(4) # Wait for connection setup to complete
print("Subscribing to topic '",topic,"'")
client.subscribe(topic)
print("Waiting for messages")
time.sleep(400) # wait
client.loop_stop() #stop the loop
