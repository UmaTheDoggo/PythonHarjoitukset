class Player:
    def __init__(self, name, age, HP, deals, inventory=None):
        self.name = name
        self.age = age
        self.HP = HP
        self.deals = deals
        self.inventory = inventory if inventory is not None else []

        #self.weapon = None

    def choose_weapon(self, wpn):
        self.weapon = wpn
        print(f"Weapon set to: {self.weapon.name}")

    def take_damage(self, amount):
        self.HP = max(0, self.HP - amount)
        print(f"{self.name} took damage. I have {self.HP} of health left \n")
        self.HitDetect()

    def HitDetect(self):
        if self.HP <= 0:
            self.HP = 0
            print(f"{self.name}: You lost.")
            return True
        return False