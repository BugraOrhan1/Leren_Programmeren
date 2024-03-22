def vraag_naam_en_leeftijd():
    naam = input("Voer je naam in: ")
    leeftijd = input("Voer je leeftijd in: ")
    return {'name': naam, 'age': leeftijd}

aanroepen = vraag_naam_en_leeftijd()
print(aanroepen['name'], 'is' ,aanroepen['age'],'jaar')

