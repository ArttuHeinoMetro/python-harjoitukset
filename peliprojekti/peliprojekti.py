import random

kalapaikat = ["Joki", "Järvi", "Meri"]

nimi = input("Kerro Nimesi: ")
ika = int(input("Kerro Ikäsi: "))

print(nimi)
print(ika)
print("")
print("Tervetuloa Arskan Peliin!")
print("")


#Käyttäjän tiedot ja "päävalikko"

while ika >= 12:
    komento = input("Anna komento:\n")
    if komento == "info":
        print(nimi)
        print(ika)
        print()
    elif komento == "lopeta":
        break
    elif komento == "random":
        print(random.randint(1,100))
        print()
    elif komento == "aloita":
        print("Aloitetaan peli!")
        break
if ika < 12:
    print("Alaikäinen käyttäjä havaittu!")

#Kalastusluvan osto
def lupa(vastaus):
    if vastaus == "y":
        return "Viisas valinta!"
    else:
        return "Riskivalinta!"

print(lupa(input("Ostatko kalastusluvan seikkailullesi?(y/n)\n")))
print()

#kalastuspaikan valinta

def paikkavalinta(valinta):
    if valinta == "Joki":
        return "Joki on rauhallinen paikka missä voit rentoutua juoksevan veden äärellä"
    elif valinta == "Järvi":
        return "Järviä on Suomessa kaikkialla! Löydät varmasti mieluisan"
    elif valinta == "Meri":
        return "Merestä voit saada todella suuria kaloja!"
    else:
        return "Virhe"

print(f"Tässä lista eri kalapaikoista:\n {kalapaikat}")
print()
print(paikkavalinta(input("Minkä paikan valitset?\n")))
