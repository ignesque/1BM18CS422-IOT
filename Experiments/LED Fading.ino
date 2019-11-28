int led=11;
int potentiometer=0;
int value=0;
int output=0;
void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(potentiometer,INPUT);
}

void loop()
{
  value=analogRead(potentiometer);
  output=map(value,0,1023,0,255);
  analogWrite(led,output);
}