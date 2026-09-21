import sys
import time
import custom
from weapons import Weapon
from monsters import Monster

sword = Weapon("Sword", 5, 4)
axe = Weapon("Axe", 7, 3)

goblin = Monster("Goblin", 10)

#player name
player_name = input("Enter your name: ")

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
        custom.hat_color = input("Enter a hat color: ").lower()
        custom.jacket_color = input("Enter jacket color: ").lower()
        custom.jeans_color = input("Enter jeans color: ").lower()

    if navigation == "info":
        print(f"Name: {player_name}, Age {player_age:.0f}")

        if custom.hat_color is None:
            print("Color of hat not set")
        else:
             print(f"Color of hat: {custom.hat_color}")

        if custom.jacket_color is None:
            print("Color of jacket not set")
        else:
            print(f"Color of jacket: {custom.jacket_color}")

        if custom.jeans_color is None:
            print("Color of jeans not set")
        else:
             print(f"Color of jeans: {custom.jeans_color}")

    if navigation == "quit":
        sys.exit("Quitting game...")

    if navigation == "start":
        break

if custom.hat_color is None:
    custom.hat_color = input("Choose the color of the hat: ").lower()
    custom.jacket_color = input("Choose the color of the jacket: ").lower()
    custom.jeans_color = input("Choose the color of the jeans: ").lower()

print("Stranger: Hey, you. You're finally awake! How are you feeling?")
print("| Good |     | Bad |")
answer1 = input(f"{player_name}: ").lower()
if answer1 == "good":
        print("Stranger: I highly doubt that. It's like you fell from the heavens.")
elif answer1 == "bad":
        print("Stranger: I figured. You just fell from the sky.")
else:
    print("Stranger: Hmm... Not quite sure if I understand. You took a bit of a fall.")

time.sleep(2)
print("Stranger: Do you remember your name?")
time.sleep(2)
print(f"{player_name}: Yes, my name is {player_name}.")
time.sleep(2)
print(f"Gratos: Haha, nice to meet you {player_name}! My name is Gratos.")
time.sleep(2)
print("Gratos: It seems you do not have a weapon yet. Here in the dungeon you will need one.")
time.sleep(2)
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
time.sleep(1)
time.sleep(1)
time.sleep(1)
print(f"{player_name}: Wha... Where am I?")
time.sleep(1)
print(f"{player_name}: Huh..? How did I end up in the Dungeon?")
print(f"{player_name}: It's dangerous, I need to move.")
time.sleep(1)
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

time.sleep(3)
print(f"{player_name}: I need to stop the Goblin master!")
time.sleep(1)
print(f"A goblin starts running towards {player_name} What do you do?")
print("|   Run   |     |   Attack   |")

choice1 = input("Choose path: ").lower()

if choice1 == "run":
     print("You ran past the goblin and ended up in a different room")

elif choice1 == "attack":
    while goblin.HP > 0:
        input("Press Enter to attack!")

        if custom.weapon.attack():
            print(f"You swing your {custom.weapon.name} and hit the {goblin.name} for {custom.weapon.damage} damage!")
            goblin.take_damage(custom.weapon.damage)
            print(f"The {goblin.name} has now {goblin.HP} health.")
        else:
            print(f"The {goblin.name} backed down.")

else:
    print(f"You swing your {custom.weapon.name}, but you missed!")