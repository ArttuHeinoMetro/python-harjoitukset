vuosi = int(input("Anna vuosiluku niin kerron onko se karkausvuosi:\n"))

if vuosi % 400 == 0:
    print(f"Antamasi vuosi {vuosi} on karkausvuosi")
elif vuosi % 100 == 0:
    print(f"Antamasi vuosi {vuosi} ei ole karkausvuosi")
elif vuosi % 4 == 0:
    print(f"Antamasi vuosi {vuosi} on karkausvuosi") 
else:
    print(f"Antamasi vuosi {vuosi} ei ole karkausvuosi")