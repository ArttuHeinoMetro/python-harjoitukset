import random

def f():
    return random.randint(1,6)

while True:
    luku = f()
    print(luku)

    if luku == 6:
        break