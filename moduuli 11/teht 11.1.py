class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi} Päätoimittaja: {self.päätoimittaja}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi} Kirjoittaja: {self.kirjoittaja} Sivumäärä: {self.sivumäärä}")

def main():
    lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    lehti1.tulosta_tiedot()
    kirja1.tulosta_tiedot()

if __name__ == "__main__":
    main()