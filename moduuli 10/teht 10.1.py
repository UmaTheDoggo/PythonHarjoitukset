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

#MAIN

if __name__ == "__main__":
    hissi1 = Hissi(5, 1)

    hissi1.SiirryKerrokseen(5)
    hissi1.SiirryKerrokseen(1)