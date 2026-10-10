# luodaan luokka huone, jolle ominaisuudet nimi ja kuvaus. Ja luodaan oliot johon voidaan asettaa poistumisvaihtoehdot, onko huoneessa hirviö ja onko huoneen esinettä kerätty 
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.monster = None
        self.item_collected = False

    # määritetään huoneen poistumisvaihtoehdot suunta ja huone mihin päädytään
    def add_exit(self, direction, room):
        self.exits[direction] = room