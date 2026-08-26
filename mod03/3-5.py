print("Anna leiviskät.")
leiv=float(input())
print()
print("Anna naulat.")
naul=float(input())
print()
print("Anna luodit.")
luod=float(input())

g = leiv * 20 * 32 * 13.3
g += naul * 32 * 13.3
g += luod * 13.3

kg = int(g // 1000)
loputg = g % 1000

print()
print("Massa nykymittojen mukaan:")
print(f"{kg} kilogrammaa ja {loputg:.2f} grammaa.")