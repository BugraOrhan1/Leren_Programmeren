CENT = 100
croissantjes = int(input ('croissantjes?')) 
croissantjes_prijs_euro = float(input('croissantjes prijs?'))
croissantjes_prijs_cent = int(croissantjes_prijs_euro * CENT)
stokbroden =  int(input ('stokbroden?')) 
STOKBRODEN_PRIJS = 78
kortingsbonnen = int(input ('kortingsbonnen?')) 
KORTINGSBONNEN_PRIJS = 50


bedrag = croissantjes * croissantjes_prijs_cent + stokbroden * STOKBRODEN_PRIJS - kortingsbonnen   * KORTINGSBONNEN_PRIJS
bedrag_1 = bedrag / CENT


print (f'De feestlunch kost je bij de bakker {bedrag_1} euro voor de {croissantjes} croissantjes en de {stokbroden} stokbroden als de {kortingsbonnen } kortingsbonnen nog geldig zijn!')