from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

fenetre = Tk()
fenetre.title("Calculatrice")

equation = ""
equation_ecran = StringVar()
equation_ecran.set("")
entree_ecran = StringVar()
entree_ecran.set("")


def Bouton_num(num):

    if len(entree_ecran.get() + str(num)) > 1 and entree_ecran.get()[0] == "0":
        entree_ecran.set(str(num))
    else:
        entree_ecran.set(entree_ecran.get() + str(num))


def Calcul():

    global equation

    equation += entree_ecran.get()

    try:
        
        resultat = eval(equation)

        equation_ecran.set(equation_ecran.get() + entree_ecran.get())
        res_hist = f"{equation_ecran.get()} = {resultat}"

        lbl_hist = Label(hist, text=res_hist)
        lbl_hist.pack()

        
        equation = ""
        equation_ecran.set("")
        entree_ecran.set(f"{resultat}")

    except:
        showerror('Erreur', 'Equation invalide')

# Gere l'equation et la façon dont elle est affichée
def Operation(operateur):

    global equation

    match operateur:
        case "²":
            equation_ecran.set(equation_ecran.get() + entree_ecran.get() + "²")
            equation += f"({entree_ecran.get()}**2)"
        case "√":
            equation_ecran.set(equation_ecran.get() + f"√({entree_ecran.get()})")
            equation += f"({entree_ecran.get()}**(1/2))"
        case "%":
            equation_ecran.set(equation_ecran.get() + entree_ecran.get() + "%")
            equation += f"({entree_ecran.get()}/100)"
        case "1/x":
            equation_ecran.set(equation_ecran.get() + f"(1/{entree_ecran.get()})")
            equation += f"(1/{entree_ecran.get()})"
        case "!":
            equation_ecran.set(equation_ecran.get() + entree_ecran.get() + "!")
            equation += str(Factoriel( int(entree_ecran.get()) ))
        case "^":
            equation_ecran.set(equation_ecran.get() + entree_ecran.get() + "^")
            equation += entree_ecran.get() + "**"
        case "mod":
            equation_ecran.set(equation_ecran.get() + entree_ecran.get() + "mod")
            equation += entree_ecran.get() + "%"
        case _:
            equation_ecran.set(equation_ecran.get() + entree_ecran.get() + operateur)
            equation += entree_ecran.get() + operateur

    entree_ecran.set("")


def Factoriel(num):

    if num <= 1:
        return 1
    else:
        return num * Factoriel(num-1)

# Efface l'equation en cours
def Effacer():

    global equation

    entree_ecran.set("")
    equation_ecran.set("")
    equation = ""

# Efface L'historique
def Suppr_historique():
    for element in hist.winfo_children():
        element.destroy()

affichage = Frame(fenetre, bd=6, relief=SUNKEN)
affichage.pack(fill="both", expand="yes")
# Affiche l'equation
ecran_eq = Label(affichage, height=3, bg="#C1ECF4", font=('Arial',12), textvariable=equation_ecran, anchor='nw')
ecran_eq.pack(fill="both", expand="yes")
# Affiche l'entree de l'utilisateur
ecran = Label(affichage, bg="#C1ECF4", font=('Arial',20), textvariable= entree_ecran, anchor='e')
ecran.pack(fill="both", expand="yes")


touches = Frame(fenetre)
touches.pack(anchor= "center")

calc_hist = LabelFrame(fenetre, text="Historique")
calc_hist.pack(fill="both", expand="yes")
btn_vide_hist = Button(calc_hist, text="Vider l'historique", command= Suppr_historique)
btn_vide_hist.pack(fill="both", expand="yes")
hist = Frame(calc_hist)
hist.pack(fill="both", expand="yes")

# Boutons numerique
btn_1 = Button(touches, width=7, height=2,  text="1", command=lambda : Bouton_num(1), font=('Arial',12))
btn_2 = Button(touches, width=7, height=2, text="2", command=lambda : Bouton_num(2), font=('Arial',12))
btn_3 = Button(touches, width=7, height=2, text="3", command=lambda : Bouton_num(3), font=('Arial',12))
btn_4 = Button(touches, width=7, height=2, text="4", command=lambda : Bouton_num(4), font=('Arial',12))
btn_5 = Button(touches, width=7, height=2, text="5", command=lambda : Bouton_num(5), font=('Arial',12))
btn_6 = Button(touches, width=7, height=2, text="6", command=lambda : Bouton_num(6), font=('Arial',12))
btn_7 = Button(touches, width=7, height=2, text="7", command=lambda : Bouton_num(7), font=('Arial',12))
btn_8 = Button(touches, width=7, height=2, text="8", command=lambda : Bouton_num(8), font=('Arial',12))
btn_9 = Button(touches, width=7, height=2, text="9", command=lambda : Bouton_num(9), font=('Arial',12))
btn_0 = Button(touches, width=7, height=2, text="0", command=lambda : Bouton_num(0), font=('Arial',12))
btn_point = Button(touches, width=7, height=2, text=".", command=lambda : Bouton_num("."), font=('Arial',12))

# Boutons operateur
btn_plus = Button(touches, width=7, height=2, text="+", command=lambda : Operation("+"), font=('Arial',12))
btn_moins = Button(touches, width=7, height=2, text="-", command=lambda : Operation("-"), font=('Arial',12))
btn_mult = Button(touches, width=7, height=2, text="*", command=lambda : Operation("*"), font=('Arial',12))
btn_div = Button(touches, width=7, height=2, text="/", command=lambda : Operation("/"), font=('Arial',12))

btn_racine = Button(touches, width=7, height=2, text="√", command=lambda : Operation("√"), font=('Arial',12))
btn_carré = Button(touches, width=7, height=2, text="²", command=lambda : Operation("²"), font=('Arial',12))
btn_pourcent = Button(touches, width=7, height=2, text="%", command=lambda : Operation("%"), font=('Arial',12))

btn_fact = Button(touches, width=7, height=2, text="x!", command=lambda : Operation("!"), font=('Arial',12))
btn_inv = Button(touches, width=7, height=2, text="1/x", command=lambda : Operation("1/x"), font=('Arial',12))
btn_puissance = Button(touches, width=7, height=2, text="^", command=lambda : Operation("^"), font=('Arial',12))
btn_mod = Button(touches, width=7, height=2, text="mod", command=lambda : Operation("mod"), font=('Arial',12))

btn_suppr = Button(touches, width=7, height=2, text="suppr", command= Effacer, bg="red", fg="white", font=('Arial',12))

btn_egal = Button(touches, width=7, height=2, text="=", command=Calcul, bg="orange", font=('Arial',12))


#Dispostion des boutons
btn_1.grid(row=2, column=1)
btn_2.grid(row=2, column=2)
btn_3.grid(row=2, column=3)
btn_4.grid(row=3, column=1)
btn_5.grid(row=3, column=2)
btn_6.grid(row=3, column=3)
btn_7.grid(row=4, column=1)
btn_8.grid(row=4, column=2)
btn_9.grid(row=4, column=3)
btn_0.grid(row=5, column=2)
btn_point.grid(row=5, column=1)

btn_plus.grid(row=2, column=0)
btn_moins.grid(row=3, column=0)
btn_mult.grid(row=4, column=0)
btn_div.grid(row=5, column=0)

btn_racine.grid(row=0, column=0)
btn_carré.grid(row=0, column=1)
btn_pourcent.grid(row=0, column=2)
btn_suppr.grid(row=0, column=3)

btn_fact.grid(row=1,column=0)
btn_inv.grid(row=1,column=1)
btn_puissance.grid(row=1, column=2)
btn_mod.grid(row=1, column=3)

btn_egal.grid(row=5, column=3)


fenetre.mainloop()

