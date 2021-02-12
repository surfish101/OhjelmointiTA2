# Kirjasto jossa on tietojen järkevyystarkistukseen soveltuvia funktioita

# 1. Poistetaan tekstistä ylimääräiset merkit, kuten välilyönnit alusta ja lopusta
# 2. Vaihdetaan vahingossa syötetyt desimaalipilkut (,) desimaalipisteiksi (.)
# 3. Määritellään järkevän arvon alaraja (pienin hyväksytty arvo)
# 4. Määritellään järkevän arvon yläraja (suurin hyväksytty arvo)

def tarkastaja(syote, alaraja, ylaraja):
    """
    Puhdistaa merkkijonosta ylimääräiset tulostumattomat merkit ja välilyönnit ja selvittää onko
    syötetty arvo annettujen rajojen sisällä. Funktio muuttaa desimaalipilkun desimaalipisteeksi.

    Args:
        syote (string): Näppäimistöltä syötetty arvo
        alaraja (float): Pienin sallittu arvo
        ylaraja (float): Suurin sallittu arvo
    """

    # Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = syote.lstrip()

    # Poistetaan whitespace merkit merkkijonon lopusta
    puhdistettu_syote  = puhdistettu_syote.rstrip()

    # Selviteteään onko merkkijonossa pilkku (,)
    pilkunpaikka = puhdistettu_syote.find(',')
    
    # Jos merkkijonosta löytyy pilkku (,) korvataan se pisteellä (.)
    if pilkunpaikka != -1:
        korjattu_syote = puhdistettu_syote.replace(',', '.')
    else:
        korjattu_syote = puhdistettu_syote

    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi
    try:
        luku = float(korjattu_syote)
    except:
        print('Syötetyssä tiedossa on ylimääräisiä merkkejä. Vain numerot sallittu')
        luku = 0

    # Tarkistetaan ettei syöte ole alle alarajan
    try:
        if luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)
    
    #Tarkistetaan ettei syöte ole yli ylärajan
    try:
        if luku > ylaraja:
            raise Exception('Syöttämäsi arvo on yli sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Palautetaan luku
    return luku


# Testataan toiminta
tulos = tarkastaja('sata', 1, 500)
print(tulos)