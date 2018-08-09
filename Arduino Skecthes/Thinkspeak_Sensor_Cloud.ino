
#include <ESP8266WiFi.h>
 
String apiKey = "5A1P5IRBTIXE12J3";          //  Enter your Write API key from ThingSpeak

const char *ssid =  "epgp09";               // replace with your wifi ssid and wpa2 key
const char *pass =  "123456789";
const char* server = "api.thingspeak.com";
const float sensorValue = A0;                // Vibration Sensor OUTPUT

WiFiClient client;
 
void setup() 
{
       Serial.begin(9600);
       Serial.println("Connecting to ");
       Serial.println(ssid);
 
       WiFi.begin(ssid, pass);
 
      while (WiFi.status() != WL_CONNECTED) 
     {
            delay(500);
            Serial.print(".");
     }
      Serial.println("");
      Serial.println("WiFi connected");
 
}
 
void loop() 
{


// Read Sensor ADC value in, and convert it to a voltage
  float sensorValue = analogRead(A0);
  Serial.println(sensorValue); // Print the voltage.
  
  if (client.connect(server,80))   //   "184.106.153.149" or api.thingspeak.com
                      {  
                            
                             String postStr = apiKey;
                             postStr +="&field1=";
                             postStr += String(sensorValue);
                             postStr += "\r\n\r\n";
 
                             client.print("POST /update HTTP/1.1\n");
                             client.print("Host: api.thingspeak.com\n");
                             client.print("Connection: close\n");
                             client.print("X-THINGSPEAKAPIKEY: "+apiKey+"\n");
                             client.print("Content-Type: application/x-www-form-urlencoded\n");
                             client.print("Content-Length: ");
                             client.print(postStr.length());
                             client.print("\n\n");
                             client.print(postStr);
                             Serial.print(postStr);
   
                        }
       Serial.println("Waiting...");
  
    //thingspeak needs minimum 15 sec delay between updates
    delay(15000);
}
 

