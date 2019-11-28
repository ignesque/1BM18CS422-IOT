int red = 13; 
int yellow = 11;
int green = 9;


void setup()
{
pinMode(red,OUTPUT);
pinMode(yellow,OUTPUT);
pinMode(green,OUTPUT);
}

void loop()
{
changeLights();
delay(2000);
}

void changeLights(){
digitalWrite(red,HIGH);
  digitalWrite(yellow,LOW);
delay(3000);
digitalWrite(yellow,HIGH);
digitalWrite(red,LOW);
delay(1000);
digitalWrite(yellow,LOW);
digitalWrite(green,HIGH);
delay(4000);

digitalWrite(yellow,HIGH);
digitalWrite(green,LOW);
}
