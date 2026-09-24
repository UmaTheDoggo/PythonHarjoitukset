class Monster:
    def __init__(self, name, HP, deals):
        self.name = name
        self.HP = HP
        self.deals = deals

    def take_damage(self, amount):
        self.HP -= amount
        print(f"{self.name} took damage, it has {self.HP} of health left")
        self.HitDetect()

    def deal_damage(self, amount):
        self.deals = amount
        print(f"{self.name} dealt {self.deals} of damage.")
        self.HitDeal()

    def HitDetect(self):
        if self.HP <= 0:
            print(f"{self.name} backed down.")
            return True
        return False