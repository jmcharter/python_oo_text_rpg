import rooms
from entities import Monster

map_locations = dict()

map_locations['start'] = rooms.EmptyRoom(
    "Starting room",
    "A creepy dark room.",
    {'e': 'forest',
     's': 'basement_01'}
)
map_locations['forest'] = rooms.EmptyRoom(
    "Forest clearing",
    "A small clearing in a forest.",
    {'w': 'start',
     'e': 'dark_forest'}
)

map_locations['dark_forest'] = rooms.EmptyRoom(
    "Dark Forest",
    "A dark area of the forest...",
    {'w': 'forest'}
)

map_locations['basement_01'] = rooms.ItemRoom(
    "Basement 01",
    "A dusty basement, it's quite empty.",
    {'n': 'start',
     'w': 'nest'}
)

map_locations['nest'] = rooms.MonsterRoom(
    "Monster nest",
    "You've stumbled into the nest of something...",
    {'e': 'basement_01'},
    Monster('Giant Spider', 'nest', 6, 3, 2, 2, 1, 8)
)
