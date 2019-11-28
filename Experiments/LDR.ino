int LDR = 0;     
int LDRValue = 0;      
int light_sensitivity = 500;    
 
void setup()
  {
    Serial.begin(9600);       
    pinMode(13, OUTPUT); 
  }
 
void loop()
  {
    LDRValue = analogRead(LDR);     
    Serial.println(LDRValue);      
    delay(50);     
 
    if (LDRValue < light_sensitivity) 
      {
        digitalWrite(13, HIGH);
      }
    else
      {
        digitalWrite(13, LOW);
      }
      delay(1000);
  }
