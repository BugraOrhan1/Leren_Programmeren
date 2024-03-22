gastheer = input("Wie is de gastheer? : ").lower()
gasten = int(input("Hoeveel gasten zijn aanwezig? (0 als er geen gasten zijn): "))

chips = True
drank = True
party_gasten = gasten >= 4 and gasten <= 20 and chips and drank
party_gastheren = gastheer !='' and drank and gastheer != 'oorschot'
party_zelf = gastheer == 'bugra'
if party_gasten or party_gastheren:
    print("Party!")
else:
    print("No Party")
