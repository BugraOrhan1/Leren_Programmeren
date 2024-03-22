def is_even_getal(getal: int) -> bool:
    return getal % 2 == 0

def omgekeerde_woorden(woord:str) -> str:
    woorden = woord.split()
    omgekeert = woorden[::-1]
    omgekeerde_woord = ' '.join(omgekeert)
    return omgekeerde_woord

def unieke_karakters(tekst: str) -> int:
    unieke_set = set(tekst)
    aantal_karakters = len(unieke_set)
    return aantal_karakters

def gemiddelde_woordenlengte(zin: str) -> float:
    woorden = zin.split()
    
    totale_lengte = 0
    for woord in woorden:
        totale_lengte += len(woord)

    gemiddelde_lengte = totale_lengte / len(woorden)
    return gemiddelde_lengte

def print_tafel(gewenste_tafel: int, aantal_som: int = 10) -> None:
    for teller in range(1, aantal_som + 1):
        totaal = teller * gewenste_tafel
        print(f'{teller} x {gewenste_tafel} = {totaal}')


print_tafel(10,10)