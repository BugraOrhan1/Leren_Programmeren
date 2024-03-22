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


vrachtwagen_rijbewijs = input("Heeft u een geldig Vrachtwagen rijbewijs? (J/N): ").strip().lower() == "j"
hoed = input("Heeft u een hoge hoed? (J/N): ").strip().lower() == "j"
gewicht = int(input("Wat is uw lichaamsgewicht in kg? "))
lengte = int(input("Wat is uw lengte in cm? "))
gevaarlijk_certificaat = input("Heeft u het Certificaat 'Overleven met gevaarlijk personeel'? (J/N): ").strip().lower() == "j"
dieren_ervaring = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
jongleren_ervaring = int(input("Hoeveel jaar ervaring heeft u met jongleren? "))
acrobatiek_ervaring = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))

geschikt = (vrachtwagen_rijbewijs and hoed and gewicht > MIN_GEWICHT and gewicht < MAX_GEWICHT and
    lengte > MIN_LENGTE and lengte < MAX_LENGTE and gevaarlijk_certificaat and
    (dieren_ervaring >= MIN_DIEREN_ERVARING or
     jongleren_ervaring >= MIN_JONGLEREN_ERVARING or
     acrobatiek_ervaring >= MIN_ACROBATIEK_ERVARING))


if geschikt:
    print("U bent geschikt voor de positie van circusdirecteur!")
else:
    print("U voldoet niet aan alle criteria en bent niet geschikt voor de positie van circusdirecteur.")


