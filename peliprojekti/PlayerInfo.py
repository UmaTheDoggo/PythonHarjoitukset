class Player:
    def __init__(self, name, HP=100, inventory=None):
        self.name = name
        self.HP = HP
        self.inventory = inventory if inventory is not None else []

        self.weapon = None
        self.hat_color = None
        self.jacket_color = None
        self.jeans_color = None

    def choose_weapon(self, wpn):
        self.weapon = wpn
        print(f"Weapon set to: {self.weapon.name}")

    def set_hat_color(self, color):
        self.hat_color = color

    def set_jacket_color(self, color):
        self.jacket_color = color

    def set_jeans_color(self, color):
        self.jeans_color = color