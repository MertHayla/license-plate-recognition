#include <SPI.h>
#include <RFID.h>
#include <Servo.h>
char gelenVeri;
int servoPin = 8;
Servo motor;
RFID lrt720(10, 9);

void setup() {
  Serial.begin(9600);
  SPI.begin();
  lrt720.init();
  motor.attach(servoPin);
  motor.write(0);
  
  
}

void loop() {
  //motor.write(0);
  if(Serial.available()>0)
  {
    gelenVeri = Serial.read();
    if(gelenVeri == '1'){
      motor.write(90);
      }
     else if(gelenVeri =='0'){
      motor.write(0);
      }
     }
 /* if (Serial.available()> 0) {
    char command = Serial.read();
    if (command == '1') {
      motor.write(180);
    }
    if (command =='0'){
      motor.write(0);
      delay(1000);
      }
  }*/
  if (lrt720.isCard()) {
    if (lrt720.readCardSerial()) {
      Serial.println("Kart Bulundu ID: ");
      char cardID[5];
      sprintf(cardID, "%02X%02X%02X%02X%02X", lrt720.serNum[0], lrt720.serNum[1], lrt720.serNum[2], lrt720.serNum[3], lrt720.serNum[4]);
      String cardIDString = String(cardID);
      Serial.println(cardIDString);

      if (strcmp(cardID, "C3964C958C") == 0) {
        motor.write(90);
        Serial.println("ID Doğru");
      } else {
        motor.write(0);
        Serial.println("ID Yanlış");
      }
    }
  }
  lrt720.halt();
}
