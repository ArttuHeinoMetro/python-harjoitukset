class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivut):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivut = sivut

    def tulosta(self):
        print(f"Nimi: {self.nimi}")
        print(f"Kirjailija: {self.kirjailija}")
        print(f"Sivut: {self.sivut}")
        print("")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta(self):
        print(f"Nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.päätoimittaja}")
        print("")


l1 = Lehti("Aku Ankka", "Aki Hyyppä")
k1 = Kirja("Nytti no.6", "Rosa Liksom", 200)

l1.tulosta()
k1.tulosta()