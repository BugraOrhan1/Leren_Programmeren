def vraag_naam_en_leeftijd():
    naam = input("Voer je naam in: ")
    leeftijd = input("Voer je leeftijd in: ")
    woonplaats = input("Voer je woonplaats in: ")
    return {'name': naam, 'age': leeftijd, 'woonplaats': woonplaats}

def verzamel_gegevens():
    gegevens = []
    while True:
        antwoord = input("Toets enter om door te gaan of stop om te printen: ")
        if antwoord.lower() == 'stop':
            break
        gegevens.append(vraag_naam_en_leeftijd())
    return gegevens

gegevenslijst = verzamel_gegevens()

for gegevens in gegevenslijst:
    print(gegevens['name'],'die in',gegevens['woonplaats'],'woont', 'is', gegevens['age'], 'jaar')
    print('in',gegevens['woonplaats'],'woont de',gegevens['age'],'jarige',gegevens['naam'])