class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.monster = None

    def add_exit(self, direction, room):
        self.exits[direction] = room


#main luodaan kartta

level1Center = Room("Starting place", "I can go left or right")
level1Left = Room("Left from the starting place", "I can go forward") # GGoblin
level1Right = Room("Right from the starting place", "I can go forward") # GGoblin 

level2Center = Room("The Goblin master room", "I need to defeat the Goblin master") # Fight start
level2Left = Room("Treatment room", "Health upgrade laying on the ground") # Health upgrade +100 HP
level2Right = Room("An armory", "There is an anvil. I could sharpen my weapon") # Weapon upgrade +10 dmg

level1Center.add_exit("left", level1Left)
level1Center.add_exit("right", level1Right)

level1Left.add_exit("forward", level2Left) # GGoblin
level2Left.add_exit("right", level2Center)

level1Right.add_exit("forward", level2Right) #GGoblin
level2Right.add_exit("left", level2Center)

current_room = level1Center