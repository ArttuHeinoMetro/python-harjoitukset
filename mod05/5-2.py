tuuma =int(input("Anna mitta tuumina niin muutan sen senteiksi:\n"))

while tuuma > 0:
    print(f"Antamasi mitta on {tuuma * 2.54}cm")
    tuuma = int(input("Anna uusi mitta: \n"))
    if tuuma < 0:
        break