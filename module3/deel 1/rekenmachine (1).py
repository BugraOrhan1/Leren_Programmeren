from functions import *

def get_input(prompt):
    return input(prompt)

def rekenmachine():
    ronde1 = True
    x = False
    
    while True:
        if ronde1:
            print("Wat wilt u doen?")
            print("A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? j) kwadraat ")
            keuze = get_input("Maak uw keuze: ").upper()
            ronde1 = False
        else:
            print("Wil je wat met de uitkomst ({}) doen?".format(uitkomst))
            print("A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets?j)kwadraat")
            keuze = get_input("Maak uw keuze: ").upper()

        if keuze == 'stop':
            print("Programma gestopt.")
            break

        if x is False:
            x = float(get_input("Voer het eerste getal in: "))

        if keuze in ['E', 'F']:
            y = 1
        elif keuze in ['G', 'H']:
            y = 2
        elif keuze == 'J':
            pass

        else:
            y = float(get_input("Voer het tweede getal in: "))

        if keuze == 'A':
            uitkomst = plus(x, y)
            print(f"{x} + {y} = {uitkomst}")
        elif keuze == 'B':
            uitkomst = min(x, y)
            print(f"{x} - {y} = {uitkomst}")
        elif keuze == 'C':
            uitkomst = keer(x, y)
            print(f"{x} x {y} = {uitkomst}")
        elif keuze == 'D':
            if y == 0:
                print("Kan niet door nul delen.")
                continue
            uitkomst = delen(x, y)
            print(f"{x} : {y} = {uitkomst}")
        elif keuze == 'E':
            uitkomst = plus(x, y)
            print(f"{x} + {y} = {uitkomst}")
        elif keuze == 'F':
            uitkomst = min(x, y)
            print(f"{x} - {y} = {uitkomst}")
        elif keuze == 'G':
            uitkomst = keer(x, y)
            print(f"{x} x {y} = {uitkomst}")
        elif keuze == 'H':
            if y == 0:
                print("Kan niet door nul delen.")
                continue
            uitkomst = delen(x, y)
            print(f"{x} : {y} = {uitkomst}")
        elif keuze == 'J':
            uitkomst=kwadraat(x)
            print(f'{x} in kwadraat = {uitkomst}')

        if get_input("Wil je nog een berekening doen? (ja/nee): ").lower() != 'ja':
            print("Programma gestopt.")
            break

        x = uitkomst


rekenmachine()
