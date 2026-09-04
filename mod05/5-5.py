oikeakayttaja = "python"
oikeasala = "rules"

arvaukset = 1

while arvaukset <= 5:
    kayttajaveikkaus = input("Anna käyttäjätunnus: ")
    salaveikkaus = input("Anna salasana: ")
    if kayttajaveikkaus == oikeakayttaja:
        if salaveikkaus == oikeasala:
            print("Tervetuloa!")
            break
    elif arvaukset > 4:
        print("Pääsy evätty!!!")
        break
    elif kayttajaveikkaus != oikeakayttaja:
        if salaveikkaus != oikeasala:
            print("Väärä salasana tai käyttäjätunnus, yritä uudelleen")
    arvaukset +=1