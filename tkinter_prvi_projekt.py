import tkinter as tk

glavni_prozor = tk.Tk()
glavni_prozor.title("Glavni prozor")
glavni_prozor['bg'] = "#21201d"
glavni_prozor.minsize(500, 300)

n = 0

def pritisak_plus():
    global n 
    n += 1    
    tekst.config(text=f"Broj klikova: {n}") 
    print(n)

def pritisak_minus():
    global n
    n -= 1
    tekst.config(text=f"Broj klikova: {n}")
    print(n)

tekst = tk.Label(glavni_prozor, 
                 text=f"Broj klikova: {n}", 
                 fg="White", 
                 bg="#21201d", 
                 font=("Helvetica", 20))
tekst.place(x=155 , y=20)

dugme = tk.Button(glavni_prozor, 
                  text="Povečaj vrijednost", 
                  bg="#6b635d", 
                  borderwidth=2,
                  relief=tk.SOLID, 
                  fg="White", 
                  font=("Helvetica", 17), 
                  command=pritisak_plus)

dugme2 = tk.Button(glavni_prozor, 
                  text="Smanji vrijednost", 
                  bg="#6b635d", 
                  borderwidth=2,
                  relief=tk.SOLID, 
                  fg="White", 
                  font=("Helvetica", 17), 
                  command=pritisak_minus)

dugme2.place(x=30 , y=150)
dugme.place(x=270 , y=150)

glavni_prozor.mainloop()
