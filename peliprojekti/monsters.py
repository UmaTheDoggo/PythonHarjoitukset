# luodaan monsteri luokka, jolle ominaisuudet nimi, elämäpisteet ja paljon vahinkoa tekee (nämä arvot luodaan TheDungeon.py tiedostossa)
class Monster:
    def __init__(self, name, HP, deals):
        self.name = name
        self.HP = HP
        self.deals = deals

    # määritetään vahingon ottamis mekaniikka, pienin mahdollinen elämä on 0
    def take_damage(self, amount):
        self.HP = max(0, self.HP - amount)
        print(f"{self.name} took damage, it has {self.HP} of health left\n")
        self.HitDetect()

    # määritetään vahingon teko pelaajaan "amount" määritetään TheDungeon.py tiedostossa hirviön luomisen yhteydessä
    def deal_damage(self, amount):
        self.deals = amount
        print(f"{self.name} dealt {self.deals} of damage.")
        
    # jos hirviön elämä on 0 tai menee sen alle niin tulostetaan teksti muuten palautetaan arvo false ja silmukka jatkuu
    def HitDetect(self):
        if self.HP <= 0:
            print(f"{self.name} backed down.\n")
            return True
        return False