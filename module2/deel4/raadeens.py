import random

geheim_getal = random.randint(1, 1000)
score = 0 

rondes = int(input('Hoeveel rondes wil je spelen? '))
while rondes > 20:
    print("Sorry, het aantal rondes mag niet hoger zijn dan 20.")
    rondes = int(input('Hoeveel rondes wil je spelen? '))

for _ in range(rondes):
    for _ in range(10):
        antwoord = int(input('Antwoord: '))
        if geheim_getal == antwoord:
            score += 1
            print('Goed!')
            break
        elif 20 < abs(geheim_getal - antwoord) < 50:
            print('Heet')
        elif abs(geheim_getal - antwoord) < 20:
            print('Heel heet')
        else:
            print('Fout')
    print(f'je hebt zo veel punten {score}')
    door_stop = input('wil je door of stopen ')
    if door_stop == 'door':
        pass
    else:
        break
print('Einde van het spel.')
print(f'je hebt zo veel punten {score}')