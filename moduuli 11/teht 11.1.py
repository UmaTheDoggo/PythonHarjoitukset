class Kirja:
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumäärä}")

class Lehti:
    def __init__(self, nimi, päätoimittaja, sivumäärä):
        self.nimi = nimi
        self.päätoimittaja = päätoimittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}, Päätoimittaja: {self.päätoimittaja}, Sivumäärä: {self.sivumäärä}")
        

# main
julkaisut = []
kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
julkaisut.append(kirja1)

lehti1 = Lehti("Aku Ankka", "Aki Hyyppä", 30)
julkaisut.append(lehti1)

for t in julkaisut:
    t.tulosta_tiedot()