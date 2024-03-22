aantal_iteraties = 0

while True:
    antwoord = input('? ')
    aantal_iteraties += 1

    if antwoord.lower() == 'quit':
        break

print(f"Aantal iteraties: {aantal_iteraties}")
