from test_lib import test, report

maand_kortingsmerken = 'Vespa,Kymco,Yamaha'
MAAND_KORTINGSPERCENTAGE = 0.10

def bereken_korting(prijs: float, merk: str, maand_kortingsmerken: str) -> float:
    kortingsmerken = maand_kortingsmerken.split(',')
    
    if merk in kortingsmerken:
        berekende_korting = int(round((prijs * MAAND_KORTINGSPERCENTAGE), 2))
        return berekende_korting
    else:
        return 0.0
    
expected = 90
calculated = bereken_korting(900, 'Vespa' , maand_kortingsmerken)
test('vespa', expected, calculated)

expected = 90
calculated = bereken_korting(900, 'Kymco' , maand_kortingsmerken)
test('kymco', expected, calculated)

expected = 90
calculated = bereken_korting(900, 'Yamaha' , maand_kortingsmerken)
test('yamaha', expected, calculated)

expected = 0.0
calculated = bereken_korting(900, 'riva' , maand_kortingsmerken)
test('random', expected, calculated)

expected = 0.0
calculated = bereken_korting(900, 'zip' , maand_kortingsmerken)
test('random_1', expected, calculated)








report()
