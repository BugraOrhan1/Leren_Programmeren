pizza_small = int(input('pizza_small?'))
pizza_medium = int(input('pizza_medium?'))
pizza_large = int(input('pizza_large?'))

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
