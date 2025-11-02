def izracunaj_sumu_liste(lista_vrijednosti): #Prima listu brojeva i vraća njihovu sumu
    suma = 0
    for vrijednost in lista_vrijednosti:
        suma += vrijednost
    return suma


def izracunaj_paralelne(lista_vrijednosti):
    reciprok_suma = 0
    for R in lista_vrijednosti:
        reciprok_suma += 1 / R
    return 1 / reciprok_suma

def izbornik():
    print("----------------------")
    print("Izbornik za kalkulator")
    print("----------------------")
    print("1. Izračun napona struje")
    print("2. Izračun otpora struje")
    print("3. Izračun jakosti struje")
    print("4. Izračun ukupnog serijskog otpora (N otpornika)")
    print("5. Izračun ukupnog paralelnog otpora (N otpornika)")
    print("0. Izlaz")
    print("----------------------")


def napon_struje(jakost, otpor):
    return jakost * otpor


def otpor_struje(napon, jakost):
    return napon / jakost


def jakost_struje(napon, otpor):
    return napon / otpor


while True:
    # Izbornik za kalkulator
    izbornik()

    try:
        opcija = int(input("Izaberite operaciju (1 / 2 / 3 / 4 / 5 / 0): "))
    except Exception:
        print("Pogrešan unos, molimo unesite brojeve 0, 1, 2, 3 , 4 ili 5.")
        continue

    # Struktura grananja
    if opcija == 1:
        print("Izračun napona struje")
        try:
            jakost = float(input("Upiši jakost struje (A): "))
            otpor = float(input("Upiši otpor (Ω): "))
            napon = napon_struje(jakost, otpor)
        except ValueError:
            print("Pogrešan unos! Molimo unesite brojeve za jakost i otpor.")
            continue
        print(f"Napon struje je: {napon:.2f} V\n")

    elif opcija == 2:
        print("Izračun otpora struje")
        try:
            napon = float(input("Upiši napon (V): "))
            jakost = float(input("Upiši jakost struje (A): "))
            otpor = otpor_struje(napon, jakost)
        except ValueError:
            print("Pogrešan unos! Molimo unesite brojeve za napon i jakost.")
            continue
        except ZeroDivisionError:
            print("Greška: Ne mogu dijeliti s nulom!")
            continue
        print(f"Otpor je: {otpor:.2f} Ω\n")

    elif opcija == 3:
        print("Izračun jakosti struje")
        try:
            napon = float(input("Upiši napon (V): "))
            otpor = float(input("Upiši otpor (Ω): "))
            jakost = jakost_struje(napon, otpor)
        except ValueError:
            print("Pogrešan unos! Molimo unesite brojeve za napon i otpor.")
            continue
        except ZeroDivisionError:
            print("Greška: Ne mogu dijeliti s nulom!")
            continue
        print(f"Jakost struje je: {jakost:.4f} A\n")

    elif opcija == 4:
        print("\nIzračun serijskog otpora (N otpornika)")

        lista_otpora = []  # 1. Kreiramo praznu listu

        # 2. Pokrećemo petlju za unos otpornika
        while True:
            print(f"Trenutni otpornici u listi: {[f'{x:.2f} Ω' for x in lista_otpora]}")
            unos_str = input("Unesite vrijednost otpora (ili 'kraj' za izračun): ")

            if unos_str.lower() == 'kraj':
                break

            try:
                vrijednost = float(unos_str)
                if vrijednost <= 0:
                    print("GREŠKA: Otpor mora biti pozitivan broj.")
                else:
                    lista_otpora.append(vrijednost)
                    print(f" -> Dodan otpornik: {vrijednost:.2f} Ω")
            except ValueError:
                print("GREŠKA: Unos mora biti ispravan broj ili riječ 'kraj'.")

        # 6. Nakon što je korisnik unio 'kraj'
        if len(lista_otpora) > 0:
            ukupni_otpor = izracunaj_sumu_liste(lista_otpora)
            print(f"\nREZULTAT: Ukupan serijski otpor za {len(lista_otpora)} otpornika je: {ukupni_otpor:.4f} Ω")
        else:
            print("\nNiste unijeli nijedan otpornik.")

        input("\nPritisnite Enter za povratak na glavni izbornik...")
    elif opcija == 5:
        print("\nIzračun paralelnog otpora (N otpornika)")
        lista_otpora = []

        while True:
            print(f"Trenutni otpornici u listi: {[f'{x:.2f} Ω' for x in lista_otpora]}")
            unos_str = input("Unesite vrijednost otpora (ili 'kraj' za izračun): ")

            if unos_str.lower() == 'kraj':
                break

            try:
                vrijednost = float(unos_str)
                if vrijednost <= 0:
                    print("GREŠKA: Otpor mora biti pozitivan broj.")
                else:
                    lista_otpora.append(vrijednost)
                    print(f"   -> Dodan otpornik: {vrijednost:.2f} Ω")
            except ValueError:
                print("GREŠKA: Unos mora biti broj ili 'kraj'.")

        if len(lista_otpora) > 0:
            try:
                ukupni_otpor = izracunaj_paralelne(lista_otpora)
                print(f"\nREZULTAT: Ukupan paralelni otpor za {len(lista_otpora)} otpornika je: {ukupni_otpor:.4f} Ω")
            except ZeroDivisionError:
                print("\nGREŠKA: Jedan od unesenih otpornika ima vrijednost 0 Ω!")
        else:
            print("\nNiste unijeli nijedan otpornik.")
        input("\nPritisnite Enter za povratak na glavni izbornik...")
    elif opcija == 0:
        print("Hvala na korištenju kalkulatora.")
        break

    else:
        print("Pogrešan unos! Molimo unesite 0, 1, 2, 3 ili 4.\n")
