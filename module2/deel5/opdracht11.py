from fruitmand2 import fruitmand

beschikbare_kleuren = {fruit['color'] for fruit in fruitmand}

while True:
    gekozen_kleur = input("Kies een kleur uit de beschikbare kleuren van de fruitmand: ").lower()
    if gekozen_kleur in beschikbare_kleuren:
        break
    else:
        print(f"De kleur {gekozen_kleur} zit niet in de fruitmand. Probeer opnieuw.")

# aantal_ronde_vruchten = sum(1 for fruit in fruitmand if fruit['color'] == gekozen_kleur and fruit['round'])
aantal_rond = 0
for fruit in fruitmand:
    if fruit['color'] == gekozen_kleur and fruit['round']:
        aantal_rond += 1
# aantal_niet_ronde_vruchten = sum(1 for fruit in fruitmand if fruit['color'] == gekozen_kleur and not fruit['round'])
aantal_niet_rond = 0
for fruit in fruitmand:
    if fruit['color'] == gekozen_kleur and not fruit['round']:
        aantal_niet_rond += 1

verschil = aantal_rond - aantal_niet_rond

if verschil > 0:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
elif verschil < 0:
    print(f"Er zijn {-verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
else:
    print(f"Er zijn evenveel ronde als niet ronde vruchten in de kleur {gekozen_kleur}")
