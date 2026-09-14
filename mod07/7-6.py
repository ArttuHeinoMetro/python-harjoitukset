import math

def f(halkaisija, hinta):
    sade = halkaisija / 2
    pintaalacm2 = math.pi * sade ** 2
    pintaalam2 = pintaalacm2 / 10000

    return hinta / pintaalam2


halkaisiija1 = float(input("Anna ensimmäisen pizzan halkaisija:\n"))
hinta1 = float(input("Anna ensimmäisen pizzan hinta:\n"))

halkaisiija2 = float(input("Anna toisen pizzan halkaisija:\n"))
hinta2 = float(input("Anna toisen pizzan hinta:\n"))

worth1 = f(halkaisiija1, hinta1)
worth2 = f(halkaisiija2, hinta2)

print(f"Ensimmäinen pizza maksaa {worth1:.2f}€/m²")
print(f"Toinen pizza maksaa {worth2:.2f}€/m²")

if worth1 < worth2:
    print("Ensimmäinen pizza on kannattavampi")
elif worth2 < worth1:
    print("Toinen pizza on kannattavampi")
else:
    print("Pizzat ovat yhtä kannattavia")