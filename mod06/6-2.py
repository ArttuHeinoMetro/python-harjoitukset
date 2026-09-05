lukulista = []

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break

    lukulista.append(int(luku))

lukulista.sort(reverse=True)

print("Viisi suurinta lukua:")

for luku in lukulista[:5]:
    print(luku)