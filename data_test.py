# These dictionaries and master dictionaries are used in \
# 'new_turn_generator_2.py'.

# For now, only 'ref', 'name', 'init', and 'init_mod' are being made use of \
# 'init' refers to initiative, or relative speed in this case, and the \
# 'init_mod' is a modifier that determines 'init' reassignment between rounds \
# of fighting.

# Base dictionary that could be used to generate class objects later.
character_base_data = {
    'character_number': 0,
    'name': '',
    'class': '',
    'level': 1,
    'max_HP': 100,
    'current_HP': 100,
    'max_MP': 50,
    'current_MP': 50,
    'attack': 10,
    'defence': 10,
    'speed': 10,
    'magic': 10,
    'init': 0,
    'init_mod': 0,
    'statuses': ['fine', ],
}

# Master dictionary that can be referenced using a 'name' value.
party_data = {
    'c_1': {
        'ref': 'c_1',
        'number': 1,
        'name': 'Johnny Johns',
        'class': '',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': 7,
        'magic': 10,
        'init': 0,
        'init_mod': 0,
        'statuses': ['fine', ],
    },
    'c_2': {
        'ref': 'c_2',
        'number': 2,
        'name': 'Bibbs',
        'class': '',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': 12,
        'magic': 10,
        'init': 0,
        'init_mod': 0,
        'statuses': ['fine', ],
    },
    'c_3': {
        'ref': 'c_3',
        'number': 3,
        'name': 'Chobby Bobba',
        'class': '',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': -5,
        'magic': 10,
        'init': 0,
        'init_mod': 0,
        'statuses': ['fine', 'slow', ],
    }
}

# Generic 'enemy' dictionary.
e_1 = {
    'ref': 'e_1',
    'number': 0,
    'name': 'Mad Hatter',
    'class': 'Hatter',
    'level': 1,
    'max_HP': 100,
    'current_HP': 100,
    'max_MP': 50,
    'current_MP': 50,
    'attack': 10,
    'defence': 10,
    'speed': 30,
    'magic': 10,
    'init': 0,
    'init_mod': 0,
    'statuses': ['fine', 'haste', ],
}

# I created this list to allow better referencing of values during battle \
# processing, I think this dictionary could be populated anew every time an \
# instance of a battle started in the game and expunged afterwards.
battlers_data = {
    'c_1': {
        'ref': 'c_1',
        'number': 1,
        'name': 'Johnny Johns',
        'class': '',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': 7,
        'magic': 10,
        'init': 0,
        'init_mod': 0,
        'statuses': ['fine', ],
    },
    'c_2': {
        'ref': 'c_2',
        'number': 2,
        'name': 'Bibbs',
        'class': '',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': 12,
        'magic': 10,
        'init': 0,
        'init_mod': 0,
        'statuses': ['fine', ],
    },
    'c_3': {
        'ref': 'c_3',
        'number': 3,
        'name': 'Chobby Bobba',
        'class': '',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': -5,
        'magic': 10,
        'init': 10,
        'init_mod': 0,
        'statuses': ['fine', 'slow', ],
    },
    'e_1': {
        'ref': 'e_1',
        'number': 0,
        'name': 'Mad Hatter',
        'class': 'Hatter',
        'level': 1,
        'max_HP': 100,
        'current_HP': 100,
        'max_MP': 50,
        'current_MP': 50,
        'attack': 10,
        'defence': 10,
        'speed': 30,
        'magic': 10,
        'init': 0,
        'init_mod': 0,
        'statuses': ['fine', 'haste', ],
    },
}

# 'battlers' is a collection of the dictionaries that represent who will be \
# participating in the battle, when enemies are killed they can be removed \
# from this list.
battlers = [
    battlers_data['c_1'],
    battlers_data['c_2'],
    battlers_data['c_3'],
    battlers_data['e_1'],
]
