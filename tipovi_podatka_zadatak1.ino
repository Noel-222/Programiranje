unsigned int napon_mV = 3750;
unsigned int kapacitet_mAh = 2600;
unsigned long ukupna_energija;
float naponV;
float kapacitet_Ah;

void setup()
{
  Serial.begin(9600);
  Serial.println("-----------------------");
  
  // računanje napona u voltima
  naponV = (float)napon_mV / 1000;
  Serial.print("Napon u Voltima: ");
  Serial.println(naponV);
  // računanje kapaciteta u Ah
  kapacitet_Ah = (float)kapacitet_mAh / 1000;
  Serial.print("Kapacitet u Ah: ");
  Serial.println(kapacitet_Ah);
  
  // računanje ukupne energije
  ukupna_energija = (unsigned long)napon_mV * kapacitet_mAh;
  
  Serial.print("Ukupna energija: ");
  Serial.println(ukupna_energija);
  
}


void loop()
{

}
