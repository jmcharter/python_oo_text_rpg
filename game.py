from entities import Player_Character
from game_map import map_locations
from game_devices import Die
import commands as cmd
import ui


def get_room(room):
    return map_locations[room]


def play():
    pc = Player_Character('player', 'start', 10, 6, 6, 7)
    room = get_room(pc.location)
    while pc.is_alive and not pc.victory:
        user_input = input("> ").lower().split()
        if not cmd.valid_command(user_input, pc):
            continue


play()
