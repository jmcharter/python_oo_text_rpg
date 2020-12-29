import random


class Entity:
    def __init__(self, name, hp, strength, defence, agility):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.defence = defence
        self.agility = agility
        self.is_alive = True

    def __str__(self):
        return \
            f"Entity object with name {self.name} and stats: HP: {self.hp},"\
            "Atk: {self.strength}, Def: {self.defence}, Spd: {self.agility}"

    def attack_target(self, target):
        damage = int(random.randrange(1, 7)) + random.randrange(1, 7) +\
                 self.strength
        target.hp = target.hp - (damage - target.defence)

    def is_alive(self):
        return self.hp > 0


class Player_Character(Entity):

    def __init__(self, name, hp, strength, defence, agility):
        super().__init__(name, hp, strength, defence, agility)
        self.level = 1
        self.xp = 0
        self.command_list = ["move", "search", "item"]

    def parse_command(self, command, *args):
        if command.lower() in self.command_list:
            self.command_list[command]()
        else:
            print("Command not found.")

    def move(self):
        print('move')

    def search(self):
        print('search!')

    def item(self):
        print('item')


class Monster(Entity):
    def __init__(self, name, hp, strength, defence, agility, xp_given):
        super().__init__(name, hp, strength, defence, agility)
        self.level = 1
        self.xp_given = xp_given
