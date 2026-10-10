import sys # sys.exittiä varten
import time # time.sleeppiä varten
from weapons import Weapon # ase luokka
from monsters import Monster # monsteri luokka
from room import Room # huone luokka
from PlayerInfo import Player # pelaaja luokka
import json # pelin tallennusta varten

# Asetetaan aseiden nimi, vahinko ja osumismahdollisuus.  
sword = Weapon("Sword", 6, 4)
axe = Weapon("Axe", 12, 3)
weapon_choice = None

# Tehdään sanakirja asekoodia varten, jotta tiedetään mikä ase ladataan nimen perusteella
weapon_directory = {
    "Sword": sword,
    "Axe": axe
}

# Luodaan monstereille nimi, elämäpisteet ja paljon tekee vahinkoa pelaajaan
Goblin = Monster("Goblin", 20, 5)
GGoblin = Monster("Giant Goblin", 50, 10)
MGoblin = Monster("Goblin Master", 100, 30)

#luodaan kartta Room luokan avulla, huoneen sijainti ja kuvaus
level0Start = Room("Fields", "A peaceful spot under a tree") # pelaajan aloitushuone ennen dungeoniin menemistä
level0End = Room("Fields", "You see Gratos waving at you...")
level1Center = Room("Starting place", "I can go left or right")
level1Left = Room("Left from the starting place", "I can go forward.") # GGoblin + syringe
level1Right = Room("Right from the starting place", "I can go forward.") # GGoblin + smithing stone
level1Behind = Room("A huge staircase leads down", "I can go forward.")

level2Center = Room("Generator room", "Turn the generator into gear") # upgrade gear
level2Left = Room("Treatment room", "Health upgrade laying on the ground") # Health upgrade +100 HP
level2Right = Room("An armory", "There is an anvil. I could sharpen my weapon") # Weapon upgrade +10 dmg
level3Center = Room("The Goblin Master room", "A throneroom full of gold and diamonds.")# Goblin master lopputaistelu huone
level2Behind = Room("A dim room", "It is hard to see.") # teamup with gratos

# määritetään jokaiselle huoneelle poistumissuunta / suunnat
level1Center.add_exit("left", level1Left)
level1Center.add_exit("right", level1Right)
level1Center.add_exit("behind", level1Behind)

level1Left.add_exit("forward", level2Left) # GGoblin + Syringe jolla otetaan health upgrade seuraavasta huoneesta
level2Left.add_exit("right", level2Center)

level1Right.add_exit("forward", level2Right) #GGoblin ja upgrade flint joka appendataan listaan, jolla päivitetään ase
level2Right.add_exit("left", level2Center)

level1Behind.add_exit("forward", level2Behind)
level2Behind.add_exit("forward",level2Center) # Gratos liittyy pelaajan matkaan

level2Center.add_exit("forward", level3Center)
level3Center.add_exit("forward", level0End)

#JSON määritetään jokaiselle huoneelle arvot
room_directory = {
    "Fields": level0Start,
    "Starting place": level1Center,
    "Left from the starting place": level1Left,
    "Right from the starting place": level1Right,
    "A huge staircase leads down": level1Behind,
    "Generator room": level2Center,
    "Treatment room": level2Left,
    "An armory": level2Right,
    "The Goblin Master room": level3Center,
    "A dim room": level2Behind
}

# Asetetaan pelaaja aloittamaan level0Start huoneesta
current_room = level0Start

# Merkitään hirviöt huoneisiin
level1Center.monster = Goblin
level1Left.monster = GGoblin
level1Right.monster = GGoblin
level1Behind.monster = GGoblin
level3Center.monster = MGoblin

# Pelaaja luokan ominaisuudet, asetetaan nimi, ikä, elämäpisteet, vahinko (Gratos tarvitsee "deals" ominaisuuden. Muuten ase tekee vahingon) ja tavaraluettelo
player = Player("Unknown", 0, 100, 0, inventory=[])
gratos = Player("Gratos", 158, 200, 30, inventory=[])

# Asetetaan ehto Gratoksen mahdolliselle polulle, joka vaihdetaan True kun pelaaja astuu huoneeseen level2Behind
gratos_joined = False
game_loaded = False  # Lippu tarkistamaan ladattiinko peli

# Tarkistetaan pelaajan ikä. Kysytään aina ohjelman käynnnistyessä
while True:
    try:
        player_age = int(input("Enter your age: "))
        player.age = player_age
        break
    except ValueError:
        print("Error: Set value is not a number. Try again")
    print(f"Player age: {player_age}.")
# jos pelaaja on alle 12 peli sulkeutuu
if player_age < 12:
    sys.exit("This game is meant for people over the age of 12. Quitting game.")

print(" ")

# Avataan ohjeet.txt ja menu.txt pelin alkaessa
with open("ohjeet.txt", "r") as ohjeet:
    data = ohjeet.read()
    print(data)

input("Press enter to continue: ")

while True:
    with open("menu.txt", "r") as menu:
        data = menu.read()
        print(data)

    navigation = input("Type to navigate: ").lower()

    # pelaajan tiedot tulostetaan konsoliin Nimi, ikä, tavaraluettelo, ase jos se on valittu, ja sen vahinko 
    if navigation == "info":
        print(f"Name: {player.name} Age: {player.age}")
        print(f"Inventory: {player.inventory}")
        if weapon_choice is not None:
            print(f"Weapon: {weapon_choice.name} (Damage: {weapon_choice.damage})")
        else:
            print("Weapon: None")
        input("Press Enter to continue: ")

    elif navigation == "load":
        try:
            with open("savegame.json", "r", encoding="utf-8") as file:
                loaded_data = json.load(file)
                
                player.name = loaded_data["player_name"]
                player.age = loaded_data["player_age"]
                player.HP = loaded_data["player_hp"]
                player.inventory = loaded_data["player_inventory"]
                gratos_joined = loaded_data["gratos_joined"]
                
                # Ladataan ase takaisin weapon muuttujaan ja asetetaan sen vahinko
                weapon_name = loaded_data.get("weapon_name", "Sword")
                weapon_damage = loaded_data.get("weapon_damage", 6)

                # jos aseen nimi on aijemin luodussa json weapon_directoryssä. weapon_choice muuttuja saa tallennetun aseen arvon
                if weapon_name in weapon_directory:
                    weapon_choice = weapon_directory[weapon_name]
                else:
                    weapon_choice = sword
                weapon_choice.damage = weapon_damage  # Palautetaan päivitetty vaurio, jos asetta on parannettu

                # etsitään json mäppäyksestä pelaajan sijainti ja määritetään se nykyiseksi huoneeksi
                room_name = loaded_data["current_room"]
                if room_name in room_directory:
                    current_room = room_directory[room_name]
                
            print("Game loaded...")
            print(f"Welcome back, {player.name} (HP: {player.HP}, Weapon: {weapon_choice.name} DMG: {weapon_choice.damage})!\n")
            input("Press Enter to continue game: ")
            game_loaded = True  # Merkitään, että peli ladattiin. Tämä hyppää pelin intron yli ja jatkaa tallennuspisteestä
            break
            
        except FileNotFoundError:
            print("\n Saved game file not found: Start a new game. \n")
            input("Press Enter to continue: ")
             
    elif navigation == "quit":
        sys.exit("Quitting game...")

    # Peli alkaa start komennolla
    elif navigation == "start":
        with open("intro.txt", "r") as tiedosto:
            data = tiedosto.read()
            print(data)
        input("Press enter to continue: ")
        break

    else:
        print("This is not a menu option. Type again.")

# Jos peli ladattiin niin ohitetaan pelin intro
if not game_loaded:
    player.name = input("Enter your name: ")
    player_info = print (f"Hello, {player.name} Age: {player.age}")
    time.sleep(1)
    print("Stranger: Hey, you. You're finally awake! How are you feeling?")
    print("| Good |     | Bad |")
    answer1 = input(f"{player.name}: ").lower()
    if answer1 == "good":
            print("Stranger: I highly doubt that. It's like you fell from the heavens.")
    elif answer1 == "bad":
            print("Stranger: I figured. You just fell from the sky.")
    else:
        print("Stranger: Hmm... Not quite sure if I understand. You took a bit of a fall.")

    # import time kirjaston avulla voidaan hidastaa tekstin tulostusta jotta dialogista tulee selkeämpää 
    time.sleep(1)
    print("Stranger: Do you remember your name?")
    time.sleep(1)
    print(f"{player.name}: Yes, my name is {player.name}.")
    time.sleep(1)
    print(f"Gratos: Haha, nice to meet you {player.name}! My name is Gratos.")
    time.sleep(1)
    print("Gratos: It seems you do not have a weapon yet. Here in the dungeon you will need one.")
    time.sleep(1)
    print("Gratos: I don't have much, but you can choose one from me.\n")
    print("Sword (6 dmg), 5/6 hit chance |  Axe (12 dmg), 4/6 hit chance |  Napkin (0 dmg)")

    while True:
        weapon_choice = input("Choose weapon: ").lower()
        
        if weapon_choice == "sword":
            weapon_choice = sword
            print(f"Gratos: Ahhh, good old {weapon_choice.name}")
            break
            
        elif weapon_choice == "axe":
            weapon_choice = axe
            print(f"Gratos: Ahhh, good old {weapon_choice.name}")
            break

        # nenäliinaa ei voi asettaa aseeksi ja Gratos reagoi asianmukaisesti
        elif weapon_choice == "napkin":
            print(f"Gratos: Are you serious??? I can't let you go with a napkin!")
            
        else:
            print("Gratos: That's not a valid weapon. Try again.")

    print(f"Gratos: {player.name} WATCH OUT! A .....\n")
    time.sleep(3)
    print(f"{player.name}: Wha... Where am I?")
    time.sleep(1)
    print(f"{player.name}: Huh..? How did I end up in the Dungeon?")
    time.sleep(1)
    print(f"{player.name}: It's dangerous, I need to move.")
    time.sleep(1)
    print(f"{player.name}: There's something in my pocket... A poster?")
    time.sleep(2)

    # avataan news.txt tekstitiedosto jossa anetaan pelaajalle tavoite pysäyttää Peikko Mestari
    with open("news.txt", "r") as news:
        data = news.read()
        print(data)
        input("Press Enter to continue: ")

    print(f"{player.name}: I need to stop the Goblin Master!\n")

    # Pelaaja asetetaan level1Center, jossa ensimmäinen hirviö tulee vastaan
    current_room = level1Center
    print(f"A {current_room.monster.name} starts running towards {player.name} What do you do?")

    while True:
        print("|   Run   |     |   Attack   |")
        choice1 = input("Choose path: ").lower()
        # jos pelaaja juoksee niin asetetaan pelaaja juoksemaan aina huoneeseen level1Left
        if choice1 == "run":
            print(f"You ran past the {current_room.monster.name} and ended up in a different room")
            current_room = level1Left
            break
        # jos pelaaja hyökkää niin pelaaja on while silmukassa niin kauan kunnes toisen elämäpisteet osuu 0
        elif choice1 == "attack":
            while current_room.monster.HP > 0:
                input(f"Press Enter to attack the {current_room.monster.name}!")

                if weapon_choice.attack():
                    print(f"You swing your {weapon_choice.name} and hit the {current_room.monster.name} for {weapon_choice.damage} damage!")
                    current_room.monster.take_damage(weapon_choice.damage)
                else:
                    print(f"You swing your {weapon_choice.name}, but you missed! You took 5 damage.\n")
                    player.take_damage(5)
                    if player.HP <=0:
                        sys.exit(f"You were slain by {current_room.monster.name}")
            break
        else:
            print("I need to decide quickly!!!")

while True:
    print(f"\n{current_room.name}")

    if current_room.monster and current_room.monster.HP > 0:        
        print(f"{current_room.monster.name} is blocking your way.")
        # Jos aikaisemmin määritetty vipu gratoksen liittymiselle on tosi, niin suoritetaan gratoksen hyökkäys viholliseen 
        if gratos_joined == True:
            print(f"Gratos lifts his axes and launches himself towards the {current_room.monster.name} dealing {gratos.deals} damage!")
            current_room.monster.take_damage(gratos.deals)
            time.sleep(2)
            print(f"{player.name}: Woah! That was a crazy move {gratos.name}")

        # Sama while silmukka tähän, kun elämäpisteet osuu 0 niin silmukka päättyy        
        while current_room.monster.HP > 0:
                input("Press Enter to attack!\n")
                if weapon_choice.attack():
                    print(f"You swing your {weapon_choice.name} and hit the {current_room.monster.name} for {weapon_choice.damage} damage!")
                    current_room.monster.take_damage(weapon_choice.damage)
                else:
                    print(f"You swing your {weapon_choice.name}, but you missed!")
                    player.take_damage(current_room.monster.deals)
                    if player.HP <=0:
                        # Peli päättyy kun pelaajan elämäpisteet osuu 0
                        sys.exit(f"You were slain by {current_room.monster.name}")

    #  Määritetään huoneet level1Right, left ja behind, jos huoneen esinettä ei ole kerätty niin seuraava koodi ajetaan
    if current_room == level1Right and not current_room.item_collected:
        print(f"The {current_room.monster.name} dropped a smithing stone in the ground")
        while True:
            choiceStone = input("Take the smithing stone?:\n    | YES |     | NO |\n").lower()
            if choiceStone == "yes":
                # Määritetään nykyisen huoneen esine kerätyksi ja appendataan se pelaajan tavaraluetteloon sama käy kaikkiin seuraaviin pelaajan päivityshuoneisiin
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
            ChoiceHealth = input("Take the syringe?:\n    | YES |     | NO |\n").lower()
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
        choiceMultiU = input("Take the armour and consume the glowing liquid?:\n    | YES |     | NO |\n").lower()

        # Päivitetään pelaajan elämäpisteet ja aseen vahinko, jos choiceMultiU muuttuja on tosi
        if choiceMultiU == "yes":
            player.inventory.append("Leather armour")
            player.HP = 100
            player.HP += 50
            weapon_choice.damage += 5
            current_room.item_collected = True
            print(f"{player.name}: Hmm... I feel... Great! And now I got a cool armour!")
            time.sleep(1)
            print("Obtained: Leather armour. Type 'inventory' to check pockets.")
            time.sleep(1)
            print(f"Health restored and gained +50 HP and {weapon_choice.name} deals now {weapon_choice.damage} damage.")
            time.sleep(1)
            print(f"Health now: {player.HP}")
        # jos muuttuja on epätosi niin jatketaan peliä
        if choiceMultiU == "no":
            print(f"{player.name}: I better not get too close to the {current_room.monster.name}.")
            
    # Taistelun jälkeen palautetaan pelaajan elämäpisteet ennen mahdollisen asepäivityksen tekoa
    if current_room == level2Right:
        player.HP = 100
        print(f"Health restored to {player.HP}")
        if "smithing stone" in player.inventory:
            print("Upgrade weapon?:\n    | Yes |    | No |")
            while True:
                choiceUpgrade = input("Use smithing stone and upgrade weapon for +10 damage?: ").lower()

                if choiceUpgrade == "yes":
                    weapon_choice.damage += 10
                    player.inventory.remove("smithing stone")
                    print(f"{weapon_choice.name} upgraded for +10! It now deals {weapon_choice.damage} damage.")
                    break

                if choiceUpgrade == "no":
                    print(f"Nah.. Upgrades are for noobs.")
                    break

                else:
                    print("I need to decide.")

    if current_room == level2Left:
        # Tarkistetaan onko pelaajalla ruiskua tavaraluettelossa
        if "syringe" in player.inventory:
            print("Upgrade health?:\n    | Yes |    | No |")
            choiceHealthU = input("Use syringe and upgrade health to 200?:\n").lower()
            # jos pelaaja päivittää elämäpisteet niin asetetaan pelaajan HP 200
            if choiceHealthU == "yes":
                player.HP = 200
                print(f"{player.name}'s health set to {player.HP} HP.")

            if choiceHealthU == "no":
                print(f"{player.name}: Nahh, I ain't a noob!")
                player.HP = 100
                print(f"Checkpoint reached {player.name} health set to {player.HP}")

        else:
            print("I could upgrade my health here.")
    
    if current_room == level2Center and not current_room.item_collected: # asetetaan current_room.item_collected sitä varten ettei pelaaja voi loputtomasti päivittää hahmoa silmukassa lähtemällä pelistä
        print("The generator is here. I can break it in pieces to upgrade my gear and stop the pollution.\n")
        time.sleep(1)
        print("Riks")
        time.sleep(1)
        print("Raks")
        time.sleep(1)
        print("Poks")
        # päivitetään pelaajan elämäpisteet ja aseen vahinko
        player.HP += 50
        weapon_choice.damage += 10
        current_room.item_collected = True
        print(f"{player.name}: Oh yeeah!\n Weapon damage upgraded to {weapon_choice.damage}\n Health upgraded to {player.HP}.")
        time.sleep(1)
        print(f"{player.name}: I am ready to take the Goblin Master down!\n")

    if current_room == level2Behind:
        print(f"Orc: {player.name}?? Is it really you?")
        time.sleep(1)
        print(f"{player.name}: Not a step closer I have a weapon and I know how to use it!")
        time.sleep(1)
        print(f"Gratos: Woah!... Chillax {player.name}. It's me Gratos. Man I am glad I found you.")
        time.sleep(1)
        print(f"{player.name}: Oh, it's just you. Gratos we don't have time. We have to defeat the Goblin Master!!")
        time.sleep(1)
        print(f"Gratos: I saw the news {player.name}. I am with you!\n")
        time.sleep(1)
        gratos_joined = True # asetetaan Gratos liittymään lopputaisteluun asettamalla tosi muuttujaan gratos_joined
        print(f"Gratos will now help you defeat the Master Goblin!\n")

    # Pelin loppuvaihe, jossa kerrotaan Peikko Mestarille miten voisi parantaa tapojaan
    if current_room == level3Center:
        print(f"{player.name}: I did it! {current_room.monster.name}, you have done a lot of bad things to the village.")
        time.sleep(1)
        print(f"{current_room.monster.name}: Me knows.... Feel bad I do.. Me just wanted to mine shiny ores.")
        time.sleep(1)
        print(f"{player.name}: I stopped the pollution coming from your generator and recycled the materials to upgrade my gear totally carbon neutral")
        time.sleep(1)
        print(f"{current_room.monster.name}: Wooooww... Incredible craftmanship me say!")
        time.sleep(1)
        print(f"{player.name}: Look {current_room.monster.name}. You don't need coal to power these machines.")
        time.sleep(1)
        print(f"{player.name}: You can make a watermill next to the lake or a wind turbine on the fields. This way you will create a lot of energy wihout damaging the environment.")
        time.sleep(1)
        print(f"{current_room.monster.name}: See I do. Thank you wise human!")
    # kun pelaaja saavuttaa level0End. Tulostetaan lopputekstit, jos Gratos oli mukana niin ending2 mutta muuten ending1 
    if current_room == level0End:
        if gratos_joined == True:
            with open("ending2.txt", "r") as end2:
                data = end2.read()
                print(data)
                break
        else:
            with open("ending1.txt", "r") as end1:
                data = end1.read()
                print(data)
                break
    # tulostetaan pelaajan konsoliin reitit mihin voi mennä    
    available_exits = list(current_room.exits.keys())
    print(f"Exits available: {', '.join(available_exits)}")

    move = input("Where do you want to move?: ").lower()
    # pelistä poistuminen
    if move == "quit":
        print("Quitting game...")
        break

    elif move == "inventory":
        print(f"\nInventory: {player.inventory}")
        if weapon_choice is not None:
            print(f"Weapon: {weapon_choice.name} (Damage: {weapon_choice.damage})\n")
        else:
            print("Weapon: None\n")
        continue

    elif move in current_room.exits:
        current_room = current_room.exits[move]
        
        #tallennus JSON tiedostoon. Aseen nimi ja aseen vahinko, jos arvoa ei saada niin asetetaan varakeinoksi arvo 6
        current_weapon_name = weapon_choice.name if weapon_choice else "Sword"
        current_weapon_damage = weapon_choice.damage if weapon_choice else 6
        # tiedot mitä tallennetan savegame.json tiedostoon
        game_data = {
            "player_name": player.name,
            "player_age": player.age,
            "player_hp": player.HP,
            "player_inventory": player.inventory,
            "weapon_name": current_weapon_name,
            "weapon_damage": current_weapon_damage,
            "current_room": current_room.name,
            "gratos_joined": gratos_joined
        }
        # luodaan tai muokataan tiedosto savegame.json utf-8 enkoodauksella ja tallennetaan pelaajan arvot sinne 
        with open("savegame.json", "w", encoding="utf-8") as file:
            json.dump(game_data, file, indent=4)
        
        print("Game saved...")
    # jos pelaaja kirjoittaa suunnan väärin niin tulostetaan tämä
    else:
        print("A stone wall is blocking the way")