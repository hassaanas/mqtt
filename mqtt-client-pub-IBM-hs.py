#!/usr/bin/env python
# Usage: mqtt-client-pub-hs.py brokerAddress topicName messageText

import sys, time, json
import paho.mqtt.client as mqtt


broker_address = sys.argv[1]
if broker_address == "ibm":
	broker_address = "5yalfo.messaging.internetofthings.ibmcloud.com"
payloadType = sys.argv[2]
#topic = "iot-2/type/test/id/4321/evt/status/fmt/" + payloadType # For IBM Apps, Event topic format: iot-2/evt/_eventid/fmt/_formatstring
topic = "iot-2/evt/status/fmt/" + payloadType # For IBM Devices, Event topic format: iot-2/evt/_eventid/fmt/_formatstring
message = sys.argv[3]

# ---------- IBM IoT API Parameters ------------ #
port = 8883 # -p
cafile = "C:\\Users\\eisahds\\Documents\\Hassaan\\project-mqtt\\messaging.pem"
#userName = "a-5yalfo-sfeu7mrh3t" # -u : username. For IBM Apps, API key goes here.
userName = "use-token-auth" # -u : username. For IBM Devices, use use-token-auth.
password = "K9XA*VbrEx&kV1YxTJ" # -P : provide a password. For IBM, Authentication Token goes here.
userID = "d:5yalfo:Hassaan-Laptop:laptop-hs-1" # Device ID: d:_orgid:_devicetype:_deviceid
# -----------------------------------------------#

def on_connect(client, userdata, flags, rc):
	if rc==0:
		print("Connection successful.")
	else:
		print("Connection failed with return code = ",rc)


#Client(client_id="abc1234", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
client = mqtt.Client(client_id=userID, clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.tls_set(ca_certs=None, certfile=None, keyfile=cafile, ciphers=None)
client.username_pw_set(userName, password=password)
#client.user_data_set(userID)

client.on_connect=on_connect
print("Connecting to Broker: ",broker_address,"on port:",port)
client.connect(broker_address,port)
client.loop_start()  #Start loop 
time.sleep(4) # Wait for connection setup to complete
#client.publish(topic,message)
client.publish(topic, json.dumps(message))
print("Message '",message,"'","published to Topic '",topic,"'")
client.disconnect()