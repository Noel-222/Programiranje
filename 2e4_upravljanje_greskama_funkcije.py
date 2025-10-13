# Izbornik za pretvarač
def ispis_izbornika():
    print("Izbornik za Pretvarač Mjernih Jedinica")
    print("----------------------")
    print("0. Izlaz iz pretvarača")
    print("1. Volt --> Milivolt (mV)")
    print("2. Ohmi (Ω) --> Kiloohmi (kΩ)")
    print("3. Amperi (A) --> Miliamperi (mA)")
    print("----------------------")
def pretvori_V_u_mV():
    try:
        print("Pretvorba Volta u Milivolte.")
        napon=float(input("Upiši napon: ")) #   --- >   koristimo float za decimalne brojeve
        mili = napon*1000
        print(f"Npaon of {napon} V je {mili} mV") #   --- >   ispisujemo rezultat
        print("----------------------")
    except ValueError:
        print("GREŠKA: Unesena vrijednost nije ispravan broj.")
def pretvori_Ohm_u_kOhm():
    try:
        print("Pretvorba Ohma u Kiloohme.")
        otpor=float(input("Upiši otpor: "))
        kO=otpor/1000
        print(f"Otpor {otpor} Ω je {kO} kΩ")
        print("----------------------")
    except ValueError:
        print("GREŠKA: Unesena vrijednost nije ispravan broj.")
def pretvori_A_u_mA():
    try:
        print("Pretvorba Ampera u Miliampere.")
        jakost=float(input("Upiši jakost struje: "))
        mA = jakost*1000
        print(f"Jakost struje {jakost} A je {mA} mA")
        print("----------------------")
    except ValueError:
        print("GREŠKA: Unesena vrijednost nije ispravan broj.")
while True:
    ispis_izbornika()
    # Obrada grešaka
    try:
        opcija=int(input("Izaberite opciju ( 0. / 1. / 2. / 3. ): "))
    except Exception as greska:
        print(f"Pogrešan unos.. tip greške: {greska}")
        continue
    # Struktura grananja
    if opcija == 1:
        pretvori_V_u_mV() #   --- >   poziv funkcije za pretvorbu Volta u Milivolte
    elif opcija == 2: #   --- >   odabir druge opcije
        pretvori_Ohm_u_kOhm()
    elif opcija == 3:
        pretvori_A_u_mA()
    elif opcija == 0:
        print("Hvala na korištenju pretvarača.")
        break  #   --- >   završavamo program
    else:
        print("Pogrešan unos..") #   --- >   ako je unesena pogrešna vrijednost program se ponavlja
        print("----------------------")