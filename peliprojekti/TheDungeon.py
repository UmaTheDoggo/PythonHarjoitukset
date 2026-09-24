import sys
import time
import custom
from weapons import Weapon
from monsters import Monster
from room import Room
from PlayerInfo import Player

#weapons and monsters
sword = Weapon("Sword", 5, 4)
axe = Weapon("Axe", 7, 3)

goblin = Monster("Goblin", 10, 5)
GGoblin = Monster("Giant Goblin", 50, 10)
MGoblin = Monster("Goblin Master", 100, 15)

#luodaan kartta
level0Start = Room("Fields", "A peaceful spot under a tree") # pelaajan aloitushuone ennen dungeoniin menemistä
level1Center = Room("Starting place", "I can go left or right")
level1Left = Room("Left from the starting place", "I can go forward") # GGoblin + syringe
level1Right = Room("Right from the starting place", "I can go forward") # GGoblin + smithing stone

level2Center = Room("The Goblin master room", "I need to defeat the Goblin master") # Fight start
level2Left = Room("Treatment room", "Health upgrade laying on the ground") # Health upgrade +100 HP
level2Right = Room("An armory", "There is an anvil. I could sharpen my weapon") # Weapon upgrade +10 dmg

level1Center.add_exit("left", level1Left)
level1Center.add_exit("right", level1Right)

level1Left.add_exit("forward", level2Left) # GGoblin + Syringe jolla otetaan health upgrade seuraavasta huoneesta
level2Left.add_exit("right", level2Center)

level1Right.add_exit("forward", level2Right) #GGoblin ja upgrade flint joka appendataan listaan, jolla päivitetään ase
level2Right.add_exit("left", level2Center)

current_room = level0Start

#dungeon monsters
level1Center.monster = goblin
level1Left.monster = GGoblin
level1Right.monster = GGoblin
level2Center.monster = MGoblin

#player
player_name = input("Enter your name: ")
player = Player(player_name, HP=100, inventory=[])

#player age
player_age = float(input("Enter your age: "))
if player_age < 12:
    sys.exit("This game is meant for people over the age of 12. Quitting game.")

print(" ")

#player info
player_info = print (f"Hello, {player_name}, Age: {player_age:.0f}")

while True:
    # time.sleep(1)

    print("""\
------------------------------------------------------------------------------------------------------------------------
__        __   _                            _          _____ _            ____                                     
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |_   _| |__   ___  |  _ \ _   _ _ __   __ _  ___  ___  _ __  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | | | '_ \ / _ \ | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | | | | | |  __/ | |_| | |_| | | | | (_| |  __/ (_) | | | |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    |_| |_| |_|\___| |____/ \__,_|_| |_|\__, |\___|\___/|_| |_|
                                                                                            |___/                  
------------------------------------------------------------------------------------------------------------------------
  | Start |     | Customise |     | Info |     | Quit |                                                                          

""")
    
    navigation = input("Type to navigate: ").lower()
    if navigation == "customise":
        player.hat_color = input("Enter a hat color: ").lower()
        player.jacket_color = input("Enter jacket color: ").lower()
        player.jeans_color = input("Enter jeans color: ").lower()

    if navigation == "info":
        print(f"Name: {player.name}, Age {player_age:.0f}")

        if player.hat_color is None:
            print("Color of hat not set")
        else:
             print(f"Color of hat: {player.hat_color}")

        if player.jacket_color is None:
            print("Color of jacket not set")
        else:
            print(f"Color of jacket: {player.jacket_color}")

        if player.jeans_color is None:
            print("Color of jeans not set")
        else:
             print(f"Color of jeans: {player.jeans_color}")
             
    if navigation == "quit":
        sys.exit("Quitting game...")

    if navigation == "start":
        break

if Player.set_hat_color is None:
    Player.hat_color = input("Choose the color of the hat: ").lower()
    Player.jacket_color = input("Choose the color of the jacket: ").lower()
    Player.jeans_color = input("Choose the color of the jeans: ").lower()

print("Stranger: Hey, you. You're finally awake! How are you feeling?")
print("| Good |     | Bad |")
answer1 = input(f"{player_name}: ").lower()
if answer1 == "good":
        print("Stranger: I highly doubt that. It's like you fell from the heavens.")
elif answer1 == "bad":
        print("Stranger: I figured. You just fell from the sky.")
else:
    print("Stranger: Hmm... Not quite sure if I understand. You took a bit of a fall.")

# time.sleep(2)
print("Stranger: Do you remember your name?")
# time.sleep(2)
print(f"{player_name}: Yes, my name is {player_name}.")
# time.sleep(2)
print(f"Gratos: Haha, nice to meet you {player_name}! My name is Gratos.")
# time.sleep(2)
print("Gratos: It seems you do not have a weapon yet. Here in the dungeon you will need one.")
# time.sleep(2)
print("Gratos: I don't have much, but you can choose one from me.")
print("Sword (5 dmg), 4/6 hit chance |  Axe (7 dmg), 3/6 hit chance |  Napkin (0 dmg)")

while True:
    weapon_choice = input("Choose weapon: ").lower()
    
    if weapon_choice == "sword":
        custom.weapon = sword
        print(f"Gratos: Ahhh, good old {custom.weapon.name}")
        break
        
    elif weapon_choice == "axe":
        custom.weapon = axe
        print(f"Gratos: Ahhh, good old {custom.weapon.name}")
        break
        
    elif weapon_choice == "napkin":
        print(f"Gratos: Are you serious??? I can't let you go with a napkin!")
        
    else:
        print("Gratos: That's not a valid weapon. Try again.")

print(f"Gratos: {player_name} WATCH OUT! A .....")
# # time.sleep(1)
# time.sleep(1)
# time.sleep(1)
print(f"{player_name}: Wha... Where am I?")
# time.sleep(1)
print(f"{player_name}: Huh..? How did I end up in the Dungeon?")
print(f"{player_name}: It's dangerous, I need to move.")
# time.sleep(1)
print(f"{player_name}: There's something in my pocket... A poster?")
print("""\
_______________________________________________
--THE LOCAL DUNGEON RELEASING TOXINS TO LAKES--
-----------------------------------------------
A local Goblin master is running an illegal ge-
nerator in the dungeon which releases toxins
to the nearby lake. Villagers have been...
_______________________________________________

.... Rest of the page was torn. 
""")

# time.sleep(3)
print(f"{player_name}: I need to stop the Goblin Master!")
# time.sleep(1)
current_room = level1Center
print(f"A {current_room.monster.name} starts running towards {player_name} What do you do?")

while True:
    print("|   Run   |     |   Attack   |")
    choice1 = input("Choose path: ").lower()

    if choice1 == "run":
        print(f"You ran past the {current_room.monster.name} and ended up in a different room")
        current_room = level1Left
        break

    elif choice1 == "attack":
        while current_room.monster.HP > 0:
            input(f"Press Enter to attack the {current_room.monster.name}!")

            if custom.weapon.attack():
                print(f"You swing your {custom.weapon.name} and hit the {current_room.monster.name} for {custom.weapon.damage} damage!")
                goblin.take_damage(custom.weapon.damage)
                print(f"The {current_room.monster.name} has now {current_room.monster.HP} health.")
            else:
                print(f"You swing your {custom.weapon.name}, but you missed! You took 5 damage.")
                player.take_damage(5)
                if player.HP <=0:
                    sys.exit(f"You were slain by {current_room.monster.name}")
        break
    else:
        print("I need to decide quickly!!!")


while True:
    print(f"{current_room.name}")
    print(current_room.description)

    if current_room.monster and current_room.monster.HP > 0:
        print(f"{current_room.monster.name} is blocking your way.")
        while current_room.monster.HP > 0:
                input("Press Enter to attack!")
        
                if custom.weapon.attack():
                    print(f"You swing your {custom.weapon.name} and hit the {current_room.monster.name} for {custom.weapon.damage} damage!")
                    GGoblin.take_damage(custom.weapon.damage)
                    print(f"The {current_room.monster.name} has now {current_room.monster.HP} health.")
                else:
                    print(f"You swing your {custom.weapon.name}, but you missed!")

    if current_room == level1Right:
        print(f"The {current_room.monster.name} dropped a smithing stone in the ground")
        while True:
            choice2 = input("Take the smithing stone?:\n     | YES |     | NO |\n").lower()
            if choice2 == "yes":
                player.inventory.append("smithing stone")
                print("Obtained: Smithing stone for a weapon upgrade. Type 'inventory' to check pockets")
                break
            if choice2 == "no":
                print("No... I don't think i'll need a rock.")
                break
            else:
                print("I need to decide.")

    if current_room == level2Right:
        #time.sleep(2)
        player.HP = 100
        print(f"Checkpoint reached. Health restored to {player.HP}")
        if "smithing stone" in player.inventory:
            print("Upgrade weapon?:\n    | Yes |    | No |")
            while True:
                choice3 = input("Upgrade weapon for +10 damage?: ").lower()

                if choice3 == "yes":
                    custom.weapon.damage += 10
                    player.inventory.remove("smithing stone")
                    print(f"{custom.weapon.name} upgraded for +10! It now deals {custom.weapon.damage} damage.")
                    break

                if choice3 == "no":
                    print(f"Nah.. Upgrades are for noobs.")
                    break

                else:
                    print("I need to decide.")

    available_exits = list(current_room.exits.keys())
    print(f"Exits available: {', '.join(available_exits)}")

    move = input("Where do you want to move?: ").lower()

    if move == "quit":
        print("Quitting game...")
        break

    if move in current_room.exits:
        current_room = current_room.exits[move]
    else:
        print("A stone wall is blocking the way")

    if move == "inventory":
        print(f"Inventory: {player.inventory}")