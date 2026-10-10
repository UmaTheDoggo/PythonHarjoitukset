# luodaan satunnainen lyömismekanismi
import random
# luodaan luokka ase, jolla ominaisuudet nimi, vahinko, osumanumero ja staattinen numero mihin asti arvotaan lukuja
class Weapon:
    def __init__(self, name, damage, hit_number, hit_scale=6):
        self.name = name
        self.damage = damage
        self.hit_number = hit_number
        self.hit_scale = hit_scale

    # arvotaan luku 1 - 6 satunnaisesti ja jos luku on pienempi tai yhtäsuuri kuin asetettu osumanumero niin ase onnistuu tekemään vahinkoa
    def attack(self):
        roll = random.randint(1, self.hit_scale)
        return roll <= self.hit_number