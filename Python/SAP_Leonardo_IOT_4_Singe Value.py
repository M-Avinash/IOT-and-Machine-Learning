import time, sys, platform
import json
import base64
import time

import paho.mqtt.client as mqtt

# ========================================================================

def on_connect_broker(client, userdata, flags, rc):
       print('Connected to MQTT broker with result code: ' + str(rc))
        
def on_subscribe(client, obj, message_id, granted_qos):
	print('on_subscribe - message_id: ' + str(message_id) + ' / qos: ' + str(granted_qos))

def on_message(client, userdata, message):
       print("received message =",str(message.payload.decode("utf-8")))

def on_publish(client, userdata, mid):
    print("Published to client", str(client)+ '\nMid value received is :' , str(mid))

def on_log(client, userdata, level, buf):
    print('\nbuffer output :', str(buf))

def on_disconnect(client, userdata, rc):
    print("client disconnected with result code :", str(rc))
    
# ========================================================================

config_broker='ENTER BROKER DETAILS'

config_credentials_key='D:/FD4/NewDeviceCerts/credentials.key'
config_credentials_crt='D:/FD4/NewDeviceCerts/credentials.crt'

broker=config_broker
broker_port=8883

client=mqtt.Client(client_id="ENTER CLIENT ID")

client.on_connect=on_connect_broker
client.on_subscribe=on_subscribe
client.on_message=on_message
client.on_publish=on_publish
client.on_log = on_log
client.on_disconnect = on_disconnect

client.tls_set(ca_certs=None ,certfile=config_credentials_crt,  keyfile=config_credentials_key)

client.connect(broker, broker_port, 60)

client.loop_start()

client.subscribe("commands/162af764537c699b",0)
time.sleep(5)
payload = { "capabilityAlternateId": "d34f54bda8d40721", "sensorAlternateId": "918dd8b354dbde8e", "measures": [["22"]] } 
client.publish("measures/163b8dd6c89384f5", str(payload), 0)
time.sleep(5)
#client.disconnect()


