kuha = int(input("Kerro kuhan mitta senttimetreinä niin kerron onko se laillinen:\n"))

vajaa = 37 - kuha

if vajaa >=0:
    print(f"HEITÄ JÄRVEEN SENKIN SAAPAS. Kuhasi on {vajaa}cm liian pieni")
elif vajaa <0:
    print("Saat pitää kuhan!")