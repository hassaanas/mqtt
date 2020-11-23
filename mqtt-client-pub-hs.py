#!/usr/bin/env python
# Usage: mqtt-client-pub-hs.py brokerAddress topicName messageText

import sys
import paho.mqtt.client as mqtt
#broker_address = "192.168.0.108"
broker_address = sys.argv[1]
if broker_address == "default":
	broker_address = "192.168.0.108"
topic = sys.argv[2]
message = sys.argv[3]
#Client(client_id="abc1234", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
client = mqtt.Client()
print("Connecting to Broker: ",broker_address)
client.connect(broker_address)
client.publish(topic,message)
print("Message",message,"published to Topic",topic)