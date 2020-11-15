from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Colors:
    # todo: fix these, ugly
    """ ANSI color codes """
    black: str = "\033[0;30m"
    red: str = "\033[0;31m"
    green: str = "\033[0;32m"
    brown: str = "\033[0;33m"
    blue: str = "\033[0;34m"
    purple: str = "\033[0;35m"
    cyan: str = "\033[0;36m"
    light_gray: str = "\033[0;37m"
    dark_gray: str = "\033[1;30m"
    light_red: str = "\033[1;31m"
    light_green: str = "\033[1;32m"
    yellow: str = "\033[1;33m"
    light_blue: str = "\033[1;34m"
    light_purple: str = "\033[1;35m"
    light_cyan: str = "\033[1;36m"
    light_while = "\033[1;37m"
    bold: str = "\033[1m"
    faint: str = "\033[2m"
    italic: str = "\033[3m"
    underline: str = "\033[4m"
    blink: str = "\033[5m"
    negative: str = "\033[7m"
    crossed: str = "\033[9m"
    end: str = "\033[0m"


@dataclass
class Race:
    """
    Enter as Race, Str, Dex, Con, Wis, Int, Cha, Height, Weight, Age, Desc
    """

    Race_name: str = 'New'
    Str: int = 0
    Dex: int = 0
    Con: int = 0
    Wis: int = 0
    Int: int = 0
    Cha: int = 0
    Height: tuple = (0, 0)
    Weight: tuple = (0, 0)
    Age: tuple = (0, 0)
    Desc: str = ''


@dataclass
class UserOptions:
    Type: str = 'User Options'
    Type_print: bool = True
    Type_speed: int = 200
    Loading_screen: bool = True


@dataclass
class Archetype:
    Name: str = "new"
    Hit_die: int = 0
    Weapons: tuple = 'Enter: simple, light, medium, arms'
    Armor: tuple = 'Enter: light, medium, heavy'
    Items: tuple = 'backpack'
    Fitness: int = 0
    Nimbleness: int = 0
    Stealth: int = 0
    Awareness: int = 0
    Tame: int = 0
    Insight: int = 0
    Trickery: int = 0
    Imposing: int = 0
    Speech: int = 0
    Spells: bool = False
    Spell_type: str = None
    Desc: str = ''


@dataclass
class SpellBook:
    Level_1: list
    Level_2: list
    Level_3: list
    Level_4: list
    Level_5: list
    Level_6: list
    Level_7: list
    Level_8: list
    Level_9: list


@dataclass
class Spells:
    Name: str = 'New'
    Type: str = 'Enter: arcane, holy, or nature'
    Level: int = 1
    Range: int = 0
    Damage: tuple = (0, 0)
    Desc: str = 'Spell description'


@dataclass
class Equipped:
    Head: str = None
    Neck: str = None
    Armor: str = 'Old Shirt'
    Waist: str = 'Cord Belt'
    Wrist: str = None
    Gloves: str = None
    Right_finger: str = None
    Left_finger: str = None
    Legs: str = 'Old Pants'
    Feet: str = 'Old Shoes'
    Left_hand: str = None
    Right_hand: str = None


@dataclass
class Player:
    Player_name: str = ''
    Player_race: Race = None
    Player_type: Archetype = None
    Player_spells: SpellBook = None
    Max_HP: int = 0
    AC: int = 0
    XP: int = 0
    Str: int = 0
    Dex: int = 0
    Con: int = 0
    Wis: int = 0
    Int: int = 0
    Cha: int = 0
    Height: str = ''
    Weight: int = 0
    Age: int = 0
    Current_HP: int = 0
    Inventory: List[str] = field(default_factory=list)
    Player_EQ: Equipped = None
    Carry_weight: float = 0.0
    Current_weight: float = 0.0
    Level: int = 1


@dataclass
class Items:
    Name: str = 'Item name'
    Class: str = 'Enter: common, magical, armor, weapon'
    Type: str = 'Enter: simple, light, medium, heavy, arms'
    Damage_dice: tuple = (0, 0)
    Uses: int = 0
    AC: int = 0
    Weight: float = 0
    Desc: str = None


@dataclass
class SubWin:
    """
    ht = Height of subwin\n
    lg = Length of subwin\n
    y = Y starting location\n
    x = X starting locaton\n
    """
    ht: int
    lg: int
    y: int
    x: int

