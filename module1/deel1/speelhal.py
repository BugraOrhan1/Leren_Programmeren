aantal_personen = 4

PRIJS_PER_TICKET = 7.45

speel_tijd = 45

MIN_5 = 0.37

A = 5 

totale_kosten = aantal_personen * PRIJS_PER_TICKET


vip_kosten = (speel_tijd / A) * aantal_personen * MIN_5

totale_kosten = totale_kosten + vip_kosten
x = round(totale_kosten, 2)

print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {speel_tijd} minuten VR kost je maar {x} euro')


