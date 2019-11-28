int button=3;
int led=13;
int buttonstate=0;

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(button,INPUT);
}

void loop()
{
  buttonstate=digitalRead(button);
  if(buttonstate==HIGH){
  digitalWrite(13, HIGH);
  }
  else{
  digitalWrite(13, LOW);
}
}