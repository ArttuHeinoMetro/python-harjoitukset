luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    alkuluku = False
else:
    alkuluku = True

    for jakojaannos in range(2, luku):
        if luku % jakojaannos == 0:
            alkuluku = False
            break

if alkuluku == True:
    print("Lukusi on alkuluku")
else:
    print("Lukusi ei ole alkuluku")