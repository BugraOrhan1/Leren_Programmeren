from test_lib import test, report




def vergelijk_getallen(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return 'Beide getallen zijn even groot'
    elif nr1 > nr2:
        return (f'Maximum: {nr1} en minimum: {nr2}')
    return (f'Maximum: {nr2} en minimum: {nr1}')
    

expected = f'Maximum: 9 en minimum: 6'
calculated = vergelijk_getallen(9, 6)
test('vergelijk1', expected, calculated)


expected = 'Beide getallen zijn even groot'
calculated = vergelijk_getallen(6, 6)
test('vergelijk2', expected, calculated)

expected = f'Maximum: 9 en minimum: 6'
calculated = vergelijk_getallen(6, 9)
test('vergelijk2', expected, calculated)

report()