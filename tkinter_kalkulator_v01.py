import tkinter as tk

# Glavni prozor
glavni_prozor = tk.Tk()
glavni_prozor.title("Kalkulator - Ohmov zakon")
glavni_prozor['bg'] = "#21201d"
glavni_prozor.geometry("500x300")

# Globalni frame koji ćemo mijenjati
okvir = tk.Frame(glavni_prozor, bg="#21201d")
okvir.pack(expand=True, fill="both")

#Funkcije

def ocisti_okvir():
    #Uklanja sve widgete iz trenutnog okvira
    for widget in okvir.winfo_children():
        widget.destroy()

def glavni_izbornik():
    #Prikazuje glavni izbornik s tri opcije
    ocisti_okvir()
    naslov = tk.Label(okvir, text="Izbornik kalkulatora", fg="white", bg="#21201d", font=("Helvetica", 16, "bold"))
    naslov.pack(pady=20)

    tk.Button(okvir, text="Izračunaj napon (U)", command=prikazi_napon,
              bg="#6b635d", fg="white", font=("Helvetica", 14), width=25).pack(pady=5)
    tk.Button(okvir, text="Izračunaj struju (I)", command=prikazi_struju,
              bg="#6b635d", fg="white", font=("Helvetica", 14), width=25).pack(pady=5)
    tk.Button(okvir, text="Izračunaj otpor (R)", command=prikazi_otpor,
              bg="#6b635d", fg="white", font=("Helvetica", 14), width=25).pack(pady=5)

#Pomoćne funkcije za prikaz pojedinog izračuna

def prikazi_napon():
    ocisti_okvir()
    tk.Label(okvir, text="Izračun napona (U = I × R)", fg="white", bg="#21201d", font=("Helvetica", 15, "bold")).pack(pady=10)

    tk.Label(okvir, text="Unesi struju (I):", fg="white", bg="#21201d").pack()
    entry_I = tk.Entry(okvir)
    entry_I.pack()

    tk.Label(okvir, text="Unesi otpor (R):", fg="white", bg="#21201d").pack()
    entry_R = tk.Entry(okvir)
    entry_R.pack()

    rezultat_label = tk.Label(okvir, text="", fg="white", bg="#21201d", font=("Helvetica", 13))
    rezultat_label.pack(pady=10)

    def izracun():
        try:
            I = float(entry_I.get())
            R = float(entry_R.get())
            U = I * R
            rezultat_label.config(text=f"Napon U = {U:.2f} V")
        except ValueError:
            rezultat_label.config(text="Greška: unesi brojeve!")

    tk.Button(okvir, text="Izračunaj", command=izracun,
              bg="#6b635d", fg="white", font=("Helvetica", 12)).pack(pady=5)
    tk.Button(okvir, text="Natrag", command=glavni_izbornik,
              bg="#44403c", fg="white", font=("Helvetica", 12)).pack(side="bottom", pady=10)

def prikazi_struju():
    ocisti_okvir()
    tk.Label(okvir, text="Izračun struje (I = U ÷ R)", fg="white", bg="#21201d", font=("Helvetica", 15, "bold")).pack(pady=10)

    tk.Label(okvir, text="Unesi napon (U):", fg="white", bg="#21201d").pack()
    entry_U = tk.Entry(okvir)
    entry_U.pack()

    tk.Label(okvir, text="Unesi otpor (R):", fg="white", bg="#21201d").pack()
    entry_R = tk.Entry(okvir)
    entry_R.pack()

    rezultat_label = tk.Label(okvir, text="", fg="white", bg="#21201d", font=("Helvetica", 13))
    rezultat_label.pack(pady=10)

    def izracun():
        try:
            U = float(entry_U.get())
            R = float(entry_R.get())
            I = U / R
            rezultat_label.config(text=f"Jakost struje I = {I:.2f} A")
        except ValueError:
            rezultat_label.config(text="Greška: unesi brojeve!")

    tk.Button(okvir, text="Izračunaj", command=izracun,
              bg="#6b635d", fg="white", font=("Helvetica", 12)).pack(pady=5)
    tk.Button(okvir, text="Natrag", command=glavni_izbornik,
              bg="#44403c", fg="white", font=("Helvetica", 12)).pack(side="bottom", pady=10)

def prikazi_otpor():
    ocisti_okvir()
    tk.Label(okvir, text="Izračun otpora (R = U ÷ I)", fg="white", bg="#21201d", font=("Helvetica", 15, "bold")).pack(pady=10)

    tk.Label(okvir, text="Unesi napon (U):", fg="white", bg="#21201d").pack()
    entry_U = tk.Entry(okvir)
    entry_U.pack()

    tk.Label(okvir, text="Unesi struju (I):", fg="white", bg="#21201d").pack()
    entry_I = tk.Entry(okvir)
    entry_I.pack()

    rezultat_label = tk.Label(okvir, text="", fg="white", bg="#21201d", font=("Helvetica", 13))
    rezultat_label.pack(pady=10)

    def izracun():
        try:
            U = float(entry_U.get())
            I = float(entry_I.get())
            R = U / I
            rezultat_label.config(text=f"Otpor R = {R:.2f} Ω")   #Uređujemo rezultat_label tako da se na njemu napiše rezultat
        except ValueError:
            rezultat_label.config(text="Greška: unesi brojeve!")     #Provjeravamo grešku unosa

    tk.Button(okvir, text="Izračunaj", command=izracun,
              bg="#6b635d", fg="white", font=("Helvetica", 12)).pack(pady=5)
    tk.Button(okvir, text="Natrag", command=glavni_izbornik,
              bg="#44403c", fg="white", font=("Helvetica", 12)).pack(side="bottom", pady=10)

#Pokreni s glavnim izbornikom
glavni_izbornik()

#Glavna petlja
glavni_prozor.mainloop()
