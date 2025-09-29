# Izbornik za kalkulator
print("----------------------")
print("Izbornik za kalkulator")
print("----------------------")
print("1. Izračun napona")
print("2. Izračun otpora")
print("3. Izračun jakosti")
print("4. Izračun serijskih i paralelnih otpora")
print("----------------------")
while True:
    opcija=int(input("Izaberite opciju (1. / 2. / 3. / 4. ): "))
    # Struktura grananja
    if opcija == 1:     # == , != , <> , <= , >=
        print("Izračun napona struje")
        jakost=int(input("Upiši jakost struje: "))
        otpor=int(input("Upiši otpor: "))
        napon = jakost*otpor
        print(f"Npaon struje je: {napon} V")
    elif opcija == 2:
        print("Izračun otpora struje: ")
        napon=int(input("Upiši napon: "))
        jakost=int(input("Upiši jakost struje: "))
        otpor= napon/jakost
        print(f"Otpor je: {otpor} Ω")
    elif opcija == 3:
        print("Izračun jakosti struje: ")
        napon=int(input("Upiši napon: "))
        otpor=int(input("Upiši otpor struje: "))
        jakost = napon/otpor
        print(f"Jakost struje je: {jakost} A")
    elif opcija == 4:
        sip=input("Jesu li otpornici u seriji ili paraleli? (seriji , paraleli): ")
        if sip == "seriji":
            otpor1=int(input("Upiši otpor prvog otpornika: "))
            otpor2=int(input("Upiši otpor drugog otpornika: "))
            ukupniotporS=otpor1+otpor2
            print(f"Ukupni otpor je {ukupniotporS} Ω")
        elif sip == "paraleli":
            otpor1=int(input("Upiši otpor prvog otpornika: "))
            otpor2=int(input("Upiši otpor drugog otpornika: "))
            ukupniotporP=(1/otpor1)+(1/otpor2)
            print(f"Ukupni otpor je {ukupniotporP} Ω")
        else:
            print("Pogrešan unos..")
    else:
        print("Pogrešan unos..")

    ponovo=input("Želiš li ponoviti? (da / ne): ")
    if ponovo != "da":
        break
