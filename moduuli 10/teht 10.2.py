class Hissi:
    def __init__(self, ylin, alin):
        self.ylin = ylin
        self.alin = alin
        self.kerros_nyt = alin

    def SiirryYlös (self):
        if self.kerros_nyt < self.ylin:
            self.kerros_nyt += 1
            print(f"Olet nyt kerroksessa: {self.kerros_nyt}")
        else: print("Olet ylimmässä kerroksessa.")

    def SiirryAlas (self):
        if self.kerros_nyt > self.alin:
            self.kerros_nyt -= 1
            print(f"Olet nyt kerroksessa: {self.kerros_nyt}")
        else: print("Olet alimmassa kerroksessa.")

    def SiirryKerrokseen (self, kohde):
        if kohde > self.ylin or kohde < self.alin:
            print("Kerrosta ei ole")
            return

        print(f"Siirrytään kerrokseen {kohde}")
        while self.kerros_nyt < kohde:
            self.SiirryYlös()
        while self.kerros_nyt > kohde:
            self.SiirryAlas()

class Talo:
    def __init__(self, alin, ylin, hissi_määrä):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissi_määrä):
            uusi_hissi = Hissi(alin=1, ylin=5)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"Hissi numero {hissin_numero} Kerrokseen {kohde_kerros}: ")
            valittu_hissi = self.hissit[hissin_numero - 1]
            valittu_hissi.SiirryKerrokseen(kohde_kerros)
        else:
            print(f"Virhe: hissiä {hissin_numero} ei löydy.")



#MAIN

if __name__ == "__main__":
    hissi1 = Hissi(5, 1)
    talo1 = Talo(1, 5, 2)

    talo1.aja_hissiä(1, 5)
