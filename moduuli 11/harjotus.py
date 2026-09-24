# # periytyminen esimerkki

# class Varusmies():
#     def __init__(self, etunimi, sukunimi):
#         self.etunimi = etunimi
#         self.sukunimi = sukunimi

#     def ilmoita_tiedot(self):
#         print(f"{self.etunimi} {self.sukunimi}")


# class Miehistö(Varusmies):
#     def __init__(self, etunimi, sukunimi, sotilasarvo="Sotamies"):
#         super.__init__(etunimi, sukunimi)
#         self.sotilasarvo = sotilasarvo

#     def ilmoita_tiedot(self):
#         super().ilmoita_tiedot()
#         print(f"{self.sotilasarvo}")

# class Henkilökunta(Miehistö):
#     self.tehtävä = tehtävä
#     print(f"{self.tehtävä]")

# # MAIN

# # varusmies1 = Varusmies(input("Etunimi: "), input("Sukunimi: "))
# # varusmies1.ilmoita_tiedot()

# miehistö1 = Miehistö(input("Etunimi: "), input("Sukunimi: ", input("Sotilasarvosi: ")))
# miehistö1.ilmoita_tiedot()



class Adventurer():
    def __init__(self, name, health=100, stamina=100, attackDamage=10):
     self.name = name
     self.health = health
     self.stamina = stamina
     self.attackDamage = attackDamage

     def gainLife(self, healingAmount):
        self.healingPoints += healingAmount
        print(f"{self.name} gains {self.healingPoints}.")

    def loseLife(self, amount):
       self.healingPoints -= amount

       if self.healingPoints <= 0:
          print("You died")
          
        else:
          print(f"{self.name} loses: {amount} of HP")

    PlayerList = []

    player1 = Adventurer(input("Nimi: "))
    player2 = Adventurer(input("Nimi: "))
    player3 = Adventurer(input("Nimi: "))

    PlayerList.append(player1)
    PlayerList.append(player2)
    PlayerList.append(player3)

    # for i in range(3):
    #    player = Adventurer(input("Adventurer name: "))
    #    playerList.append

for player in PlayerList:
   print(player.name)

player1.loseHealth(50)
player2.gainlife(50)
print("Player 3 has anjurismi")
player3.loselife(50)

