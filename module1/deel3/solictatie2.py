print('********************************************************************')
print('* er worden u een aantal relevante vragen gesteld                  *')
print('* gelieve die naar eer en geweten in te vullen                     *')
print('* als blijkt dat u aan de criteria voldoet dan komt                *')
print('* u in aan merking voor een serieus sollicitattiegesprek           *')
print('* ontspan maar blijf wakker, hier komen de vragen                  *')
print('********************************************************************')

MIN_GEWICHT = 90
MAX_GEWICHT = 120
MIN_LENGTE = 150
MAX_LENGTE = 220
MIN_DIEREN_ERVARING = 4
MIN_JONGLEREN_ERVARING = 5
MIN_ACROBATIEK_ERVARING = 3
snor = 0
haarlengte = 0
glimlach = 0

geslacht = input("Wat is uw geslacht? (Man/Vrouw): ").strip().lower()
gewicht = int(input("Wat is uw lichaamsgewicht in kg? "))
lengte = int(input("Wat is uw lengte in cm? "))
ondernemers_diploma = input("Heeft u een Diploma MBO-4 ondernemen? (J/N): ").strip().lower() == "j"
ondernemer = input("Bent u al meer dan 3 jaar ondernemer met minimaal 5 werknemers in loondienst? (J/N): ").strip().lower() == "j"
gevaarlijk_certificaat = input("Heeft u het Certificaat 'Overleven met gevaarlijk personeel'? (J/N): ").strip().lower() == "j"
dieren_ervaring = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
jongleren_ervaring = int(input("Hoeveel jaar ervaring heeft u met jongleren? "))
acrobatiek_ervaring = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))

if geslacht == "man":
    snor = int(input("Hoe breed is uw snor in cm? "))
elif geslacht == "vrouw":
    haarlengte = int(input("Hoe lang is uw rode krulhaar in cm? "))
else:
    glimlach = int(input("Hoe breed is uw glimlach in cm? "))


bizarre_criteria = []

if not (ondernemers_diploma or ondernemer):
    bizarre_criteria.append("U voldoet niet aan de ondernemerscriteria.")

if geslacht == "man" and snor <= 10:
    bizarre_criteria.append("Uw snor is niet breed genoeg.")
elif geslacht == "vrouw" and haarlengte <= 20:
    bizarre_criteria.append("Uw krulhaar is niet lang genoeg.")
elif glimlach <= 10:
    bizarre_criteria.append("Uw glimlach is niet breed genoeg.")

standaard_criteria = ( gewicht > MIN_GEWICHT and gewicht < MAX_GEWICHT and
    lengte > MIN_LENGTE and lengte < MAX_LENGTE and gevaarlijk_certificaat and
    (dieren_ervaring >= MIN_DIEREN_ERVARING or
     jongleren_ervaring >= MIN_JONGLEREN_ERVARING or
     acrobatiek_ervaring >= MIN_ACROBATIEK_ERVARING))


geschikt = standaard_criteria and (ondernemers_diploma or ondernemer) and (snor > 10 or haarlengte > 20 or glimlach > 10)


if geschikt:
    print("U bent geschikt voor de positie van circusdirecteur!")
else:
    print("U voldoet niet aan alle criteria en bent niet geschikt voor de positie van circusdirecteur.")
    print("Redenen voor afwijzing:")
    for criteria in bizarre_criteria:
        print(criteria)
