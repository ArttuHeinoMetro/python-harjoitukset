lista = []

print("Anna viiden eri kaupungin nimet niin tulostan ne oikeassa järjestyksessä")
print("")

for x in range(5):
    kaupunki = input("Anna kaupungin nimi:\n")
    lista.append(kaupunki)

print("")
for kaupunki in lista:
    print(kaupunki)