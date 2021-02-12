# Tuodaan käyttöön modulin sanitycheck.py toiminnot
import sanitycheck

# Funktio painoindeksin (body mass index) laskemiseksi
def bmi(paino, pituus):
    painoindeksi = paino / pituus**2
    return painoindeksi


# Funktio kehon rasvaprosentin laskemiseksi
def rasvaprosentti(bmi, ika, sukupuoli):
    rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    return rprosentti


# Kysytään käyttäjältä tarvittavat tiedot, huom näppäimistöstä saadaan aina merkkijono (string)
paino_str = input('Anna painosi kilogrammoina: ')
paino = sanitycheck.tarkastaja(paino_str, 20, 500)
pituus_str = input('Anna pituutesi metreinä: ')
pituus = sanitycheck.tarkastaja(pituus_str, 1, 3)
ika_str = input('Anna ikäsi: ')
ika = sanitycheck.tarkastaja(ika_str, 10, 150)
sukupuoli_str = input('Paina 1 jos olet mies, 0 jos olet nainen: ')
sukupuoli = sanitycheck.tarkastaja(sukupuoli_str, -1, 2)


# Muutetaan merkkijono luvuiksi
# Muuttuja, johon tallentuu tieto virheen tapahtumisesta alustus: False
tapahtui_virhe = False

# Virheenkäsittelyrutiini
try:
    # Tutkitaan onko merkkijonossa aakkosia ja annetaan tyyppivirhe jos on
    if paino_str.isalpha():
        raise TypeError('Vain numerot (0..9) ja desimaalipiste(.) on sallittu')

    # Jos ei ole virhettä, muutetaan liukuluvuksi
    paino = float(paino_str)

# Jos tapahtui virhe, tulostetaan virheilmoitusteksti ja asetetaan virhemuuttujan arvoksi True
except Exception as virhe:
    print(virhe)
    tapahtui_virhe = True

try:
    if pituus_str.isalpha():
        raise TypeError('Vain numerot (0..9) ja desimaalipiste(.) on sallittu')
    pituus = float(pituus_str)
except Exception as virhe:
    print(virhe)
    tapahtui_virhe = True

try:
    if ika_str.isalpha():
        raise TypeError('Vain numerot (0..9) ja desimaalipiste(.) on sallittu')
    ika = float(ika_str)
except Exception as virhe:
    print(virhe)
    tapahtui_virhe = True

try:
    if sukupuoli_str.isalpha():
        raise TypeError('Vain numerot (0..9) ja desimaalipiste(.) on sallittu')
    sukupuoli = float(sukupuoli_str)
except Exception as virhe:
    print(virhe)
    tapahtui_virhe = True

if tapahtui_virhe == False:
    painoindeksi = bmi(paino, pituus)
    print('Painoindeksisi on:', painoindeksi)
    rprosentti = rasvaprosentti(painoindeksi, ika, sukupuoli)
    print('Kehosi rasvaprosentti on:', rprosentti)
else:
    print('Ei voitu laskea sillä tiedot olivat virheellisiä')