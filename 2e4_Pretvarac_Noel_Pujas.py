# Izbornik za pretvarač
while True:
    print("Izbornik za Pretvarač Mjernih Jedinica")
    print("----------------------")
    print("0. Izlaz iz pretvarača")
    print("1. Volt --> Milivolt (mV)")
    print("2. Ohmi (Ω) --> Kiloohmi (kΩ)")
    print("3. Amperi (A) --> Miliamperi (mA)")
    print("----------------------")
    opcija=int(input("Izaberite opciju ( 0. / 1. / 2. / 3. ): "))
    # Struktura grananja
    if opcija == 1:
        print("Pretvorba Volta u Milivolte.")
        napon=float(input("Upiši napon: ")) #   --- >   koristimo float za decimalne brojeve
        mili = napon*1000
        print(f"Npaon of {napon} V je {mili} mV") #   --- >   ispisujemo rezultat
        print("----------------------")
    elif opcija == 2: #   --- >   odabir druge opcije
        print("Pretvorba Ohma u Kiloohme.")
        otpor=float(input("Upiši otpor: "))
        kO=otpor/1000
        print(f"Otpor {otpor} Ω je {kO} kΩ")
        print("----------------------")
    elif opcija == 3:
        print("Pretvorba Ampera u Miliampere.")
        jakost=float(input("Upiši jakost struje: "))
        mA = jakost*1000
        print(f"Jakost struje {jakost} A je {mA} mA")
        print("----------------------")
    elif opcija == 0:
        print("Hvala na korištenju pretvarača.")
        break  #   --- >   završavamo program
    else:
        print("Pogrešan unos..") #   --- >   ako je unesena pogrešna vrijednost program se ponavlja
        print("----------------------")
