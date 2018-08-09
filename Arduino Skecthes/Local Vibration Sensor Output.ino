  
void setup ()

{
  Serial.begin(115200);
  }

void loop (){
 
 float sensorValue = analogRead(17);
    Serial.println("========Avinash loooop==");
    Serial.println(sensorValue); 
    delay(800);
}
