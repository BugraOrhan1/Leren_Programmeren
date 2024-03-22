pizza_small = 0
pizza_medium = 0 
pizza_large = 0
try:
    pizza_small = float(input('pizza_small?'))
except ValueError:
    print('je moet wel een getal invullen ')
try:
    pizza_medium = float(input('pizza_medium?'))
except ValueError:
    print('je moet wel een getal invullen ')
try:
    pizza_large = float(input('pizza_large?'))
except ValueError:
    print('je moet wel een getal invullen ')

PIZZA_SMALL_PRIJS = 699
PIZZA_MEDIUM_PRIJS = 799
PIZZA_LARGE_PRIJS = 1299 
CENT = 100

totaal_small = pizza_small * PIZZA_SMALL_PRIJS 
totaal_medium = pizza_medium * PIZZA_MEDIUM_PRIJS 
totaal_large = pizza_large * PIZZA_LARGE_PRIJS  
totaal = (totaal_large + totaal_medium + totaal_small)

print('----------------------------------------------------')
print(f'|u heeft {pizza_small} small pizza bestelt het kost{totaal_small/CENT}        ')         
print(f'|u heeft {pizza_medium} medium pizza bestelt het kost{totaal_medium/CENT}     ')        
print(f'|u heeft {pizza_large} large pizza bestelt het kost{totaal_large/CENT}        ')
print(f'|totaal kost het pizza{totaal/CENT}                                           ')
print('----------------------------------------------------')
