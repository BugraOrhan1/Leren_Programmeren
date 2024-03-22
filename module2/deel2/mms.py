# import random

# kleuren = ('oranje', 'blauw', 'groen', 'bruin')
# zak = []
# aantal_mms = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))
# for x in range(aantal_mms):
#     zak.append(random.choice(kleuren))

# print("Inhoud van de zak met M&M's:",zak)

import random

kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']
zak = {}

aantal_mms = int(input("Hoeveel m&m's wil je aan de zak toevoegen? "))

for _ in range(aantal_mms):
    kleur = random.choice(kleuren)
    zak[kleur] = zak.get(kleur, 0) + 1 #het returnt waarde met het op gegeven key 
    if kleur in zak :
        zak[kleur] += 1
    else:
        zak[kleur] = 1
        






print("Inhoud van de zak met m&m's:")
for kleur, aantal in zak.items(): #kleur is het sleutel
    print(f"{kleur}: {aantal}") #elke kleur en het bijbehorende aantal M&M's afgedrukt.





# met het waarde