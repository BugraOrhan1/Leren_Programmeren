from fruitmand2 import fruitmand

fruitmand.sort(key=lambda fruit: fruit['weight'], reverse=True)

for fruit in fruitmand:
    gewicht_in_kg = fruit['weight'] / 1000  
    print(f"{fruit['name']}: {gewicht_in_kg:.3f} kg")
