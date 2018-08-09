import time, sys, platform
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

config_broker='broker-service.eu10.cp.iot.sap'

config_credentials_key='D:/Users/avmanoli/Desktop/Device3/credentials.key'
config_credentials_crt='D:/Users/avmanoli/Desktop/Device3/credentials.crt'

config_alternate_id_device='DEVICE ID'
config_alternate_id_capability='ALT CAP ID'
config_alternate_id_sensor='SENSOR'

broker=config_broker
broker_port=8883
s_pctCPU = "66"


my_device=config_alternate_id_device

my_publish_topic='measures/' + my_device

client=mqtt.Client(client_id=my_device)

client.on_connect=on_connect_broker
client.on_subscribe=on_subscribe
#client.on_message=on_message
client.on_publish=on_publish
client.on_log = on_log
client.on_disconnect = on_disconnect

client.tls_set(ca_certs=None ,certfile=config_credentials_crt,  keyfile=config_credentials_key)

client.connect(broker, broker_port, 60)

client.loop_start()

client.subscribe('commands/ca8d0b5736d2e077',0)
time.sleep(5)
##payload = "{ 'capabilityAlternateId': 'input the alternate aid', 'sensorAlternateId': 'input the alternate aid', 'measures': 22 }"
##payload = { 'capabilityAlternateId':'input the alternate aid', 'sensorAlternateId':'input the alternate aid', 'measures':22 }
payload = "{ \"capabilityAlternateId\": \""+config_alternate_id_capability+"\",\"sensorAlternateId\": \""+config_alternate_id_sensor+"\", \"measures\":"+s_pctCPU+"}"
print(payload)
client.publish(my_publish_topic, str(payload), 0)
time.sleep(5)
print('ending')
#client.disconnect()


