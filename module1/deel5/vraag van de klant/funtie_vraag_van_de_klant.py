import random
import time

def stats_():
    return random.randint(50, 100)

def toon_stats(entiteit_naam, aanval, verdediging, energie, gezondheid, snelheid):
    print('-----------------------------------------------')
    time.sleep(1)
    print(f'-               Statistieken {entiteit_naam}                     -')
    time.sleep(1)
    print('-                                             -')
    time.sleep(1)
    print(f'- Aanval: {aanval}                           -')
    time.sleep(1)
    print(f'- Verdediging: {verdediging}                 -')
    time.sleep(1)
    print(f'- Energie: {energie}                         -')
    time.sleep(1)
    print(f'- Gezondheid: {gezondheid}                   -')
    time.sleep(1)
    print(f'- Snelheid: {snelheid}                       -')
    time.sleep(1)
    print('-----------------------------------------------')
    time.sleep(1)
    print('')






def gevecht_gebruiker_tegen_baas(gebruiker_aanval, gebruiker_verdediging, gebruiker_gezondheid,
                                 baas_aanval, baas_verdediging, baas_gezondheid, baas_naam):

    while gebruiker_gezondheid > 0 and baas_gezondheid > 0:
        gebruiker_schade = max(0, gebruiker_aanval - baas_verdediging)
        baas_gezondheid -= gebruiker_schade
        baas_schade = max(0, baas_aanval - gebruiker_verdediging)
        gebruiker_gezondheid -= baas_schade

        print(f'Je doet {gebruiker_schade} schade aan {baas_naam}. De gezondheid van {baas_naam} is nu {max(0, baas_gezondheid)}.')
        time.sleep(1)
        print(f'{baas_naam} doet {baas_schade} schade. Jouw gezondheid is nu {max(0, gebruiker_gezondheid)}.')

        if baas_gezondheid <= 0:
            print(f'Gefeliciteerd! Je hebt {baas_naam} verslagen.')
            print('\n-----------------------')
            print('Gefeliciteerd! Je avontuur eindigt hier. Hier zijn je eindstatistieken:')
            print('-----------------------')
            break
        if gebruiker_gezondheid <= 0:
            print(f'Je bent verslagen door {baas_naam}. Het avontuur eindigt hier.')
            break


def open_kist():
    print('Je ziet een mysterieuze kist voor je.')
    keuze = input('Wil je de kist openen? (ja/nee): ')
    
    if keuze.lower() == 'ja':
        kans_op_item = random.randint(1, 10)  
        if kans_op_item == 1:
            print('Gefeliciteerd! Je hebt een krachtig zwaard gevonden. Je aanval neemt toe!')
            return 'aanval'
        elif kans_op_item <= 4:
            print('Je hebt een gezondheidsdrankje gevonden. Je gezondheid herstelt een beetje.')
            return 'gezondheid'
        elif kans_op_item == 5:
            print('er komt een mimic op je af ')
            return 'mimic'
        else:
            print('Helaas, de kist was leeg. Geen items gevonden.')
            return None
    else:
        print('Je besluit de kist niet te openen.')
        return None

def zoek_verlaten_hut():
    print('Je ontdekt een verlaten hut diep in het bos.')
    keuze = input('Wil je de hut verkennen? (ja/nee): ')
    
    if keuze.lower() == 'ja':
        kans_op_item = random.randint(1, 10)
        if kans_op_item == 1:
            print('Gefeliciteerd! Je hebt een oude toverstaf gevonden. Je energie neemt toe!')
            return 'energie'
        else:
            print('Helaas, de hut bevatte geen waardevolle items.')
            return None
    else:
        print('Je besluit de verlaten hut met rust te laten.')
        return None

def red_verwond_dier():
    print('Je hoort een zacht gekreun en ontdekt een gewond dier.')
    keuze = input('Wil je proberen het dier te helpen? (ja/nee): ')
    
    if keuze.lower() == 'ja':
        print('Dankbaar voor je hulp, geeft het dier je een mysterieuze drank. Je gezondheid herstelt.')
        return 'gezondheid'
    else:
        print('Je laat het gewonde dier met rust.')
        return None

def daag_dorpsbewoner_uit():
    print('Je komt een dorpsbewoner tegen die eruitziet alsof hij wil vechten.')
    keuze = input('Wil je de dorpsbewoner uitdagen voor een duel? (ja/nee): ')
    
    if keuze.lower() == 'ja':
        print('Je hebt een episch duel met de dorpsbewoner. Na de overwinning voel je je sterker.')
        return 'aanval'
    else:
        print('Je besluit het vreedzaam op te lossen en vermijdt het gevecht.')
        return None

def vind_schat():
    print('Je ontdekt een verborgen schat op de grond.')
    keuze = input('Wil je de schat openen? (ja/nee): ')
    
    if keuze.lower() == 'ja':
        kans_op_item = random.randint(1, 10)  # Kans op een item is 1 op 10
        if kans_op_item == 1:
            print('Gefeliciteerd! Je hebt een magische amulet gevonden. Je energie neemt toe!')
            return 'energie'
        elif kans_op_item <= 5:
            print('Je hebt een snelheidsdrank gevonden. Je snelheid neemt toe!')
            return 'snelheid'
        else:
            print('Helaas, de schat bevatte geen waardevolle items.')
            return None
    else:
        print('Je laat de schat onaangeroerd liggen.')
        return None

def ontmoet_reiziger():
    print('Je komt een vriendelijke reiziger tegen.')
    keuze = input('Wil je met de reiziger praten? (ja/nee): ')
    
    if keuze.lower() == 'ja':
        print('De reiziger geeft je een genezingskruid. Je gezondheid herstelt.')
        return 'gezondheid'
    else:
        print('Je besluit de reiziger met rust te laten.')
        return None


