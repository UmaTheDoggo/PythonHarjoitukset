import sys
import time
import custom
from weapons import Weapon
from monsters import Monster
from room import Room
from PlayerInfo import Player
import json
import os

#weapons and monsters
sword = Weapon("Sword", 6, 4)
axe = Weapon("Axe", 12, 3)

goblin = Monster("Goblin", 20, 5)
GGoblin = Monster("Giant Goblin", 50, 10)
MGoblin = Monster("Goblin Master", 100, 30)

#luodaan kartta
level0Start = Room("Fields", "A peaceful spot under a tree") # pelaajan aloitushuone ennen dungeoniin menemistä
level0End = Room("Fields", "You see Gratos waving at you...")
level1Center = Room("Starting place", "I can go left or right")
level1Left = Room("Left from the starting place", "I can go forward.") # GGoblin + syringe
level1Right = Room("Right from the starting place", "I can go forward.") # GGoblin + smithing stone
level1Behind = Room("A huge staircase leads down", "I can go forward.")

level2Center = Room("Generator room", "Turn the generator into gear") # upgrade gear
level2Left = Room("Treatment room", "Health upgrade laying on the ground") # Health upgrade +100 HP
level2Right = Room("An armory", "There is an anvil. I could sharpen my weapon") # Weapon upgrade +10 dmg
level3Center = Room("The Goblin Master room", "A throneroom full of gold and diamonds.")# fight
level2Behind = Room("A dim room", "It is hard to see.") # teamup with gratos


level1Center.add_exit("left", level1Left)
level1Center.add_exit("right", level1Right)
level1Center.add_exit("behind", level1Behind)

level1Left.add_exit("forward", level2Left) # GGoblin + Syringe jolla otetaan health upgrade seuraavasta huoneesta
level2Left.add_exit("right", level2Center)

level1Right.add_exit("forward", level2Right) #GGoblin ja upgrade flint joka appendataan listaan, jolla päivitetään ase
level2Right.add_exit("left", level2Center)

level1Behind.add_exit("forward", level2Behind)
level2Behind.add_exit("forward",level3Center) # go against the goblin master with Gratos

level2Center.add_exit("forward", level3Center)
level3Center.add_exit("forward", level0End)

#aloitus huone
current_room = level0Start

#dungeon monsters
level1Center.monster = goblin
level1Left.monster = GGoblin
level1Right.monster = GGoblin
level1Behind.monster = GGoblin
level3Center.monster = MGoblin

#player
player_name = input("Enter your name: ")
player = Player(player_name, 100, 0, inventory=[])
gratos = Player("Gratos", 200, 30, inventory=[])

#Asetetaan ehto Gratoksen mahdolliselle polulle
gratos_joined = False

#player age
while True:
    try:
        player_age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Error: Set value is not a number. Try again")
    print(f"Player age: {player_age}.")

if player_age < 12:
    sys.exit("This game is meant for people over the age of 12. Quitting game.")

print(" ")

#player info
player_info = print (f"Hello, {player_name}, Age: {player_age:.0f}")


with open("ohjeet.txt", "r") as ohjeet:
    data = ohjeet.read()
    print(data)

input("Press enter to continue: ")

while True:
    # time.sleep(1)
    with open("menu.txt", "r") as menu:
        data = menu.read()
        print(data)
    
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
        with open("intro.txt", "r") as tiedosto:
            data = tiedosto.read()
            print(data)
    input("Press enter to continue: ")
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
print("Sword (6 dmg), 5/6 hit chance |  Axe (12 dmg), 4/6 hit chance |  Napkin (0 dmg)")

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

with open("save.txt", "w") as document:
    document.write("Player in dungeon.")

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
                current_room.monster.take_damage(custom.weapon.damage)
                #print(f"The {current_room.monster.name} has now {current_room.monster.HP} health.\n")
            else:
                print(f"You swing your {custom.weapon.name}, but you missed! You took 5 damage.\n")
                player.take_damage(5)
                if player.HP <=0:
                    sys.exit(f"You were slain by {current_room.monster.name}")
        break
    else:
        print("I need to decide quickly!!!")


while True:
    print(f"\n{current_room.name}")
    #print(current_room.description)

    if current_room.monster and current_room.monster.HP > 0:        # ASETA GRATOS TULEMAAN VIIMEISEEN BOSSIIN JOS PELAAJA VALITSEE OIKEAN ROUTEN
        print(f"{current_room.monster.name} is blocking your way.")

        if gratos_joined == True:
            print(f"Gratos lifts his axes and launches himself towards the {current_room.monster.name} dealing {gratos.deals} damage!")
            current_room.monster.take_damage(gratos.deals)
            print(f"{player.name}: Woah! That was a crazy move {gratos.name}")
        
        while current_room.monster.HP > 0:
                
                input("Press Enter to attack!\n")
                if custom.weapon.attack():
                    print(f"You swing your {custom.weapon.name} and hit the {current_room.monster.name} for {custom.weapon.damage} damage!")
                    current_room.monster.take_damage(custom.weapon.damage)
                    #print(f"The {current_room.monster.name} has now {current_room.monster.HP} health.")
                else:
                    print(f"You swing your {custom.weapon.name}, but you missed!")
                    player.take_damage(current_room.monster.deals)
                    if player.HP <=0:
                        sys.exit(f"You were slain by {current_room.monster.name}")

    if current_room == level1Right and not current_room.item_collected:
        print(f"The {current_room.monster.name} dropped a smithing stone in the ground")
        while True:
            choiceStone = input("Take the smithing stone?:\n     | YES |     | NO |\n").lower()
            if choiceStone == "yes":
                player.inventory.append("smithing stone")
                current_room.item_collected = True
                print("Obtained: Smithing stone for a possible weapon upgrade. Type 'inventory' to check pockets.")
                break
            if choiceStone == "no":
                print("No... I don't think i'll need a rock.")
                break
            else:
                print("I need to decide.")

    if current_room == level1Left and not current_room.item_collected:
        print(f"The {current_room.monster.name} dropped a syringe.")
        while True:
            ChoiceHealth = input("Take the syringe?:\n     | YES |     | NO |\n").lower()
            if ChoiceHealth == "yes":
                player.inventory.append("syringe")
                current_room.item_collected = True
                print("Obtained syringe for a possible health upgrade. Type 'inventory' to check pockets.")
                break
            if ChoiceHealth == "no":
                print("I am not touching that... yuck.")
                break
            else:
                print("I need to decide.")

    if current_room == level1Behind and not current_room.item_collected:
        print(f"{current_room.monster.name} dropped a leather armour and a glowing bottle?")
        choiceMultiU = input("Take the armour and consume the glowing liquid?:\n     | YES |     | NO |\n").lower()

        if choiceMultiU == "yes":
            player.inventory.append("Leather armour")
            player.HP = 100
            player.HP += 50
            custom.weapon.damage += 5
            current_room.item_collected = True
            print(f"{player.name}: Hmm... I feel... Great! And now I got a cool armour!")
            print("Obtained: Leather armour. Type 'inventory' to check pockets.")
            print(f"Health restored and gained +50 HP and {custom.weapon.name} deals now {custom.weapon.damage} damage.")
            print(f"Health now: {player.HP}")

        if choiceMultiU == "no":
            print(f"{player.name}: I better not get too close to the {current_room.monster.name}.")
            

    if current_room == level2Right:
        #time.sleep(2)
        player.HP = 100
        print(f"Checkpoint reached. Health restored to {player.HP}")
        if "smithing stone" in player.inventory:
            print("Upgrade weapon?:\n    | Yes |    | No |")
            while True:
                choiceUpgrade = input("Use smithing stone and upgrade weapon for +10 damage?: ").lower()

                if choiceUpgrade == "yes":
                    custom.weapon.damage += 10
                    player.inventory.remove("smithing stone")
                    print(f"{custom.weapon.name} upgraded for +10! It now deals {custom.weapon.damage} damage.")
                    break

                if choiceUpgrade == "no":
                    print(f"Nah.. Upgrades are for noobs.")
                    break

                else:
                    print("I need to decide.")

    if current_room == level2Left:
        if "syringe" in player.inventory:
            print("Upgrade health?:\n    | Yes |    | No |")
            choiceHealthU = input("Use syringe and upgrade health to 200?:\n").lower()
            
            if choiceHealthU == "yes":
                player.HP = 200
                print(f"{player.name}'s health set to {player.HP} HP.")

            if choiceHealthU == "no":
                print(f"{player.name}: Nahh, I ain't a noob!")
                player.HP = 100
                print(f"Checkpoint reached {player.name} health set to {player.HP}")

        else:
            print("I need to decide!")
    
    if current_room == level2Center and not current_room.item_collected:
        print("The generator is here. I can break it in pieces to upgrade my gear and stop the pollution.")
        time.sleep(1)
        print("Riks")
        time.sleep(1)
        print("Raks")
        time.sleep(1)
        print("Poks")
        player.HP += 50
        custom.weapon.damage += 10
        current_room.item_collected = True
        print(f"{player.name}: Oh yeeah!\n Weapon damage upgraded to {custom.weapon.damage}\n Health upgraded to {player.HP}.")
        time.sleep(1)
        print(f"{player.name}: I am ready to take the Goblin Master down!")

    if current_room == level2Behind:
        print(f"Orc: {player.name}?? Is it really you?")
        print(f"{player.name}: Not a step closer I have a weapon and I know how to use it!")
        print(f"Gratos: Woah!... Chillax {player.name}. It's me Gratos. Man I am glad I found you.")
        print(f"{player.name}: Oh, it's just you. Gratos we don't have time. We have to defeat the Goblin Master!!")
        print(f"Gratos: I saw the news {player.name}. I am with you!\n")
        gratos_joined = True
        print(f"Gratos will now help you defeat the Master Goblin!\n")

    if current_room == level3Center:
        print(f"{player.name}: I did it! {current_room.monster.name}, you have done a lot of bad things to the village.")
        #time.sleep(1)
        print(f"{current_room.monster.name}: Me knows.... Feel bad I do.. Me just wanted to mine shiny ores.")
        #time.sleep(1)
        print(f"{player.name}: I stopped the pollution coming from your generator and recycled the materials to upgrade my gear totally carbon neutral")
        #time.sleep(1)
        print(f"{current_room.monster.name}: Wooooww... Incredible craftmanship me say!")
        time.sleep(1)
        print(f"{player.name}: Look {current_room.monster.name}. You don't need coal to power these machines.")
        time.sleep(1)
        print(f"{player.name}: You can make a watermill next to the lake or a wind turbine on the fields. This way you will create a lot of energy wihout damaging the environment.")
        time.sleep(1)
        print(f"{current_room.monster.name}: See I do. Thank you wise human!")



    if current_room == level0End:
        print("Gratos greets you and the whole villagers celebrate for saving them.")
        break

        
    available_exits = list(current_room.exits.keys())
    print(f"Exits available: {', '.join(available_exits)}")

    move = input("Where do you want to move?: ").lower()

    if move == "quit":
        print("Quitting game...")
        break

    elif move == "inventory":
        print(f"\nInventory: {player.inventory}\n")
        continue

    elif move in current_room.exits:
        current_room = current_room.exits[move]
    else:
        print("A stone wall is blocking the way")