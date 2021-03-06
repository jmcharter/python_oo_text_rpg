class Entity:
    # All entities (player and NPCs) are based off of this class

    def __init__(self, name, location, hp, strength, defence, agility):
        self.name = name
        self.location = location
        self.hp = hp
        self.strength = strength
        self.defence = defence
        self.agility = agility

    def __str__(self):
        return \
            f"Entity object with name {self.name} and stats: HP: {self.hp}, "\
            f"Atk: {self.strength}, Def: {self.defence}, Spd: {self.agility}"

    def attack_target(self, target, damage):
        target.hp = target.hp - (damage - target.defence)

    def is_alive(self):
        return self.hp > 0

# Player class


class Player_Character(Entity):

    def __init__(self, name, location, hp, strength, defence, agility):
        super().__init__(name, location, hp, strength, defence, agility)
        self.level = 1
        self.xp = 0
        self.items = []
        self.victory = False

    def update_location(self, location):
        self.location = location

    def get_items(self):
        return self.items


class Monster(Entity):
    def __init__(self, name, location, hp, strength, defence, agility, level, xp_given):
        super().__init__(name, location, hp, strength, defence, agility)
        self.level = level
        self.xp_given = xp_given

# Monsters

