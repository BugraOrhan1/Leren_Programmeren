# import random

# kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']

# waarden = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']

# jokers = ['joker'] * 2

# deck = [(kleur, waarde) for kleur in kleuren for waarde in waarden] + [(None, joker) for joker in jokers]
# random.shuffle(deck) 

# hand = deck[:7]

# deck = deck[7:]

# print("Bovenste 7 kaarten:")

# for i, kaart in enumerate(hand, 1):
#     print(f'Kaart {i}: {kaart[1]} van {kaart[0] if kaart[0] else "joker"}')

# print("\nOverige kaarten in het deck:")

# overige_kaarten = tuple((f"{kaart[1]} van {kaart[0] if kaart[0] else 'joker'}" for kaart in deck))

# print(overige_kaarten)

import random

kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
waarden = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
jokers = ['joker'] * 2

deck = []
for kleur in kleuren:
    for waarde in waarden:
        deck.append((kleur, waarde))

for joker in jokers:
    deck.append((None, joker))

random.shuffle(deck)

hand = deck[:7]
deck = deck[7:]

print("Jouw beginhand:")
for i, kaart in enumerate(hand, 1):
    print(f'Kaart {i}: {kaart[1]} van {kaart[0] if kaart[0] else "joker"}')

print("\nOverige kaarten in het deck:")
overige_kaarten = []
for kaart in deck:
    overige_kaarten.append(f"{kaart[1]} van {kaart[0] if kaart[0] else 'joker'}")

print(overige_kaarten)





