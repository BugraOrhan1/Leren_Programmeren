from test_lib import test, report


def rond_bedrag_af(origineel_bedrag):
    AFROND_CENTEN = 0.05
    return round(origineel_bedrag / AFROND_CENTEN) * AFROND_CENTEN


origineel_bedrag = 2.24
verwacht_afgerond_bedrag = 2.25
berekend_afgerond_bedrag = rond_bedrag_af(origineel_bedrag)
naam = f'test origineel bedrag: {origineel_bedrag}'
test(naam, verwacht_afgerond_bedrag, berekend_afgerond_bedrag)

origineel_bedrag = 13.01
verwacht_afgerond_bedrag = 13.00
berekend_afgerond_bedrag = rond_bedrag_af(origineel_bedrag)
naam = f'test origineel bedrag: {origineel_bedrag}'
test(naam, verwacht_afgerond_bedrag, berekend_afgerond_bedrag)

bedrag = float(input('bedrag?'))

result1 = round(bedrag*100/5)*5/100
result2 = rond_bedrag_af (bedrag)

print(result1)
print(result2)

report()
