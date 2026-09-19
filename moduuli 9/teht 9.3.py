class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 2000

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.nopeus * tuntimaara

# main

autoni = Auto("ABC-123", 150)

autoni.kiihdytä(60)

print(f"Auton nopeus ennen ajoa: {autoni.nopeus} km/h")
print(f"Kuljettu matka ennen ajoa: {autoni.kuljettu_matka} km/h")

autoni.kulje(1.5)

print(f"Kuljettu matka 1.5 tunnin ajon jälkeen: {autoni.kuljettu_matka} km")