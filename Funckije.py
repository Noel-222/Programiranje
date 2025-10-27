def izbornik():
    print("----------------------")
    print("Izbornik za kalkulator")
    print("----------------------")
    print("1. Izračun napona struje")
    print("2. Izračun otpora struje")
    print("3. Izračun jakosti struje")
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
        opcija = int(input("Izaberite operaciju (1 / 2 / 3 / 0):"))
    except Exception as greska:
        print(f"Pogrešan unos, molimo unesite brojeve 1, 2 ili 3. \nOdaberite 0 za izlaz.")
        continue
    #Struktura grananja

    if opcija == 1:     # == != < > <> >= <= - operatori usporedbe
        print("Izračun napona struje")
        try:
            jakost = int(input("Upiši jakost struje: "))
            otpor = int(input("Upiši otpor: "))
            napon = napon_struje(jakost, otpor)
        except ValueError:
            print("Pogrešan unos \nmolimo unesite brojeve za jakost i otpor struje.")
            continue
        except Exception as greska:
            print(f"Došlo je do pogreške: {greska}")
            continue
        print(f"Napon struje je: {napon} V")
    elif opcija == 2:
        print("Izračun otpora struje")
        try: 
            napon = int(input("Upiši napon: "))
            jakost = int(input("Upiši jakost struje: "))
            otpor = otpor_struje(napon, jakost)
        except ValueError:
            print("Pogrešan unos \nmolimo unesite brojeve za napon i jakost struje.")
            continue
        except ZeroDivisionError:
            print("Ne mogu dijeliti s nulom!")
            continue
        except Exception as greska:
            print(f"Došlo je do pogreške: {greska}")
            continue
        print(f"Otpor je: {otpor} Ohm")
    elif opcija == 3:
        print("Izračun jakosti struje")
        try: 
            napon = int(input("Upiši napon: "))
            otpor = int(input("Upiši otpor: "))
            jakost = jakost_struje(napon, otpor)
        except ValueError:
            print("Pogrešan unos \nmolimo unesite brojeve za napon i otpor.")
            continue
        except ZeroDivisionError:
            print("Ne mogu dijeliti s nulom!")
            continue
        except Exception as greska:
            print(f"Došlo je do pogreške: {greska}")
            continue
        print(f"Jakost struje je: {jakost} A")
    elif opcija == 0:
        print("Hvala na korištenju kalkulatora.")
        break
    else:
        print("Pogrešan unos")