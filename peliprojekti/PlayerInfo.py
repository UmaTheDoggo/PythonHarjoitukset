#Määritetään pelaajan nimi, ikä elämäpisteet, paljon vahinkoa tekee ja tavaraluettelo
class Player:
    def __init__(self, name, age, HP, deals, inventory=None):
        self.name = name
        self.age = age
        self.HP = HP
        self.deals = deals
        self.inventory = inventory if inventory is not None else []
        
    # pelaajan vahingon ottamismekanismi. Alhasin HP määrä on 0 ja aina kun pelaaja ottaa vahinkoa tulostetaan teksti
    def take_damage(self, amount):
        self.HP = max(0, self.HP - amount)
        print(f"{self.name} took damage. I have {self.HP} of health left \n")
        self.HitDetect()

    # Jos pelaajan HP on 0 tai alle. Tulostetaan "You lost"
    def HitDetect(self):
        if self.HP <= 0:
            self.HP = 0
            print(f"{self.name}: You lost.")
            return True
        return False