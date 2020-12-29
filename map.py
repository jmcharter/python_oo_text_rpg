import rooms


map = dict()

map['start'] = rooms.EmptyRoom(
    "Starting room",
    "A creepy dark room.",
    {'e': 'forest',
     's': 'basement'}
)
map['forest'] = rooms.EmptyRoom(
    "Forest clearing",
    "A small clearing in a forest.",
    {'w': 'start',
     'e': 'dark_forest'}
)

map['dark_forest'] = rooms.EmptyRoom(
    "Dark Forest",
    "A dark area of the forest...",
    {'w': 'forest'}
)

map['basement_01'] = rooms.ItemRoom(
    "Basement 01",
    "A dusty basement, it's quite empty.",
    {'n': 'start',
     'w': 'nest'}
)

map['nest'] = rooms.MonsterRoom(
    "Monster nest",
    "You've stumbled into the nest of something...",
    {'e': 'basement_01'}
)
