class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def action(self):
        # Rooms have no action by default
        pass

    def valid_exit(self, direction):
        return direction in self.exits


class EmptyRoom(Room):
    def __init__(self, name, description, exits):
        super().__init__(name, description, exits)


class MonsterRoom(Room):
    def __init__(self, name, description, exits, monster):
        super().__init__(name, description, exits)
        self.monster = monster

    def action(self):
        pass

    def check_monster(self):
        if not self.monster.is_alive():
            self.description += f"""
             The corpse of a {self.monster.name} lies here."""


class ItemRoom(Room):
    def __init__(self, name, description, exits):
        super().__init__(name, description, exits)
