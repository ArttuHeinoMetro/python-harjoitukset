import random

summa = 0

maara = int(input("Anna noppien määrä:\n"))

for x in range(maara):
    luku = random.randint(1,6)
    summa += luku

print(f"Noppien summa on: {summa}")