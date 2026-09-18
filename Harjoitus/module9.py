# Module 9 class, object and constructor

class Hero:
    sankarien_määrä = 0

    def __init__(self, nimi, tyyppi, voima, aseaani, huudahdus="Hei!"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.voima = voima
        self.huudahdus = huudahdus
        self.aseaani = aseaani
        Hero.sankarien_määrä = Hero.sankarien_määrä + 1

    def huuda(self, kerrat=1):
        for i in range(kerrat):
            print(f"{self.huudahdus}")


    def ase(self):
        print(self.aseaani)

    

hero1 = Hero("Reinhardt", "Tankki", "Voimakas", "BONK", "AAAAARGH")
hero2 = Hero("Tracer", "DPS", "Nopea", "Bäng")
hero3 = Hero("Mercy", "Tukija", "Parannus", "viuh")

print(f"{hero1.nimi} on {hero1.tyyppi} ja hän on {hero1.voima}, hän huutaa {hero1.huudahdus}")
print(f"{hero2.nimi} on {hero2.tyyppi} ja hän on {hero2.voima}, hän huutaa {hero2.huudahdus}")

hero1.huuda()
hero1.ase()

hero2.huuda(2)
hero2.ase()

print(f"Sankarien määrä joukkueessa: {Hero.sankarien_määrä}")



# class auto:
#     pass

# class opiskelija:
#     pass

# opiskelija1 = opiskelija()

# opiskelija1.nimi = "Jaakko"
# opiskelija1.syntymavuosi = "2006"
# opiskelija1.keskiarvo = 1

# print(f"{opiskelija1.nimi} syntyi vuonna {opiskelija1.syntymavuosi}")






# def laske_kahden_luvun_summa(luku1, luku2):
#     summa = luku1 + luku2
#     return summa

# yhteenlaskettu_summa = laske_kahden_luvun_summa(1, 2)

# print(f"summa: {yhteenlaskettu_summa}")

