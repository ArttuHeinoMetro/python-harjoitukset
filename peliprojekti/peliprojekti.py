import random

nimi = input("Kerro Nimesi: ")
ika = int(input("Kerro Ikäsi: "))

print(nimi)
print(ika)
print("")
print("Tervetuloa Arskan Peliin!")
print("")

while ika >= 12:
    komento = input("Anna komento:\n")
    if komento == "info":
        print(nimi)
        print(ika)
    elif komento == "lopeta":
        break
    elif komento == "random":
        print(random.randint(1,100))
if ika < 12:
    print("Alaikäinen käyttäjä havaittu!")