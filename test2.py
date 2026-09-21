class Song:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title


class Playlist:
    def __init__(self):
        self.munlista = []

    def addsong(self, x):
        self.munlista.append(x)


s1 = Song("Iso Arska", "Anna olla viimenen kerta")
s2 = Song("Iso Arska", "Syö paskas")
s3 = Song("Iso Arska", "Sanoppa vielä")
s4 = Song("Iso Arska", "Jumalauta perkele")
s5 = Song("Iso Arska", "Se tuli nyt lähtö")
s6 = Song("Iso Arska", "Mä lähen Helsinkiin")

hittilista = [s1, s2, s3, s4, s5, s6]

#for item in hittilista:
#    print(f"{item.artist} - {item.title}")


for item in hittilista:
    Playlist.addsong(item)

for item in Playlist.munlista.biisi:
    print(f"{item.artist} - {item.title}")