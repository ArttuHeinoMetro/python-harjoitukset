luvut = []

while True:
    luku = input("Syötä lukuja haluamasi määrä ja lopuksi anna tyhjä syöte niin kerron suurimman ja pienimmän: ")
    if luku == "":
        break
    luvut.append(int(luku))

print(f"Pienin luku: {min(luvut)}")
print(f"Suurin luku: {max(luvut)}")