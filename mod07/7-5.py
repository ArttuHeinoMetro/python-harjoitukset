l1 = []

while True:
    print("Syötä kokonaislukuja niin karsin niistä parittommat pois")
    luku = input("Anna kokonaisluku:\n")
    if luku == "":
        break

    l1.append(int(luku))


def f(l1):
    l2 = []
    for item in l1:
        jaannos = item % 2
        if jaannos == 0:
            l2.append(item)
    return l2


print(f"Tässä karsittu lista{f(l1)}")
print(f"Tässä alkuperäinen lista{l1}")