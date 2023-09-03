// Extra sunshine hour code 
int relay = 8;
char sms;
void setup()
{
 pinMode(relay, OUTPUT);
 digitalWrite(relay,HIGH);
 Serial.begin(9600);
}
void loop()
{
 if(Serial.available()!=0)
 {
 sms = Serial.read();
 }
 if(sms == 'a')
 {
 digitalWrite(relay,LOW);
 }
 if(sms == 'b')
 {
 digitalWrite(relay,HIGH);
 }
}