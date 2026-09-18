class Ope:
    def __init__(self, nimi):
        self.nimi = nimi
    def mun_stu(self, opis):
        print(f"Nimeni on {self.nimi} ja {opis.nimi} on mun opiskelija")


class Opiskelija:
    def __init__(self, nimi):
        self.nimi = nimi


op1 = Ope("James")
op2 = Ope("Mr. Bean")
opis1 = Opiskelija("Superman")
opis2 = Opiskelija("Batman")



#op1.mun_stu(opis1)
#op2.mun_stu(opis2)




class Author:
    def __init__(self, name):
        self.name = name

a1 = Author("Anna")
a2 = Author("Mikko")
a3 = Author("Liisa")
a4 = Author("Minä")

class Book:
    def __init__(self, title, x):
        self.title = title
        self.author = x.name

b1 = Book("Lasten satukirja", a1)
b2 = Book("Velhojen seikkailu", a2)
b3 = Book("Romanttinen romanssi", a3)
b4 = Book("Joku huono kirja", a4)

#print(f"{b1.title} - {b1.author}")
#print(f"{b2.title} - {b2.author}")
#print(f"{b3.title} - {b3.author}")
#print(f"{b4.title} - {b4.author}")


#print(b1.pages)
#print(b2.pages)
#print(b3.pages)
#print(b4.pages)








class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        print(f"{self.name} kävelee")

    def adult(self):
        if self.age >= 18:
            print(f"{self.name} on aikuinen")
        else:
            print(f"{self.name} ei ole aikuinen")

p1 = Person("James", 45)
p2 = Person("Matti", 30)
p3 = Person("Viivi", 15)

#p1.adult()
#p2.adult()
#p3.adult()








class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def piiri(self):
        piiri = self.height * 2 + self.width * 2
        return piiri


r1 = Rectangle(4, 5)#

#print(r1.piiri())







class Asukas:
    def __init__(self, nimi):
        self.nimi = nimi

asu1 = Asukas("Arska")
asu2 = Asukas("Joel")
asu3 = Asukas("Juho")

class Kaupunki:
    def __init__(self, asu):
        self.asu = asu


kau1 = Kaupunki(asu1)
kau2 = Kaupunki(asu2)
kau3 = Kaupunki(asu3)

l1 = [asu1, asu2, asu3]

#for i in l1:
#    print(i.nimi)



#kau1.kuka()
#kau2.kuka()






















class Tili:
    def __init__(self, saldo):
        self.saldo = saldo
    def talletus (self, summa):
        self.saldo += summa
    def nosto (self, summa):
        self.saldo -= summa


t1 = Tili(100)

t1.talletus(20)

t1.nosto(50)


t2 = Tili(200)

t2.talletus(50)

t2.nosto(20)

#print(t1.saldo)
#print(t2.saldo)





class Kirja:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirjasto:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kirjat = []
    def lisaa(self, kir):
        self.kirjat.append(kir.nimi)

k1 = Kirja("Maila")
k2 = Kirja("Tuntematon sotilat")
k3 = Kirja("Aakkoset")
k4 = Kirja("Raamattu")

kirjasto1 = Kirjasto("oodi")

kirjasto1.lisaa(k1)
print(kirjasto1.kirjat)