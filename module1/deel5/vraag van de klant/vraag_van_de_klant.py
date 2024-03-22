import random
import time 
from funtie_vraag_van_de_klant import *


if __name__ == "__main__":
    Gebruikersnaam = input('GebruikersID: ')

    gebruiker_aanval = 80
    gebruiker_verdediging = 40
    gebruiker_energie = stats_()
    gebruiker_gezondheid = stats_()
    gebruiker_snelheid = stats_()

    bazen = [
        {"naam": "Golem", "aanval": 40, "verdediging": 16, "energie": 56, "gezondheid": 300, "snelheid": 45},
        {"naam": "Draak", "aanval": 30, "verdediging": 12, "energie": 80, "gezondheid": 250, "snelheid": 60},
        {"naam": "Geest", "aanval": 20, "verdediging": 8, "energie": 120, "gezondheid": 200, "snelheid": 80},
        {"naam": "aap", "aanval": 15, "verdediging": 8, "energie": 120, "gezondheid": 200, "snelheid": 80},
    ]
    gekozen_baas = random.choice(bazen)
    print('--------------------------------------------------')
    time.sleep(1)
    print('-           Welkom in het Land van Avonturen      -')
    time.sleep(1)
    print('- Jij bevindt je alleen in een schilderachtig    -')
    time.sleep(1)
    print('- huis, verscholen in het hart van een betoverend -')
    time.sleep(1)
    print('- bos. Verveling overvalt je en je voelt dat het -')
    time.sleep(1)
    print('- tijd is voor een opwindend avontuur. Het doel  -')
    time.sleep(1)
    print('- is om je krachten te vergroten en te overleven -')
    time.sleep(1)
    print('--------------------------------------------------')
    time.sleep(1)
    print('')

    
    toon_stats(Gebruikersnaam, gebruiker_aanval, gebruiker_verdediging, gebruiker_energie, gebruiker_gezondheid, gebruiker_snelheid)

    print('-----------------------------------------------------------------------------')
    print('- Je denkt na of je naar de meest nabije stad gaat of dieper het bos in. -')
    print('-----------------------------------------------------------------------------')
    eerste_stap = input('Wat doe je? (bos/stad): ')


    if 'bos' in eerste_stap.lower():
        print('---------------------------------------------------------')
        print('Je loopt het bos in')
        print('---------------------------------------------------------')
        print('')

        
        tweede_stap = input ('Je ziet iets glimmends in de struik liggen. Wil je het oppakken? (ja/nee): ')
        if 'ja' in tweede_stap.lower():
            item = open_kist()
            if item == 'aanval':
                gebruiker_aanval += 20
            elif item == 'gezondheid':
                gebruiker_gezondheid += 30
            elif item == 'mimic':
                gebruiker_gezondheid -= 50
        else:
            print('Je laat een zwaard liggen in de struik.')
    

        derde_stap = input('Je ziet een oude brug. Wil je er overheen gaan? (ja/nee): ')
        if 'ja' in derde_stap.lower():
            item = vind_schat()
            if item == 'energie':
                gebruiker_energie += 30
            elif item == 'snelheid':
                gebruiker_snelheid += 10
        else:
            print('Je vermijdt de brug en gaat een andere richting op.')

        vierde_stap = input('In de verte zie je een kampvuur. Wil je ernaartoe gaan? (ja/nee): ')
        if 'ja' in vierde_stap.lower():
            item = ontmoet_reiziger()
            if item == 'gezondheid':
                gebruiker_gezondheid += 20
        else:
            print('Je besluit niet naar het kampvuur te gaan.')

        vijfde_stap = input('Je komt bij een splitsing in het pad. Kies je voor het linker- of rechterpad? (links/rechts): ')
        if 'links' in vijfde_stap.lower():
            item = zoek_verlaten_hut()
            if item == 'energie':
                gebruiker_energie += 20
        else:
            print('Je besluit het rechterpad te nemen.')

        zesde_stap = input('Je hoort een geluid achter een grote rots. Ga je kijken? (ja/nee): ')
        if 'ja' in zesde_stap.lower():
            item = red_verwond_dier()
            if item == 'gezondheid':
                gebruiker_gezondheid += 15
        else:
            print('Je besluit door te lopen.')

        zevende_stap = input('Je bereikt een dorp en ziet een smid. Wil je zijn winkel bezoeken? (ja/nee): ')
        if 'ja' in zevende_stap.lower():
            item = daag_dorpsbewoner_uit()
            if item == 'aanval':
                gebruiker_aanval += 15
        else:
            print('Je besluit het dorp te verlaten.')

        achtste_stap = input('Onderweg kom je een mysterieuze vreemdeling tegen. Hij biedt je een ruil aan. Accepteer je? (ja/nee): ')
        if 'ja' in achtste_stap.lower():
            item = vind_schat()
            if item == 'snelheid':
                gebruiker_snelheid += 15
        else:
            print('Je bedankt de vreemdeling en gaat verder.')

        negende_stap = input('Je ziet een betoverende fontein. Durf je ervan te drinken? (ja/nee): ')
        if 'ja' in negende_stap.lower():
            print('De magische fontein geeft je nieuwe energie. Je energie is volledig hersteld.')
            gebruiker_energie = 100
        else:
            print('Je besluit de fontein niet te gebruiken.')
        tiende_stap = input('wil je gebruik maken van de altar(ja/nee)')
        if 'ja' in tiende_stap.lower():
            print('Je offert iets aan het altaar en voelt een vreemde kracht om je heen.')
        keuze = input('Kies een attribuut om te versterken (aanval/verdediging/energie/gezondheid/snelheid): ')
    
        if keuze.lower() == 'aanval':
                gebruiker_aanval += 10
        elif keuze.lower() == 'verdediging':
            gebruiker_verdediging += 10
        elif keuze.lower() == 'energie':
            gebruiker_energie += 20
        elif keuze.lower() == 'gezondheid':
            gebruiker_gezondheid += 20
        elif keuze.lower() == 'snelheid':
            gebruiker_snelheid += 5
        else:
            print('Ongeldige keuze. Geen attributen zijn versterkt.')

        gekozen_baas = random.choice(bazen)
        
        print('--------------------------------------------------')
        print(f'Statistieken {gekozen_baas["naam"]}             -')
        print('-                                                -')
        toon_stats(gekozen_baas["naam"], gekozen_baas["aanval"], gekozen_baas["verdediging"],
                   gekozen_baas["energie"], gekozen_baas["gezondheid"], gekozen_baas["snelheid"])
        toon_stats(Gebruikersnaam, gebruiker_aanval, gebruiker_verdediging, gebruiker_energie, gebruiker_gezondheid, gebruiker_snelheid)


        aanval_keuze = input('Aanvallen of negeren: ')
        if "aanvallen" in aanval_keuze.lower():
            print('--------------------------------------------------------------')
            gevecht_gebruiker_tegen_baas(gebruiker_aanval, gebruiker_verdediging, gebruiker_gezondheid,gekozen_baas["aanval"], gekozen_baas["verdediging"], gekozen_baas["gezondheid"], gekozen_baas["naam"])

        else:
            print('je dacht slim te zijn maar je bent als nog gepakt door een boss')
            print('--------------------------------------------------------------')
            toon_stats(gekozen_baas["naam"], gekozen_baas["aanval"], gekozen_baas["verdediging"],gekozen_baas["energie"], gekozen_baas["gezondheid"], gekozen_baas["snelheid"])
            toon_stats(Gebruikersnaam, gebruiker_aanval, gebruiker_verdediging, gebruiker_energie, gebruiker_gezondheid, gebruiker_snelheid)
            gevecht_gebruiker_tegen_baas(gebruiker_aanval, gebruiker_verdediging, gebruiker_gezondheid,
                                         gekozen_baas["aanval"], gekozen_baas["verdediging"], gekozen_baas["gezondheid"], gekozen_baas["naam"])
        print('Gefeliciteerd! Je avontuur eindigt hier. Hier zijn je eindstatistieken:')
        toon_stats(Gebruikersnaam, gebruiker_aanval, gebruiker_verdediging, gebruiker_energie, gebruiker_gezondheid, gebruiker_snelheid)
        print('-----------------------')

        print(f'Dankjewel voor het spelen, {Gebruikersnaam}! Je hebt gewonnen!')   
    else :
        print('bange rik je kies het makkelijk manier  ')
        print('bange rik je kies het makkelijk manier  ')
        print('je dacht slim te zijn maar je bent als nog gepakt door een boss')
        print('--------------------------------------------------------------')
        toon_stats(gekozen_baas["naam"], gekozen_baas["aanval"], gekozen_baas["verdediging"],gekozen_baas["energie"], gekozen_baas["gezondheid"], gekozen_baas["snelheid"])
        toon_stats(Gebruikersnaam, gebruiker_aanval, gebruiker_verdediging, gebruiker_energie, gebruiker_gezondheid, gebruiker_snelheid)
        gevecht_gebruiker_tegen_baas(gebruiker_aanval, gebruiker_verdediging, gebruiker_gezondheid,gekozen_baas["aanval"], gekozen_baas["verdediging"], gekozen_baas["gezondheid"], gekozen_baas["naam"])
        print('Gefeliciteerd! Je avontuur eindigt hier. Hier zijn je eindstatistieken:')
        toon_stats(Gebruikersnaam, gebruiker_aanval, gebruiker_verdediging, gebruiker_energie, gebruiker_gezondheid, gebruiker_snelheid)
        print('-----------------------') 
            
        
