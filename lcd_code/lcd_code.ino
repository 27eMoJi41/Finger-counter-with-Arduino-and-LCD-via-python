#include <Bonezegei_LCD1602_I2C.h>

Bonezegei_LCD1602_I2C lcd(0x3F);

void setup() {
  Serial.begin(9600);
  lcd.begin();
}

void loop() {
  while(1){
    if(Serial.available()>0){
      String msg = Serial.readString();
      lcd.setPosition(0,0);
      lcd.print("Number:");
      lcd.setPosition(7,0);
      lcd.print(msg.c_str());
      lcd.clear();
  }
    else{
      lcd.setPosition(0,0);
      lcd.print("No entry");
      lcd.clear();
    }
  }
}
