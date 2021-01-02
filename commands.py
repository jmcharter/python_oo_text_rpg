from entities import Player_Character
pc = Player_Character('player', 'start', 10, 6, 6, 7)

commands = {
    'move': pc.move,
    'item': pc.item
}


def parse_command(cmd):
    if cmd[0] in commands:
        commands[cmd[0]]
    else:
        print("Command not valid, type '?' for help.")


# if cmd[0] == 'move':
#     if pc.move(cmd[1], room):
#         room = map_locations[pc.location]
#         print(f"You enter {room.name}.\n'{room.description}'")
#     else:
#         print("You cannot go this way ")