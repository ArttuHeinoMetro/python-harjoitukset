lista = []
while True:
    luku = input("Anna kokonaisluku:\n")
    if luku == "":
        break

    lista.append(int(luku))

def f():
    summa = sum(lista)
    return summa


print(f())
