sukupuoli = input("Kerro biologinen sukupuolesi (M/N):\n")
arvo = int(input("Kerro hemoglobiini arvosi (g/l):\n"))

if sukupuoli == "M":
    if arvo < 134:
        print("Alhainen hemoglobiini")
    elif 134 <= arvo <=195:
        print("Normaali hemoglobiini")
    elif arvo > 195:
        print("Korkea hemoglobiini")
elif sukupuoli == "N":
    if arvo < 117:
            print("Alhainen hemoglobiini")
    elif 117 <= arvo <=175:
            print("Normaali hemoglobiini")
    elif arvo > 175:
            print("Korkea hemoglobiini")
else:
      print("VIRHE!VIRHE!VIRHE!")