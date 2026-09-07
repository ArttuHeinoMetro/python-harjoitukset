import random

maksimi = int(input("Anna nopan tahkojen määrä:\n"))

def f(tahkot):
    return random.randint(1, tahkot)

while True:
    luku = f(maksimi)
    print(luku)
    

    if luku == maksimi:
        break