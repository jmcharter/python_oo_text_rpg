class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.descripition = description
        self.exits = exits


class EmptyRoom(Room):
    def __init__(self, name, description, exits):
        super().__init__(name, description, exits)


class MonsterRoom(Room):
    def __init__(self, name, description, exits):
        super().__init__(name, description, exits)


class ItemRoom(Room):
    def __init__(self, name, description, exits):
        super().__init__(name, description, exits)
