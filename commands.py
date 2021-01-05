import ui


def valid_command(cmd, entity):
    valid_commands = {
        'move': ['n', 'e', 's', 'w', 'north', 'east', 'south', 'west'],
        'search': None,
        'inventory': [item for item in entity.items],
        'use': [item for item in entity.items],
        'quit': None,
        '?': ['move', 'search', 'inventory', 'use', 'quit']
    }
    input_qty = len(cmd)
    if 0 > input_qty > 3 or cmd[0] not in valid_commands:
        ui.input_error(*cmd)
        return False
    elif input_qty > 1 and cmd[1] not in valid_commands[cmd[0]]:
        ui.input_error(*cmd)
        return False
    else:
        return True


def parse_command(cmd, entity):
