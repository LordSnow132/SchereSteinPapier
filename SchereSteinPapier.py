import random
while (True):
    print("Schnick")
    print("Schnack")
    print("Schnuck")
    Mensch=input()
    Auswahl = ["Schere","Stein","Papier"]
    Computer = random.choice(Auswahl)
    print(Computer)
    if Mensch == Computer:
        print("Unentschieden")
    elif Mensch == "Schere" and Computer == "Stein":
        print("Du hast verloren")
    elif Mensch =="Schere" and Computer =="Papier":
        print("Du hast Gewonnen")
    elif Mensch == "Papier" and Computer =="Schere":
        print("Du hast verloren")
    elif Mensch =="Papier" and Computer == "Stein":
        print("Du hast gewonnen")
    elif Mensch == "Stein" and Computer =="Papier":
        print("Du hast verloren")
    else:
        print("Du hast gewonnen")