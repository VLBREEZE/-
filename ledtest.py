#include <Wire.h>

int LED = 7;
int ledState = 0;
const int Address = 0x50;

void setup()
{
  Serial.begin(9600);
  Wire.begin(Address);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(sendData);
  
  pinMode(LED, OUTPUT);
}

void receiveEvent(int bytes) {
  ledState = Wire.read();
  Serial.print("Receive Data : ");
  Serial.println(ledState);
}

void loop()
{
  if(ledState > 125) {
    digitalWrite(LED, HIGH);
  }
  else {
    digitalWrite(LED, LOW);
  }
}

void sendData(){
    Wire.write(ledState);
}
