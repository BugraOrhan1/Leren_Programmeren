# toPay = int(float(input('Bedrag te betalen: ')) * 100)  
# paid = int(float(input('Betaald bedrag: ')) * 100) 
# change = paid - toPay  

# coinValue = 500

# returned_coins = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, }
# while change > 0 and coinValue > 0:
#     nrCoins = change // coinValue  
#     if nrCoins > 0:
#         print(f'Retourneer maximaal {nrCoins} munten van {coinValue} cent!' )
#         nrCoinsReturned = int(input(f'Hoeveel munten van {coinValue} cent heb je teruggegeven? '))
#         change -= nrCoinsReturned * coinValue  
#         returned_coins[coinValue] += nrCoinsReturned
    
    
#     if coinValue == 500:
#         coinValue = 200
#     elif coinValue == 200:
#         coinValue = 100
#     elif coinValue == 100:
#         coinValue = 50
#     elif coinValue == 50:
#         coinValue = 20
#     elif coinValue == 20:
#         coinValue = 10
#     elif coinValue == 10:
#         coinValue = 5
#     elif coinValue == 5:
#         coinValue = 2
#     elif coinValue == 2:
#         coinValue = 1
#     elif coinValue == 1:
#         coinValue = 0
#     else:
#         coinValue = 0

# print("Overzicht van teruggegeven munten:")
# for value, count in returned_coins.items():
#     print(f"{count} munten van {value} cent/euro")

# if change > 0:
#     print('Wisselgeld niet teruggegeven: ', str(change) + ' centen/euro')
# else:
#     print('Klaar')



toPay = int(float(input('Bedrag te betalen: ')) * 100)  
paid = int(float(input('Betaald bedrag: ')) * 100) 
change = paid - toPay  

coinValue = 500 

returned_coins = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
while change > 0 and coinValue > 0:
    nrCoins = change // coinValue  
    if nrCoins > 0:
        print(f'Retourneer maximaal {nrCoins} munten van {coinValue / 100} euro!' )
        nrCoinsReturned = int(input(f'Hoeveel munten van {coinValue / 100} euro heb je teruggegeven? '))
        change -= nrCoinsReturned * coinValue  
        returned_coins[coinValue] += nrCoinsReturned
    
    if coinValue == 500:
        coinValue = 200
    elif coinValue == 200:
        coinValue = 100
    elif coinValue == 100:
        coinValue = 50
    elif coinValue == 50:
        coinValue = 20
    elif coinValue == 20:
        coinValue = 10
    elif coinValue == 10:
        coinValue = 5
    elif coinValue == 5:
        coinValue = 2
    elif coinValue == 2:
        coinValue = 1
    elif coinValue == 1:
        coinValue = 0
    else:
        coinValue = 0

print("Overzicht van teruggegeven munten:")
for value, count in returned_coins.items():
    print(f"{count} munten van {value / 100} euro")

if change > 0:
    print('Wisselgeld niet teruggegeven: ', str(change / 100) + ' euro')
else:
    print('Klaar')
