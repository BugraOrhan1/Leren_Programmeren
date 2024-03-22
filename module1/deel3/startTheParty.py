gastheer = input("Wie is de gastheer? : ")
gasten = int(input("Hoeveel gasten zijn aanwezig? (0 als er geen gasten zijn): "))

chips = True
drank = True

if (not chips and not drank) or (gasten >= 4 and gasten <= 20) or (gastheer):
    print("Party!")
elif gastheer == "Bugra":
    print("Party!")
elif gastheer == "Oorschot":
    print("No Party")
else:
    print("No Party")
