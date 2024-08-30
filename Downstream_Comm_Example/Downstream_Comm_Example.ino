

void setup() {
  // Setup serial for monitor and Setup Serial1 for BlueTooth
  Serial.begin(9600);
  Serial1.begin(9600);

  pinMode(LED_BUILTIN,OUTPUT);

}

void loop() {
  //Process commands from bluetooth first
  if(Serial1.available()>0){
    String str =Serial1.readString().trim();
    Serial.println(str);
    if(str=="LED_ON"){
      digitalWrite(LED_BUILTIN,HIGH);
      Serial.println("IN LED ON");
         } else if(str=="LED_OFF"){
      digitalWrite(LED_BUILTIN,LOW);
      Serial.println("IN LED OFF");
          }
  }
}
    
