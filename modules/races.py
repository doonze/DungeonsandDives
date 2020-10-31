# This is the master file for all race info containing all the dictionaries defining
# all the available races
from modules.custom_classes import *


human = {
    'race': 'Human',
    'str': 0,
    'dex': 0,
    'con': 0,
    'wis': 0,
    'int': 0,
    'chr': 0,
    'height': [62, 80],
    'weight': [135, 250],
    'age': [15, 60]

}


elf = {
    'race': 'Elf',
    'str': -2,
    'dex': 2,
    'con': -2,
    'wis': 0,
    'int': 2,
    'chr': 2,
    'height': [68, 86],
    'weight': [115, 190],
    'age': [25, 500]
}

dwarfs = Race('Dwarf', 2, -2, 2, 0, 0, -2, [42, 62], [150, 275], [20,250])

dwarf = {
    'race': 'Dwarf',
    'str': 2,
    'dex': -2,
    'con': 2,
    'wis': 0,
    'int': 0,
    'chr': -2,
    'height': [42, 62],
    'weight': [150, 275],
    'age': [20, 250]
}

gnome = {
    'race': 'Gnome',
    'str': -3,
    'dex': 4,
    'con': -2,
    'wis': -1,
    'int': 4,
    'chr': 0,
    'height': [36, 52],
    'weight': [52, 110],
    'age': [20, 175]
}

halfling = {
    'race': 'Halfling',
    'str': -1,
    'dex': 4,
    'con': 0,
    'wis': -2,
    'int': 0,
    'chr': 2,
    'height': [36, 52],
    'weight': [52, 110],
    'age': [20, 80]
}

orc = {
    'race': 'Orc',
    'str': 5,
    'dex': -2,
    'con': 4,
    'wis': -2,
    'int': -3,
    'chr': -2,
    'height': [80, 96],
    'weight': [250, 375],
    'age': [20, 50]
}
