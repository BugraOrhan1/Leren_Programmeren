from fruitmand2 import fruitmand

kleur_vertaling = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'brown': 'bruin',
    'pink': 'roos'
    }

langste_naam_fruit = max(fruitmand, key=lambda fruit: len(fruit['name']))

kleur = kleur_vertaling.get(langste_naam_fruit['color'],langste_naam_fruit['color'])

gewicht_in_kg = langste_naam_fruit['weight'] / 1000

print(f"Kleur: {kleur.capitalize()}, Gewicht: {gewicht_in_kg:.3f} kg, Naam: {langste_naam_fruit['name'].capitalize()}")
