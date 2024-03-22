from fruitmand import fruitmand

fruitmand.append({
    'name': 'watermeloen',
    'weight': 7000,  
    'color': 'green',
    'round': True
})

# gewicht = sum(fruit['weight'] for fruit in fruitmand)

# print("Gewicht van de volledige fruitmand:", gewicht)



x = 0
for fruit in fruitmand:
    x += fruit['weight']


print (x)