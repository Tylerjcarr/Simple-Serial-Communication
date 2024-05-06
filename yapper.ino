//basic functions to prove it works, no extra things needed like before. 

void setup() { 
 Serial.begin(115200); //I have the uno4 wifi, use the serial based on your board and use that value on the on pi aswell
}
 
void loop() { 
  Serial.println("Yo!"); 
  delay(1000); //sends every second 
}
