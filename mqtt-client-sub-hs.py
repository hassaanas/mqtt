#!/usr/bin/env python
# Usage: mqtt-client-sub-hs.py brokerAddress topicName

import sys
import time
import paho.mqtt.client as mqtt
#broker_address = "192.168.0.108"
broker_address = sys.argv[1]
if broker_address == "default":
	broker_address = "192.168.0.108"
topic = sys.argv[2]
#qos = 0
#########################################
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain,'\n')
#########################################

#Client(client_id="abc1234", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
client = mqtt.Client(client_id="abc1234", clean_session=True, userdata=None, transport="tcp")
print("Connecting to Broker: ",broker_address)
client.on_message = on_message
client.connect(broker_address)

client.loop_start() #start the loop
print("Subscribing to topic",topic)
client.subscribe(topic)
print("Waiting for messages")
#client.publish(topic,"message11111")
time.sleep(400) # wait
client.loop_stop() #stop the loop
