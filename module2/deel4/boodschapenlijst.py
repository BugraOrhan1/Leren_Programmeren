boodschappenlijst = []

toevoegen = input('Wil je wat toevoegen aan je lijst? (ja/nee): ')

while toevoegen.lower() == 'ja':
    item = input("Voer het item in: ").lower()
    hoeveelheid = int(input(f"Voer de hoeveelheid {item} in: "))
    
    boodschappenlijst.append((item, hoeveelheid))
    
    toevoegen = input('Wil je nog iets toevoegen aan je lijst? (ja/nee): ')

print("Je boodschappenlijstje:")
for item, hoeveelheid in boodschappenlijst:
    print(f"{hoeveelheid}x {item.capitalize()}")