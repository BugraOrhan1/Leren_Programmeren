som = []
getal = 50
totaal = 50

while totaal <= 1000:
    som.append(getal)
    getal += 1
    totaal = totaal + getal
    print('+'.join(str(x) for x in som) + '=' + str(totaal))
