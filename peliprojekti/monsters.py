class Monster:
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def take_damage(self, amount):
        self.HP -= amount
        print(f"{self.name} took damage, it has {self.HP} of health left")
        self.HitDetect()

    def HitDetect(self):
        if self.HP <= 0:
            print(f"{self.name} backed down.")
            return True
        return False