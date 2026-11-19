unsigned long otpor = 100000;
float kapacitet = 47e-6;
float tau;
float vrijemePunjena;

void setup()
{
  Serial.begin(9600);
  Serial.println("----------------");
  
  tau = otpor * kapacitet;
  vrijemePunjena = 5 * tau;
  
  Serial.print("Tau je: ");
  Serial.println(tau, 3);
  Serial.print("Vrijeme punjena je: ");
  Serial.println(vrijemePunjena);
}


void loop()
{

}
