//working Version 1 dyanamic

#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <Wire.h>
#include "DHT.h"        // including the library of DHT11 temperature and humidity sensor
#define DHTTYPE DHT11   // DHT 11

#define dht_dpin 0
DHT dht(dht_dpin, DHTTYPE); 

// ========== start configuration ==========
// WiFi configuration
const char* ssid = "Manoli";
const char* password = "password";
  
// SAP HCP specific configuration
const char* host = "iotmmsp349341trial.hanatrial.ondemand.com";
String device_id = "7ffce84f-1c2a-4438-9fcb-0e878b34c077";
String message_type_id = "3091f47bb387224fbbdb";
String oauth_token="3ac8f51748eef35195e0ed36d9d797a9";
 
  
 

const int httpsPort = 443; //HTTP port

// ========== end configuration ============



 

void setup() {
  delay(2000);
  dht.begin();
  Serial.begin(115200);
  Serial.println("Humidity and temperature\n\n");
  Serial.println();
  Wire.begin(9);
  Serial.print("connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
}




void loop() {
  Serial.println("========Avinash====loooop==");
 
  float sensor1 = dht.readHumidity();
    float sensor2 = dht.readTemperature();         
    Serial.print("Current humidity = ");
    Serial.print(sensor1);
    Serial.print("%  ");
    Serial.print("temperature = ");
    Serial.print(sensor2); 
    Serial.println("C  ");
  delay(800);
 
  String url = "https://iotmmsp349341trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/" + device_id;
  String post_payload = "{\"mode\":\"async\", \"messageType\":\"" + message_type_id + "\", \"messages\":[{\"sensor1\":"+sensor1+", \"sensor2\":"+sensor2+"}]}";

  // Use WiFiClientSecure class to create TLS connection
  WiFiClientSecure client;
  Serial.print("connecting to ");
  Serial.println(host);
  if (!client.connect(host, httpsPort)) {
    Serial.println("connection failed");
    return;
  }

  
  Serial.print("requesting URL: ");
  Serial.println(url);
  
  // using HTTP/1.0 enforces a non-chunked response
  client.print(String("POST ") + url + " HTTP/1.0\r\n" +
               "Host: " + host + "\r\n" +
               "Content-Type: application/json;charset=utf-8\r\n" +
               "Authorization: Bearer " + oauth_token + "\r\n" +
               "Content-Length: " + post_payload.length() + "\r\n\r\n" +
               post_payload + "\r\n\r\n");

  delay(1500);
  Serial.println("request sent");
  Serial.println("reply was:");
  Serial.println(">>>>>>>>>>");
  delay(1000);
  while (client.connected()) {
    String line = client.readStringUntil('\n');
    Serial.println(line);
  }
  Serial.println(">>>>>>>>>>");
  Serial.println("Closing connection");
 
}
