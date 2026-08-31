import random

while True:
    noppa1 = random.randint(1,3)
    noppa2 = random.randint(1,3)
    if noppa1 == 3:
        if noppa2 == 3:
            print("Nyt tuli 3 ja 3, lopetetaan")
            break
    else:
        print(f"Nyt tuli {noppa1} ja {noppa2}, jatketaan")