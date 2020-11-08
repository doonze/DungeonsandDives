from dataclasses import dataclass


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
    Enter as Race, Str, Dex, Con, Wis, Int, Cha, Height, Weight, Age
    """

    Race_name: str = 'New'
    Str: int = 0
    Dex: int = 0
    Con: int = 0
    Wis: int = 0
    Int: int = 0
    Cha: int = 0
    Height: list = 0, 0
    Weight: list = 0, 0
    Age: list = 0, 0


@dataclass
class UserOptions:
    Type: str = 'User Options'
    Type_print: bool = True
    Type_speed: int = 200
    Loading_screen: bool = True


@dataclass
class Archetype:
    Class: str = "new"
    Hit_die: int = 0
    Weapons: list = 'Simple'
    Armor: list = 'None'
    Items: list = 'torch'
    Fitness: int = 0
    Nimbleness: int = 0
    Stealth: int = 0
    Awareness: int = 0
    Tame: int = 0
    Insight: int = 0
    Trickery: int = 0
    Imposing: int = 0
    Speech: int = 0

@dataclass
class Player:
    Player_race: Race
    Player_type: Archetype
    HP: int = 0
    AC: int = 0
    XP: int = 0


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
    Name: str
    Level: int
    Range: int
    Damage: int
    Description: str

