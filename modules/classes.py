# This is the master file for all class info containing all the dictionaries defining
# all the available classes

d = {
    'sp1': {
        'a1': {'c1': 2, 'c2': 3},
        'a2': {'c3': 1, 'c4': 4}
    },
    'sp2': {
        'a1': {'c1': 3, 'c2': 3},
        'a2': {'c3': 2, 'c4': 0}
    }
}


warrior = {
    'stats': {
        'class': 'Warrior', 'hit_die': 12},
    'skills': {
        'strength': {'athletics': 2},
        'dexterity': {'lockpick': 0, 'stealth': 0},
        'intelligence': {'search': 0},
        'wisdom': {'animals': 0, 'insight': 0, 'perception': 2},
        'charisma': {'deception': 0, 'intimidation': 2, 'persuasion': 0}, },
    'items': {
        'armor': {'wearable': ['light', 'medium', 'heavy']},
        'weapons': {'usable': ['simple', 'light', 'arms', 'heavy']}
    }
}


thief = {
    'stats': {
        'class': 'Thief', 'hit_die': 8},
    'skills': {
        'strength': {'athletics': 0},
        'dexterity': {'lockpick': 4, 'stealth': 4},
        'intelligence': {'search': 2},
        'wisdom': {'animals': 0, 'insight': 0, 'perception': 2},
        'charisma': {'deception': 2, 'intimidation': 0, 'persuasion': 0}, },
    'items': {
        'armor': {'wearable': ['light']},
        'weapons': {'usable': ['simple', 'light']}
    }
}


magi = {
    'stats': {
        'class': 'Magi', 'hit_die': 6},
    'skills': {
        'strength': {'athletics': 0},
        'dexterity': {'lockpick': 0, 'stealth': 0},
        'intelligence': {'search': 2},
        'wisdom': {'animals': 0, 'insight': 2, 'perception': 2},
        'charisma': {'deception': 0, 'intimidation': 0, 'persuasion': 2}, },
    'items': {
        'armor': {'wearable': ['light']},
        'weapons': {'usable': ['simple', 'light']}
    }
}


strider = {
    'stats': {
        'class': 'Strider', 'hit_die': 10},
    'skills': {
        'strength': {'athletics': 2},
        'dexterity': {'lockpick': 2, 'stealth': 2},
        'intelligence': {'search': 2},
        'wisdom': {'animals': 2, 'insight': 0, 'perception': 2},
        'charisma': {'deception': 0, 'intimidation': 0, 'persuasion': 0}, },
    'items': {
        'armor': {'wearable': ['light', 'medium']},
        'weapons': {'usable': ['simple', 'light', 'arms']}
    }
}


monk = {
    'stats': {
        'class': 'Monk', 'hit_die': 10},
    'skills': {
        'strength': {'athletics': 2},
        'dexterity': {'lockpick': 0, 'stealth': 0},
        'intelligence': {'search': 2},
        'wisdom': {'animals': 0, 'insight': 2, 'perception': 2},
        'charisma': {'deception': 0, 'intimidation': 2, 'persuasion': 2}, },
    'items': {
        'armor': {'wearable': ['light']},
        'weapons': {'usable': ['simple', 'light']}
    }
}


cleric = {
    'stats': {
        'class': 'Cleric', 'hit_die': 8},
    'skills': {
        'strength': {'athletics': 0},
        'dexterity': {'lockpick': 0, 'stealth': 0},
        'intelligence': {'search': 2},
        'wisdom': {'animals': 0, 'insight': 2, 'perception': 2},
        'charisma': {'deception': 0, 'intimidation': 0, 'persuasion': 4}, },
    'items': {
        'armor': {'wearable': ['light', 'medium']},
        'weapons': {'usable': ['simple', 'light', 'arms']}
    }
}


paladin = {
    'stats': {
        'class': 'Paladin', 'hit_die': 12},
    'skills': {
        'strength': {'athletics': 2},
        'dexterity': {'lockpick': 0, 'stealth': 0},
        'intelligence': {'search': 0},
        'wisdom': {'animals': 2, 'insight': 4, 'perception': 0},
        'charisma': {'deception': 0, 'intimidation': 2, 'persuasion': 2}, },
    'items': {
        'armor': {'wearable': ['light', 'medium', 'heavy']},
        'weapons': {'usable': ['simple', 'light', 'arms', 'heavy']}
    }
}

