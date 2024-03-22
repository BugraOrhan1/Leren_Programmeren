for uur in range(1, 25):
    if uur <= 12:
        uur_1 = 'AM'
        uur_2 = uur
    else :
        uur_1 = 'PM'
        uur_2 = uur - 12 
    print(f'{uur_2}:00 {uur_1}')

