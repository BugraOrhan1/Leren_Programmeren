def generate_lists():
    lijst = int(input("Hoeveel lijstjes? "))
    uitslag_lijst = []

    for i in range(1, lijst + 1 ):
        lijst = int(input(f"Hoeveel in lijst {i}? "))
        basis_lijst = list(range(i,  lijst + i))
        uitslag_lijst.append(basis_lijst)

    return uitslag_lijst


lists = generate_lists()
print(lists)
