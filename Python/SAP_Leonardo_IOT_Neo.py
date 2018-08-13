import time
import paho.mqtt.client as paho

broker="broker" #Free CloudMQTT account domain
username = "username"      #Username for CloudMQTT Broker
password = "passworx"  #Password for CloudMQTT Broker

#define callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
    ##print(message.topic+" "+str(message.payload))
def on_publish(client, userdata, mid):
    print("Published to client", str(client))
    
client= paho.Client("Not Needed") 

####set username and password from cloudmqtt server

client.username_pw_set(str(username), password= password )

######Bind functions to callback
client.on_message=on_message
client.on_connect=on_connect
client.on_publish=on_publish

#####
print("connecting to broker ",broker)
client.connect(broker, 15673, 60)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("iot/log/iotmmsp349341trial/v1/ENCRYPTEDid")  #subscribe to log
client.subscribe("iot/ack/iotmmsp349341trial/v1/ENCRYPTEDid")  #subscribe to acknowledge
client.subscribe("iot/push/iotmmsp349341trial/v1/ENCRYPTEDid") #subscribe to push
time.sleep(2)
payload = {"mode":"sync","messageType":"MessageType","messages":[{"test":"Testing-Avinash"}]} #Define Payload
print("publishing ")
client.publish("iot/data/iotmmsp349341trial/v1/ENCRYPTEDid", str(payload))#Publish 

time.sleep(4)
print("published successfully")
client.disconnect() #disconnect
client.loop_stop() #stop loop
