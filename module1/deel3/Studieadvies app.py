from studieadviestext import *
print(STUDIEDOKTER_TITEL)
AANTAL_WEKEN_antwoord =int(input('Hoeveel weken ben je al bezig met de opleiding?'))

competentie_stelling_1_antwoord = 0
competentie_stelling_2_antwoord = 0
competentie_stelling_3_antwoord = 0
competentie_stelling_4_antwoord = 0
competentie_stelling_5_antwoord = 0
competentie_stelling_6_antwoord = 0 
competentie_stelling_7_antwoord = 0

altijd = 0
vaak = 0
regelmatig = 0 

print(COMPETENTIE_STELLING_1)
print(OPTIES)
competentie_stelling_1_antwoord = int(input())
if competentie_stelling_1_antwoord == 0:
    altijd += 1
if competentie_stelling_1_antwoord == 1:
    vaak += 1
if competentie_stelling_1_antwoord == 2:
    regelmatig += 1
print(COMPETENTIE_STELLING_2)
print(OPTIES)
competentie_stelling_2_antwoord = int(input())
if competentie_stelling_2_antwoord == 0:
    altijd += 1
if competentie_stelling_2_antwoord == 1:
    vaak += 1
if competentie_stelling_2_antwoord == 2:
    regelmatig += 1
print(COMPETENTIE_STELLING_3)
print(OPTIES)
competentie_stelling_3_antwoord = int(input())
if competentie_stelling_3_antwoord == 0:
    altijd += 1
if competentie_stelling_3_antwoord == 1:
    vaak += 1
if competentie_stelling_3_antwoord == 2:
    regelmatig += 1
print(COMPETENTIE_STELLING_4)
print(OPTIES)
competentie_stelling_4_antwoord = int(input())
if competentie_stelling_4_antwoord == 0:
    altijd += 1
if competentie_stelling_4_antwoord == 1:
    vaak += 1
if competentie_stelling_4_antwoord == 2:
    regelmatig += 1
print(COMPETENTIE_STELLING_5)
print(OPTIES)
competentie_stelling_5_antwoord = int(input())
if competentie_stelling_5_antwoord == 0:
    altijd += 1
if competentie_stelling_5_antwoord == 1:
    vaak += 1
if competentie_stelling_5_antwoord == 2:
    regelmatig += 1

if AANTAL_WEKEN_antwoord >=10 :
    print(COMPETENTIE_STELLING_6)
    print(OPTIES)
    competentie_stelling_6_antwoord = int(input())
    if competentie_stelling_6_antwoord == 0:
        altijd += 1
    if competentie_stelling_6_antwoord == 1:
        vaak += 1
    if competentie_stelling_6_antwoord == 2:
        regelmatig += 1
    print(COMPETENTIE_STELLING_7)
    print(OPTIES)
    competentie_stelling_7_antwoord = int(input())
    if competentie_stelling_7_antwoord == 0:
        altijd += 1
    if competentie_stelling_7_antwoord == 1:
        vaak += 1
    if competentie_stelling_7_antwoord == 2:
        regelmatig += 1

totaal_stellingen = competentie_stelling_1_antwoord + competentie_stelling_2_antwoord + competentie_stelling_3_antwoord + competentie_stelling_4_antwoord + competentie_stelling_5_antwoord + competentie_stelling_6_antwoord + competentie_stelling_7_antwoord
VRAGEN = 7
if AANTAL_WEKEN_antwoord <= 10:
    VRAGEN - 2

gemidelde = totaal_stellingen/VRAGEN
altijd_vaak = altijd + vaak
altijd_vaak_regelmatig = altijd + vaak + regelmatig 
if gemidelde <= 2 or altijd_vaak <= 2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
if gemidelde <= 3 or altijd_vaak_regelmatig <= 3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
if gemidelde == 4 :
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)

