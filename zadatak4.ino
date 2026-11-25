// 1 pretprocesorski blok
#define SRAM_UKUPNO 2048

// 2 blok varijabli
char oznaka = 'T';
bool zastita = false;
unsigned int ulaz_mV = 12500;
unsigned int izlaz_mV = 5000;
unsigned int struja_mA = 450;
unsigned long vrijeme_s = 86400UL;
float U_pad;
float P_dis;
float E_toplina;

// 3 funkcija setup
void setup() {
  Serial.begin(9600);

  U_pad = (ulaz_mV - izlaz_mV) / 1000.0;
  P_dis = U_pad * (struja_mA / 1000.0);
  E_toplina = P_dis * vrijeme_s;

  unsigned int bajtovi = sizeof(oznaka) + sizeof(zastita)
    + sizeof(ulaz_mV) + sizeof(izlaz_mV) + sizeof(struja_mA)
    + sizeof(vrijeme_s) + sizeof(U_pad) + sizeof(P_dis)
    + sizeof(E_toplina);
  Serial.println("-------------------------");
  
  Serial.print("Kuciste regulatora: ");
  Serial.println(oznaka);
  Serial.print("Termicka zastita: ");
  Serial.println(zastita ? "ukljuceno" : "isključeno");
  Serial.print("Pad napona: ");
  Serial.print(U_pad, 2);
  Serial.println(" V");
  Serial.print("Disipirana snaga: ");
  Serial.print(P_dis, 3);
  Serial.println(" W");
  Serial.print("Toplinska energija: ");
  Serial.print(E_toplina, 0);
  Serial.println(" J");
  Serial.print("Ukupno zauzece SRAM-a: ");
  Serial.print(bajtovi);
  Serial.print(" bajtova od ");
  Serial.print(SRAM_UKUPNO);
  Serial.println(" B");
}

// 4 funkcija loop
void loop() {
}