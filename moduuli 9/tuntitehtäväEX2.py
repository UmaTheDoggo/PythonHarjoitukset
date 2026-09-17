class Merirosvolaiva:

    def __init__(self, nimi, tykit, miehistö, kulta=0):
        self.nimi = nimi
        self.tykit = tykit
        self.miehistö = miehistö
        self.kulta = kulta

    def loyda_aarre(self, maara):
        self.kulta = self.kulta + maara

    def meneta_kultaa(self, maara):
        self.kulta = self.kulta - maara

        if self.kulta < 0:
            self.kulta = 0


# pääohjelma
laiva1 = Merirosvolaiva("The Black Pearl", 12, 40)

laiva1.loyda_aarre(200)
laiva1.loyda_aarre(75)
laiva1.meneta_kultaa(100)


print(f"Nimi: {laiva1.nimi}\nTykit: {laiva1.tykit}\nMiehistö: {laiva1.miehistö}\nKulta: {laiva1.kulta}")