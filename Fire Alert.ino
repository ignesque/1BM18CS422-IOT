
int buzz=8;
int alert=0;
int led=13;
void setup(){
  pinMode(led,OUTPUT);
  pinMode(buzz,OUTPUT);
  pinMode(alert,INPUT);
	Serial.begin(9600);
}
void loop(){
      Serial.println(analogRead(alert));
  if(analogRead(alert)<150){
    digitalWrite(buzz,HIGH);
    digitalWrite(led,HIGH);
    delay(400);
    digitalWrite(led,LOW);
    digitalWrite(buzz,LOW);
	delay(500);
  }
  else{
    digitalWrite(buzz,LOW);
    digitalWrite(led,LOW);
  }
}