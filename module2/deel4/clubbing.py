PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30
prijs = 0
bandje= 0
stempel= False
DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

print('welkom')
age = int(input('hoe oud? '))

if age < 18:
    print ('sorry je mag niet naar binnen')
    x = 18 - age + 2024
    print(f'probeer het in {x} jaar nog eens')
    # einde
else:
    naam = input('wat is je naam?  ')
    if naam in VIP_LIST:
        if age >= 21:
            bandje = 'blauw'
        
        else:
            bandje= 'rood'   
        print(f'je krijgt van mij een{bandje}bandje')
    else:
        if age >= 21:
            print('je krijgt van mij een stempel')
            stempel= True
    drinken= input('wat wil je drinken?  ')

    if drinken == 'cola' :
        prijs += PRIJS_COLA
        if bandje == 'rood' or bandje == 'blauw':
            print('alstublieft,complimenten van het huis ')
        else:
            print(f'alsjeblieft je {drinken}, dat is dan{prijs}')
            #einde
    elif drinken == 'bier':
        prijs += PRIJS_COLA
        if bandje == 'rood' or bandje == 'blauw' or stempel == True:
            if bandje == 'rood' or bandje == 'blauw':
                    print('alstublieft,complimenten van het huis ')
                    #einde
        else:
            print('sorry je mag geen alcohol bestellen onder de 21')
            x = 18 - age + 2024
            print(f'probeer het in {x} jaar nog eens')
            #einde
    elif drinken == 'champagne':
        prijs += PRIJS_CHAMPAGNE
        if bandje == 'rood' or bandje == 'blauw':
            if bandje == 'blauw':
                print(f'alsjeblieft je {drinken}, dat is dan{prijs}')
                #einde
            else:
                print('sorry je mag geen alcohol bestellen onder de 21')
                x = 18 - age + 2024
                print(f'probeer het in {x} jaar nog eens')
                #einde

        else:
            print('sorry alleen vips mogen champagne bestellen')
            #einde
    else:
        print('sorry geen idee wat je bedoeld, hier een glaasje water')
        #einde

        

            
        
        
