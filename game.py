from entities import Player_Character
from game_map import map_locations
import commands
from commands import pc


def play():
    name = input("Please enter your name: ")
    # pc = Player_Character(name, 'start', 10, 6, 6, 7)
    room = map_locations[pc.location]

    while pc.is_alive() and not pc.victory:
        room.action()


def test():

    # pc = Player_Character('player', 'start', 10, 6, 6, 7)
    room = map_locations[pc.location]
    while True:
        cmd = input("Enter command: ").split(' ')
        commands.parse_command(cmd)
        room.action()


test()
