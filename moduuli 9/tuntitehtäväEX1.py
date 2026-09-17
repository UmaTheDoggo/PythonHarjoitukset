class Pelaaja:
    def __init__(self, nimi, elämät=3, kolikot=0, pisteet=0):
        self.nimi = nimi
        self.elämät = elämät
        self.kolikot = kolikot
        self.pisteet = pisteet

# pääohjelma
pelaaja1 = Pelaaja("Mario")

print(f"Nimi: {pelaaja1.nimi}\nElämät: {pelaaja1.elämät}\nKolikot: {pelaaja1.kolikot}\nPisteet: {pelaaja1.pisteet}")
