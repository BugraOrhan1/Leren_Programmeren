import math
def delen(x,y):
    gedeelt_getal = x/y
    return gedeelt_getal


def eerste_uitlijst(getallen):
    eerste_getal = getallen[0]
    return eerste_getal

def min_fun(x,y):
    min_getal=abs(x-y)
    return min_getal
def tel_elementen(getallen):   
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer

def check_deelbaar (unieke_getallen,controlegetal):
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)
    return deelbaar1

def posities_fun(controlegetal,getallen):
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal:
            posities.append(index)
def afwijking(gemiddelde,getallen,aantal):
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking