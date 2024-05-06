//basic functions to prove it works, no extra things needed like before. 

int ledPin = LED_BUILTIN; //on board yellow led

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200); //I have the uno4 wifi, use the serial based on your board and use that value on the on pi aswell
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); //continuously reads from the pi until stopped with ctrl c
    if (input == "on") {
      digitalWrite(ledPin, HIGH); 
    } else if (input == "off") {
      digitalWrite(ledPin, LOW);
    } else if (input == "blink") {
      for (int i = 0; i < 3; i++) {
        digitalWrite(ledPin, HIGH); 
        delay(1000);
        digitalWrite(ledPin, LOW);
        delay(1000);
      }
    }
  }
}
