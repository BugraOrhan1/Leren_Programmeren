import math
from test_lib import test, report

def bereken_cilinder_inhoud(diameter, hoogte):
    # if diameter <= 0 or hoogte <= 0:
    #     return 0.0  
    straal = diameter / 2
    inhoud = math.pi * straal * straal * hoogte
    afgeronde_inhoud = round(inhoud, 1)
    return afgeronde_inhoud


diameter = 8.0
hoogte = 5.0
verwachte_inhoud = 251.3
berekende_inhoud = bereken_cilinder_inhoud(diameter, hoogte)
naam = f'test diameter: {diameter} hoogte: {hoogte}'
test(naam, verwachte_inhoud, berekende_inhoud)

diameter = 11.0
hoogte = 7.0
verwachte_inhoud = 665.2
berekende_inhoud = bereken_cilinder_inhoud(diameter, hoogte)
naam = f'test diameter: {diameter} hoogte: {hoogte}'
test(naam, verwachte_inhoud, berekende_inhoud)

diameter = 18.0
hoogte = 7.0
verwachte_inhoud = 1781.3
berekende_inhoud = bereken_cilinder_inhoud(diameter, hoogte)
naam = f'test diameter: {diameter} hoogte: {hoogte}'
test(naam, verwachte_inhoud, berekende_inhoud)

diameter = 15.0
hoogte = 2.0
verwachte_inhoud = 353.4
berekende_inhoud = bereken_cilinder_inhoud(diameter, hoogte)
naam = f'test diameter: {diameter} hoogte: {hoogte}'
test(naam, verwachte_inhoud, berekende_inhoud)

diameter = 0.0
hoogte = 6.0
verwachte_inhoud = 0.0
berekende_inhoud = bereken_cilinder_inhoud(diameter, hoogte)
naam = f'test diameter: {diameter} hoogte: {hoogte}'
test(naam, verwachte_inhoud, berekende_inhoud)


report()
