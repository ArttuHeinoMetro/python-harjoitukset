import random

oikea = random.randint(1,10)

print("Anna luku 1-10 väliltä niin kerron onko se korkeampi vai matalampi kun oikea luku")

while True:
    veikkaus = int(input("Anna luku: \n"))
    if veikkaus > oikea:
        print("Liian suuri arvaus")
    elif veikkaus < oikea:
        print("Liian pieni arvaus")
    else:
        print("OIKEIN!!!")
        break