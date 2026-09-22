class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.monster = None

    def add_exit(self, direction, room):
        self.exits[direction] = room