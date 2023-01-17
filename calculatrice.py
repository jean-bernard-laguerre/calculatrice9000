from tkinter import *
from tkinter import ttk

fenetre = Tk()

def bouton_num(num):
    ecran.insert(END, num)

def bouton_egal():
    try:
        resultat = eval(ecran.get())

        res_hist = f"{ecran.get()} = {resultat}"

        lbl_hist = Label(hist, text=res_hist)
        lbl_hist.pack()

        ecran.delete(0, END)
        ecran.insert(0, resultat)
    except:
        print("operation invalide")

    pass

def operation(operateur):
    ecran.insert(END, operateur)

def clear():
    ecran.delete(0, END)

def clear_historique():
    for widget in hist.winfo_children():
        widget.destroy()


ecran = Entry(fenetre, font=('Arial',12))
ecran.pack(fill="both", expand="yes")

touches = Frame(fenetre)
touches.pack(fill="both", expand="yes")

calc_hist = LabelFrame(fenetre, text="Historique")
calc_hist.pack(fill="both", expand="yes")
btn_clr_hist = Button(calc_hist, text="Vider l'historique", command= clear_historique)
btn_clr_hist.pack(fill="both", expand="yes")
hist = Frame(calc_hist)
hist.pack(fill="both", expand="yes")


btn_1 = Button(touches, width=10, pady=20,  text="1", command=lambda : bouton_num(1))
btn_2 = Button(touches, width=10, pady=20, text="2", command=lambda : bouton_num(2))
btn_3 = Button(touches, width=10, pady=20, text="3", command=lambda : bouton_num(3))
btn_4 = Button(touches, width=10, pady=20, text="4", command=lambda : bouton_num(4))
btn_5 = Button(touches, width=10, pady=20, text="5", command=lambda : bouton_num(5))
btn_6 = Button(touches, width=10, pady=20, text="6", command=lambda : bouton_num(6))
btn_7 = Button(touches, width=10, pady=20, text="7", command=lambda : bouton_num(7))
btn_8 = Button(touches, width=10, pady=20, text="8", command=lambda : bouton_num(8))
btn_9 = Button(touches, width=10, pady=20, text="9", command=lambda : bouton_num(9))
btn_0 = Button(touches, width=10, pady=20, text="0", command=lambda : bouton_num(0))
btn_point = Button(touches, width=10, pady=20, text=".", command=lambda : bouton_num("."))

btn_plus = Button(touches, width=10, pady=20, text="+", command=lambda : operation("+"))
btn_moins = Button(touches, width=10, pady=20, text="-", command=lambda : operation("-"))
btn_mult = Button(touches, width=10, pady=20, text="*", command=lambda : operation("*"))
btn_div = Button(touches, width=10, pady=20, text="/", command=lambda : operation("/"))

btn_racine = Button(touches, width=10, pady=20, text="√", command=lambda : operation("√"))
btn_carré = Button(touches, width=10, pady=20, text="²", command=lambda : operation("²"))
btn_pourcent = Button(touches, width=10, pady=20, text="%", command=lambda : operation("%"))

btn_clear = Button(touches, width=10, pady=20, text="suppr", command= clear)

btn_egal = Button(touches, width=10, pady=20, text="=", command=bouton_egal, bg="orange")


btn_1.grid(row=1, column=1)
btn_2.grid(row=1, column=2)
btn_3.grid(row=1, column=3)
btn_4.grid(row=2, column=1)
btn_5.grid(row=2, column=2)
btn_6.grid(row=2, column=3)
btn_7.grid(row=3, column=1)
btn_8.grid(row=3, column=2)
btn_9.grid(row=3, column=3)
btn_0.grid(row=4, column=2)
btn_point.grid(row=4, column=1)

btn_plus.grid(row=1, column=0)
btn_moins.grid(row=2, column=0)
btn_mult.grid(row=3, column=0)
btn_div.grid(row=4, column=0)

btn_racine.grid(row=0, column=0)
btn_carré.grid(row=0, column=1)
btn_pourcent.grid(row=0, column=2)
btn_clear.grid(row=0, column=3)

btn_egal.grid(row=4, column=3)


fenetre.mainloop()

