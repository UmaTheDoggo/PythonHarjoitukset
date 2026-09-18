class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.matka = matka


#main
auto1 = Auto("ABC-123", "142km/h")
print(f"Rekisteritunnus: {auto1.rekisteritunnus}\n Huippunopeus: {auto1.huippunopeus}\n Nopeus nyt: {auto1.nopeus_nyt}\n Matka: {auto1.matka}")