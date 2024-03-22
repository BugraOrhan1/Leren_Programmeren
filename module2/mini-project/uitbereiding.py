import random

namen = []
loop = True

while loop:
    naam = input("Voer een naam in: ")
    if naam not in namen:
        namen.append(naam)
    else:
        print("Deze naam is al ingevoerd. Voer een unieke naam in.")
    if len(namen) > 2:
        door_gaan = input('Wil je doorgaan met loten of wil je nog een naam toevoegen (loten/naam)? ')
        if door_gaan != 'naam':
            loop = False

lootjes = namen[:]
ok = False
while True:
    # shuffle
    if not ok:
        random.shuffle(lootjes)
    # controle
    ok = True
    for naam, lootje in zip(namen, lootjes):
        if naam == lootje:
            ok = False
            break  
    if ok:
        break

for naam, lootje in zip(namen, lootjes):
    print(f"Naam: {naam}, Lootje: {lootje}")


for naam, lootje in zip(namen, lootjes):

    naam_uitloting = input('wie ben je?')
    x = naam_uitloting           +  '        '  +         lootje
    if naam_uitloting in namen:
        print(x)
        
