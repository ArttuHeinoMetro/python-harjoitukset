import random
from time import sleep
#funktiot
def lue_tiedosto(tiedostonimi):
    with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
        return tiedosto.read()

def tallenna_peli(nimi, ika, luontopisteet):
    with open("tallennus.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(f"nimi={nimi}\n")
        tiedosto.write(f"ika={ika}\n")
        tiedosto.write(f"luontopisteet={luontopisteet}\n")

    print("Peli tallennettu!")

def lataa_peli():
    try:
        with open("tallennus.txt", "r", encoding="utf-8") as tiedosto:
            tiedot = tiedosto.readlines()

        nimi = tiedot[0].strip().split("=")[1]
        ika = int(tiedot[1].strip().split("=")[1])
        luontopisteet = int(tiedot[2].strip().split("=")[1])

        return nimi, ika, luontopisteet

    except FileNotFoundError:
        return None

class Pelaaja:
    def  __init__(self, nimi, ika, luontopisteet):
        self.nimi = nimi
        self.ika = ika
        self.luontopisteet = luontopisteet

class Esine:
    def __init__(self, nimi, ):
        self.nimi = nimi

class Vapa(Esine):
    def __init__(self, nimi):
        super().__init__(nimi)

kalapaikat = ["Joki", "Järvi", "Meri"]

print(lue_tiedosto("intro.txt"))
print("")
print(lue_tiedosto("ohjeet.txt"))
print("")

jatka = input("Onko sinulla tallennettu peli? (y/n)\n").lower()

if jatka == "y":
    peli = lataa_peli()

    if peli is not None:
        nimi, ika, luontopisteet = peli
        pelaaja = Pelaaja(nimi, ika, luontopisteet)

        print(f"Tervetuloa takaisin, {pelaaja.nimi}!")
        print(f"Luontopisteesi: {pelaaja.luontopisteet}")

    else:
        print("Tallennettua peliä ei löytynyt.")
        nimi = input("Kerro nimesi: ")
        ika = int(input("Kerro ikäsi: "))
        pelaaja = Pelaaja(nimi, ika, 0)

else:
    nimi = input("Kerro nimesi: ")
    ika = int(input("Kerro ikäsi: "))
    pelaaja = Pelaaja(nimi, ika, 0)
pelaaja = Pelaaja(nimi, ika, 0)

print(pelaaja.nimi)
print(pelaaja.ika)
print("")
print("Tervetuloa Arskan Peliin!")
print("")


# Käyttäjän tiedot ja "päävalikko"

while pelaaja.ika >= 12:
    komento = input("Anna komento(Komennolla 'aloita' voit aloittaa pelin):\n")
    if komento == "info":
        print(pelaaja.nimi)
        print(pelaaja.ika)
        print()
    elif komento == "lopeta":
        break
    elif komento == "random":
        print(random.randint(1,100))
        print()
    elif komento == "tallenna":
        tallenna_peli(pelaaja.nimi, pelaaja.ika, pelaaja.luontopisteet)
    elif komento == "aloita":
        print("Aloitetaan peli!")
        break
if pelaaja.ika < 12:
    print("Alaikäinen käyttäjä havaittu!")

# Kalastusluvan osto
def lupa(vastaus):
    if vastaus == "y":
        return True
    else:
        return False

on_lupa = lupa(input("Ostatko kalastusluvan seikkailullesi?(y/n)\n"))

if on_lupa:
    print("Viisas valinta!")
else:
    print("Riskivalinta!")

print()

#kalastuspaikan valinta

def paikkavalinta(valinta):
    if valinta == "Joki":
        paikkavalinta = "Joki"
        return "Joki on rauhallinen paikka missä voit rentoutua juoksevan veden äärellä"
    elif valinta == "Järvi":
        paikkavalinta = "Järvi"
        return "Järviä on Suomessa kaikkialla! Löydät varmasti mieluisan"
    elif valinta == "Meri":
        paikkavalinta = "Meri"
        return "Merestä voit saada todella suuria kaloja!"
    else:
        return "Virhe"

print(f"Tässä lista eri kalapaikoista:\n {kalapaikat}")
print()
sleep(2)
paikka = input("Minkä paikan valitset?\n")
print(paikkavalinta(paikka))
print("")

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
    print("Virheellinen valinta.")
    valine = "Onki"

print()

# Kalastuslupatarkastaja

print("Kuulet painokkaan äänen takaatasi:")
sleep(2)
print('"Kalastuslupatarkastaja tässä hyvää päivää, mahtaako teillä olla lupa-asiat kunnossa?"')
sleep(2)

if pelaaja.ika < 18 or pelaaja.ika > 69:
    print("Ilmoitat lupatarkastajalle olevasi oikeutettu ikään perustuvaan poikkeukseen kalastusluvasta")
    print('"Aivan niin, en sitten häiritse enempää. Hyvää päivänjatkoa."')
    print("")

elif on_lupa:
    print("Näytät lupatarkastajalle aikaisemmin ostamasi luvan, hän kiittää ja jatkaa matkaansa")
    print("")

elif valine == "Onki" and (paikka == "Järvi" or paikka == "Meri"):
    print("Lähemmältä tarkastelulta lupatarkastaja huomaa, että kalastat vain mato-ongella.")
    print('"Eihän tässä ollutkaan mitään ongelmaa. Pahoittelut häiriöstä."')
    print("")

else:
    print("Nyt olet joutunut todella ikävään tilanteeseen.")
    print("Sinulla ei ole vaadittavia lupia kalastamiseen.")
    print('"Kuules nyt! Sinulla ei ole vaadittavaa lupaa. Määrään sinut tästä hyvästä sakkoon."')
    print("")

# Roskan löytyminen vedestä

def roskatapahtuma():
    print("Heität ongen veteen ja odotat hetken...")
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


pelaaja.luontopisteet += roskatapahtuma()

print()
print(f"Luontopisteesi: {pelaaja.luontopisteet}")