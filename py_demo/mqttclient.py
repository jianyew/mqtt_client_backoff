#!/usr/bin/python3

import sys
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
import retry

#Setup our MQTT client and security certificates
#Make sure your certificate names match what you downloaded from AWS IoT

mqttc = AWSIoTMQTTClient("2AF8BC6AD9A2")

#Use the endpoint from the settings page in the IoT console
mqttc.configureEndpoint("a1w6jnzc1m4aj1-ats.iot.ap-southeast-1.amazonaws.com",8883)
mqttc.configureCredentials("AmazonRootCA1.pem","2AF8BC6AD9A2_privateKey.pem","2AF8BC6AD9A2_certificatePem.pem")

#Function to encode a payload into JSON
def json_encode(string):
        return json.dumps(string)

mqttc.json_encode=json_encode

#This sends our test message to the iot topic
@retry(wait_random_min=1000, wait_random_max=2000)
def send(i):
  #Declaring our variables
    message ={
      'thing': "device01",
      'no': i,
      'ct': time.asctime(time.localtime(time.time()) ),
      'message': "Test Message"
    }

    #Encoding into JSON
    message = mqttc.json_encode(message)

    mqttc.publish("999999/2AF8BC6AD9A2/", message, 1)
    
    print ("Message Published " + message)


#Connect to the gateway
mqttc.connect()
print ("Connected")
i=0
#Loop until terminated
while True:
    i = i  +1
    send(i)
    time.sleep(5)
#send(i)
mqttc.disconnect()