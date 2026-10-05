import os
import random
from time import sleep
import json


#funktiot
import os

def lue_tiedosto(tiedostonimi):
    polku = os.path.join(os.path.dirname(os.path.abspath(__file__)), tiedostonimi)

    with open(polku, "r", encoding="utf-8") as tiedosto:
        return tiedosto.read()

def tallenna_peli(nimi, ika, luontopisteet, kalapisteet, kalojen_maara):
    polku = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "tallennus.txt"
    )

    with open(polku, "w", encoding="utf-8") as tiedosto:
        tiedosto.write(f"nimi={nimi}\n")
        tiedosto.write(f"ika={ika}\n")
        tiedosto.write(f"luontopisteet={luontopisteet}\n")
        tiedosto.write(f"kalapisteet={kalapisteet}\n")
        tiedosto.write(f"kalojen_maara={kalojen_maara}\n")

    print("Peli tallennettu!")

def lataa_peli():
    try:
        polku = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "tallennus.txt"
        )

        with open(polku, "r", encoding="utf-8") as tiedosto:
            tiedot = tiedosto.readlines()

        nimi = tiedot[0].strip().split("=")[1]
        ika = int(tiedot[1].strip().split("=")[1])
        luontopisteet = int(tiedot[2].strip().split("=")[1])
        kalapisteet = int(tiedot[3].strip().split("=")[1])
        kalojen_maara = int(tiedot[4].strip().split("=")[1])

        return nimi, ika, luontopisteet, kalapisteet, kalojen_maara

    except FileNotFoundError:
        return None

def roskatapahtuma():
    print("Heität syötin veteen ja odotat hetken...")
    print("Nyppäiset jotain vedestä!")
    print("Huomaat, että kyseessä ei ole kala vaan roskaa.")
    print()
    
    valinta = input("Vietkö roskan mukanasi pois vai heitätkö sen takaisin veteen? (pois/takaisin)\n")
    if valinta == "pois":
        print("Hienoa! Otat roskan mukaasi ja viet sen myöhemmin roskiin.")
        print("Kalastuspaikka pysyy siistimpänä. +3 Pistettä!")
        return 3
    elif valinta == "takaisin":
        print("Heität roskan takaisin veteen.")
        print("Kalastus jatkuu, mutta roska jää veteen.")
        return 0
    else:
        print("Et osannut päättää, joten nostat roskan rannalle.")
        print("Ehkä joku muu hoitaa sen myöhemmin.")
        return 1

def kalastus(pelaaja):
    print()
    print("KALASTUS")
    print("Kalastus alkaa!")
    print("Jokaisella kalastuskerralla voi tulla yksi kala.")
    print("Kirjoita 'lopeta', jos haluat lopettaa kalastamisen.")
    print()

    while True:
        komento = input(
            "Paina Enter kalastaaksesi tai kirjoita 'lopeta': "
        ).lower()

        if komento == "lopeta":
            print("Lopetat kalastamisen.")
            print(f"Pyydystit yhteensä {pelaaja.kalojen_maara} kalaa.")
            print(f"Kalapisteesi: {pelaaja.kalapisteet}")
            break

        pelaaja.luontopisteet += roskatapahtuma()

        print()
        sleep(2)

        print("Heität uudelleen ja tunnet nykäisyn!")
        sleep(2)
        print("Kala tarttui koukkuun!")
        sleep(1)

        kalan_paino = random.randint(100, 2000)
        kalan_pisteet = kalan_paino

        pelaaja.kalojen_maara += 1
        pelaaja.kalapisteet += kalan_pisteet

        print(f"Sait {kalan_paino} gramman painoisen kalan!")
        print(f"Sait {kalan_pisteet} kalapistettä!")
        print()

        print(f"Kaloja yhteensä: {pelaaja.kalojen_maara}")
        print(f"Kalapisteitä yhteensä: {pelaaja.kalapisteet}")
        print(f"Luontopisteitä yhteensä: {pelaaja.luontopisteet}")

        tallenna_peli(
            pelaaja.nimi,
            pelaaja.ika,
            pelaaja.luontopisteet,
            pelaaja.kalapisteet,
            pelaaja.kalojen_maara
        )

def aloita_peli(pelaaja):
    print()
    print("PELI ALKAA")
    print(f"Tervetuloa seikkailuun, {pelaaja.nimi}!")
    print()
    sleep(2)

    # Kalastusluvan osto
    def lupa(vastaus):
        if vastaus == "y":
            return True
        else:
            return False

    on_lupa = lupa(input("Ostatko kalastusluvan seikkailullesi? (y/n)\n"))

    if on_lupa:
        print("Viisas valinta!")
    else:
        print("Riskivalinta!")

    print()
    sleep(2)

    # Kalastuspaikan valinta
    kalapaikat = ["Joki", "Järvi", "Meri"]

    print(f"Tässä lista eri kalapaikoista:\n{kalapaikat}")
    print()
    sleep(1)

    paikka = input("Minkä paikan valitset? (Joki/Järvi/Meri)\n")

    if paikka == "Joki":
        print("Joki on rauhallinen paikka, missä voit rentoutua juoksevan veden äärellä.")
    elif paikka == "Järvi":
        print("Järviä on Suomessa kaikkialla! Löydät varmasti mieluisan.")
    elif paikka == "Meri":
        print("Merestä voit saada todella suuria kaloja!")
    else:
        print("Tuntematon paikka. Valitaan Joki.")
        paikka = "Joki"

    print()
    sleep(2)

    # Onkivälineen valinta
    onki = Vapa("Onki")
    virveli = Vapa("Virveli")

    print("Valitse kalastusväline:")
    print("1 = Mato-onki")
    print("2 = Virveli")

    valine = input("Kumman valitset? (1/2)\n")

    if valine == "1":
        valine = "Onki"
        print("Valitsit mato-ongen.")
    elif valine == "2":
        valine = "Virveli"
        print("Valitsit virvelin.")
    else:
        print("Virheellinen valinta. Otetaan käyttöön mato-onki.")
        valine = "Onki"

    print()
    sleep(2)

    # Matka kalastuspaikalle
    print("Pakkaat varusteet mukaasi...")
    sleep(2)
    print("Lähdet matkaan kohti kalastuspaikkaa.")
    sleep(2)
    print(f"Saavut paikalle: {paikka}.")
    print()

    # Lupatarkastaja
    print("Kuulet painokkaan äänen takaatasi:")
    sleep(2)
    print('"Kalastuslupatarkastaja tässä, hyvää päivää."')
    sleep(2)
    print('"Mahtaako teillä olla lupa-asiat kunnossa?"')
    sleep(2)

    if pelaaja.ika < 18 or pelaaja.ika > 69:
        print(
            "Ilmoitat lupatarkastajalle olevasi oikeutettu "
            "ikään perustuvaan poikkeukseen kalastusluvasta."
        )
        print('"Aivan niin, en sitten häiritse enempää. Hyvää päivänjatkoa."')
        sleep(2)

    elif on_lupa:
        print(
            "Näytät lupatarkastajalle aikaisemmin ostamasi luvan. "
            "Hän kiittää ja jatkaa matkaansa."
        )
        sleep(2)

    elif valine == "Onki" and (paikka == "Järvi" or paikka == "Meri"):
        print(
            "Lähemmältä tarkastelulta lupatarkastaja huomaa, "
            "että kalastat vain mato-ongella."
        )
        print('"Eihän tässä ollutkaan mitään ongelmaa. Pahoittelut häiriöstä."')
        sleep(2)

    else:
        print("Nyt olet joutunut todella ikävään tilanteeseen.")
        print("Sinulla ei ole vaadittavia lupia kalastamiseen.")
        print(
            '"Kuules nyt! Sinulla ei ole vaadittavaa lupaa. '
            'Määrään sinut tästä hyvästä sakkoon."'
        )

    print()
    sleep(2)

    # Viimeiset valmistelut
    print("Tarkistat vielä kalastusvälineesi.")
    sleep(2)
    print(f"Käytössäsi on: {valine}")
    print(f"Kalastuspaikkasi on: {paikka}")
    print()

    print("Kaikki on valmista.")
    sleep(2)

    kalastus(pelaaja)

# Luokat
class Pelaaja:
    def __init__(self, nimi, ika, luontopisteet, kalapisteet=0, kalojen_maara=0):
        self.nimi = nimi
        self.ika = ika
        self.luontopisteet = luontopisteet
        self.kalapisteet = kalapisteet
        self.kalojen_maara = kalojen_maara

class Esine:
    def __init__(self, nimi, ):
        self.nimi = nimi

class Vapa(Esine):
    def __init__(self, nimi):
        super().__init__(nimi)

print(lue_tiedosto("intro.txt"))
print("")
print(lue_tiedosto("ohjeet.txt"))
print("")

jatka = input("Onko sinulla tallennettu peli? (y/n)\n").lower()

if jatka == "y":
    peli = lataa_peli()

    if peli is not None:
        nimi, ika, luontopisteet, kalapisteet, kalojen_maara = peli

        pelaaja = Pelaaja(
        nimi,
        ika,
        luontopisteet,
        kalapisteet,
        kalojen_maara
    )

        print(f"Tervetuloa takaisin, {pelaaja.nimi}!")
        print(f"Luontopisteesi: {pelaaja.luontopisteet}")
        print(f"Kalapisteesi: {pelaaja.kalapisteet}")
        print(f"Kaloja pyydystetty: {pelaaja.kalojen_maara}")
    else:
        print("Tallennettua peliä ei löytynyt.")
        nimi = input("Kerro nimesi: ")
        ika = int(input("Kerro ikäsi: "))
        pelaaja = Pelaaja(nimi, ika, 0)

else:
    nimi = input("Kerro nimesi: ")
    ika = int(input("Kerro ikäsi: "))
    pelaaja = Pelaaja(nimi, ika, 0)


print(pelaaja.nimi)
print(pelaaja.ika)
print("")
print("Tervetuloa Arskan Peliin!")
print("")


# Käyttäjän tiedot ja "päävalikko"

while pelaaja.ika >= 12:
    komento = input(
        "Anna komento "
        "(Komennolla 'aloita' voit aloittaa pelin):\n"
    ).lower()

    if komento == "info":
        print(pelaaja.nimi)
        print(pelaaja.ika)
        print(f"Luontopisteet: {pelaaja.luontopisteet}")
        print(f"Kalapisteet: {pelaaja.kalapisteet}")
        print(f"Kaloja pyydystetty: {pelaaja.kalojen_maara}")
        print()

    elif komento == "lopeta":
        break

    elif komento == "random":
        print(random.randint(1, 100))
        print()

    elif komento == "tallenna":
        tallenna_peli(
            pelaaja.nimi,
            pelaaja.ika,
            pelaaja.luontopisteet,
            pelaaja.kalapisteet,
            pelaaja.kalojen_maara
        )

    elif komento == "aloita":
        aloita_peli(pelaaja)
        break

    else:
        print("Tuntematon komento.")
        print()