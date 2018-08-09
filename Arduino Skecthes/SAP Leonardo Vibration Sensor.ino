//working Version 1 dyanamic

#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <Wire.h>

//const int SENSOR_PIN = 17;   

//float sensorValue = analogRead(17);

// ========== start configuration ==========
// WiFi configuration
const char* ssid = "Manoli";
const char* password = "password";
  
// SAP HCP specific configuration
const char* host = "iotmmsp*****.hanatrial.ondemand.com";
String device_id = "device Id";
String message_type_id = "message ID";
String oauth_token= "o_Auth Token";
 
const int httpsPort = 443; //HTTP port

// ========== end configuration ============

void setup() {
  delay(2000);
  Serial.begin(115200);
  Serial.println("Vibration Data \n\n");
  //Wire.begin(9);
  Serial.print("connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
}

void loop() {
  float sensorValue = analogRead(17);
    Serial.println("========Avinash loooop==");
    Serial.println(sensorValue); 
    delay(800);
 
  String url = "https://iotmmsp****ial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/" + device_id;
  String post_payload = "{\"mode\":\"async\", \"messageType\":\"" + message_type_id + "\", \"messages\":[{\"sensorValue\":"+sensorValue+"}]}";

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
