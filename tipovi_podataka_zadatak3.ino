unsigned int adc = 612;
float postotak_naponske_skale;
unsigned int napon_mV;
byte donjiBajt;
  
void setup()
{
  Serial.begin(9600);
  Serial.println("--------------------");
  
  postotak_naponske_skale = (adc * 100UL) / 1023;
  postotak_naponske_skale = (byte)postotak_naponske_skale;
  Serial.print("Postotak naponske skale je: ");
  Serial.print(postotak_naponske_skale);
  Serial.println(" %");
  
  napon_mV = (adc * 5000UL) / 1023;
  donjiBajt = adc;
  Serial.print("Napon u mili Voltima je: ");
  Serial.print(napon_mV);
  Serial.println(" mV");
  
  Serial.print("Decimalni byte: ");
  Serial.println(donjiBajt, DEC);
  Serial.print("Hexadekadski byte: ");
  Serial.println(donjiBajt, HEX);
  Serial.print("Binarni byte: ");
  Serial.println(donjiBajt, BIN);
}


void loop()
{

}
