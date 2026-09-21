import random

class Weapon:
    def __init__(self, name, damage, hit_number, hit_scale=6):
        self.name = name
        self.damage = damage
        self.hit_number = hit_number
        self.hit_scale = hit_scale

    def attack(self):
        roll = random.randint(1, self.hit_scale)
        return roll <= self.hit_number