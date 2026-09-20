import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntia):
        self.kuljettu_matka += self.nopeus * tuntia


# Luodaan 10 autoa
autot = []

for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


# Kisa
while True:

    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)

    for auto in autot:
        auto.kulje(1)

    # Tarkistetaan, onko joku auto saavuttanut 10000 km
    kilpailu_loppui = False

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_loppui = True
            break

    if kilpailu_loppui:
        break


# Tulostetaan tulokset taulukkona
print(f"{'Rekisteritunnus':<18}{'Huippunopeus':<15}"
      f"{'Nopeus':<10}{'Kuljettu matka':<15}")

for auto in autot:
    print(f"{auto.rekisteritunnus:<18}"
          f"{auto.huippunopeus:<15}"
          f"{auto.nopeus:<10}"
          f"{auto.kuljettu_matka:<15.1f}")