from tkinter import *
from tkinter import ttk

fenetre = Tk()
fenetre.title("Calculatrice")

equation = ""
equation_ecran = StringVar()
equation_ecran.set("")

def bouton_num(num):

    ecran.insert(END, num)


def calcul():

    global equation
 
    try:
        equation += ecran.get()
        resultat = eval(equation)

        equation_ecran.set(equation_ecran.get() + ecran.get())
        res_hist = f"{equation_ecran.get()} = {resultat}"

        lbl_hist = Label(hist, text=res_hist)
        lbl_hist.pack()

        ecran.delete(0, END)
        equation = ""
        equation_ecran.set("")
        ecran.insert(0, resultat)

    except:
        print("operation invalide")


def operation(operateur):

    global equation

    match operateur:
        case "²":
            equation_ecran.set(equation_ecran.get() + ecran.get() + "²")
            equation += ecran.get() +"**2"
        case "√":
            equation_ecran.set(equation_ecran.get() + f"√({ecran.get()})")
            equation += ecran.get() +"**(1/2)"
        case "%":
            equation_ecran.set(equation_ecran.get() + ecran.get() + "%")
            equation += ecran.get() +"/100"
        case _:
            equation_ecran.set(equation_ecran.get() + ecran.get() + operateur)
            equation += ecran.get() + operateur

    ecran.delete(0, END)


def effacer():

    global equation

    ecran.delete(0, END)
    equation_ecran.set("")
    equation = ""


def clear_historique():
    for widget in hist.winfo_children():
        widget.destroy()



ecran_eq = Label(fenetre, height=3, bg="white", font=('Arial',12), textvariable=equation_ecran)
ecran_eq.pack(fill="both", expand="yes")
ecran = Entry(fenetre, font=('Arial',16), highlightthickness=0, relief=FLAT)
ecran.pack(fill="both", expand="yes")

touches = Frame(fenetre)
touches.pack(anchor= "center")

calc_hist = LabelFrame(fenetre, text="Historique")
calc_hist.pack(fill="both", expand="yes")
btn_vide_hist = Button(calc_hist, text="Vider l'historique", command= clear_historique)
btn_vide_hist.pack(fill="both", expand="yes")
hist = Frame(calc_hist)
hist.pack(fill="both", expand="yes")


btn_1 = Button(touches, width=7, height=2,  text="1", command=lambda : bouton_num(1), font=('Arial',12))
btn_2 = Button(touches, width=7, height=2, text="2", command=lambda : bouton_num(2), font=('Arial',12))
btn_3 = Button(touches, width=7, height=2, text="3", command=lambda : bouton_num(3), font=('Arial',12))
btn_4 = Button(touches, width=7, height=2, text="4", command=lambda : bouton_num(4), font=('Arial',12))
btn_5 = Button(touches, width=7, height=2, text="5", command=lambda : bouton_num(5), font=('Arial',12))
btn_6 = Button(touches, width=7, height=2, text="6", command=lambda : bouton_num(6), font=('Arial',12))
btn_7 = Button(touches, width=7, height=2, text="7", command=lambda : bouton_num(7), font=('Arial',12))
btn_8 = Button(touches, width=7, height=2, text="8", command=lambda : bouton_num(8), font=('Arial',12))
btn_9 = Button(touches, width=7, height=2, text="9", command=lambda : bouton_num(9), font=('Arial',12))
btn_0 = Button(touches, width=7, height=2, text="0", command=lambda : bouton_num(0), font=('Arial',12))
btn_point = Button(touches, width=7, height=2, text=".", command=lambda : bouton_num("."), font=('Arial',12))

btn_plus = Button(touches, width=7, height=2, text="+", command=lambda : operation("+"), font=('Arial',12))
btn_moins = Button(touches, width=7, height=2, text="-", command=lambda : operation("-"), font=('Arial',12))
btn_mult = Button(touches, width=7, height=2, text="*", command=lambda : operation("*"), font=('Arial',12))
btn_div = Button(touches, width=7, height=2, text="/", command=lambda : operation("/"), font=('Arial',12))

btn_racine = Button(touches, width=7, height=2, text="√", command=lambda : operation("√"), font=('Arial',12))
btn_carré = Button(touches, width=7, height=2, text="²", command=lambda : operation("²"), font=('Arial',12))
btn_pourcent = Button(touches, width=7, height=2, text="%", command=lambda : operation("%"), font=('Arial',12))

btn_fact = Button(touches, width=7, height=2, text="x!", command=lambda : operation("!"), font=('Arial',12))


btn_suppr = Button(touches, width=7, height=2, text="suppr", command= effacer, bg="red", fg="white", font=('Arial',12))

btn_egal = Button(touches, width=7, height=2, text="=", command=calcul, bg="orange", font=('Arial',12))


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
btn_suppr.grid(row=0, column=3)

btn_egal.grid(row=4, column=3)


fenetre.mainloop()

