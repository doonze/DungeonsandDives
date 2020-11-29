# Dungeons and Dives functions

import logging
import os
from dataclasses import fields
from random import randint
from random import random
from textwrap import TextWrapper
from time import sleep
from modules.custom_classes import Colors, Items, Inventory
from modules.options import user_options
from uuid import uuid4

wrapper = TextWrapper(width=70)
cb = Colors.brown
ce = Colors.end
cr = Colors.red
cbl = Colors.blink
cg = Colors.green
cbol = Colors.bold
cy = Colors.cyan
lg = Colors.light_green
cp = Colors.purple


def center_text(spaces: int):
    ret_spaces = ' ' * spaces
    return ret_spaces


def exception_log(custom_text: str, ex: Exception):
    print(f'{cr}EXCEPTION RAISED:{ce} {custom_text} {ex}')
    logging.basicConfig(filename='error.log', filemode='a', level=logging.DEBUG, format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.error(custom_text, exc_info=True)


def typed_print(input_text: str, speed=user_options.Type_speed, typing=user_options.Type_print, new_line=True):
    """
    Simulates typed print output (typing).\n
    Feed it a string and it will type it out.\n
    Optional if you want typing or normal print output.

    :param input_text: Text to type out
    :type input_text: str
    :param speed: Words per min of typing speed (set in options)
    :type speed: int
    :param typing: Sets if output is typing or normal print (set in options)
    :type typing: bool
    :param new_line: Bool for if a new line will be returned
    :type new_line: bool
    """

    if typing:
        if new_line:
            input_text += '\n'
            for char in input_text:
                sleep(random() * 10.0 / float(speed))
                print(char, end='', flush=True)
        else:
            for char in input_text:
                sleep(random() * 10.0 / float(speed))
                print(char, end='', flush=True)
    else:
        if new_line:
            print(f'{input_text}')
        else:
            print(f'{input_text}', end='')


def clear_screen() -> None:
    """Sends the clear screen command. Should work with both windows an linux
    :rtype: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def scroll(time: float, amount: int):
    """Scrolls the screen at a set speed and amount.

    :rtype: None
    :param time: How fast the lines scroll
    :type time: float
    :param amount: How many lines it scrolls
    :type amount: int
    """
    for x in range(1, amount):
        print()
        sleep(time)


def dice(sides: int, rolls=1, reroll_ones=False):
    """
    Rolls a dice a number of times and returns the results.

    :param sides: How many sides the rolled dice have (d4, d6, etc)
    :type sides: int
    :param rolls: How many times to roll the dice
    :type rolls: int
    :param reroll_ones: If True any 1's are rerolled
    :type reroll_ones: bool
    :return: Returns an total of the dice rolls
    :rtype: int
    """
    roll = 0
    for d in range(rolls):
        loop_roll = randint(1, int(sides))
        if reroll_ones:
            while loop_roll == 1:
                loop_roll = randint(1, int(sides))
        roll += loop_roll
    return roll


def stat_bonus(stat: int, colored: bool = False) -> any:
    """
    Pass the function a stat, and it will return the correct bonus value

    :param stat: Pass the stat
    :type stat: int
    :param colored: True if formatted/colored string is desired
    :type colored: bool
    :return: Stat bonus as int or colored string (negative is red)
    :rtype: any
    """
    bonus_int = ''

    if stat == 1:
        bonus_int = -5
    if 2 <= stat <= 3:
        bonus_int = -4
    if 4 <= stat <= 5:
        bonus_int = -3
    if 6 <= stat <= 7:
        bonus_int = -2
    if 8 <= stat <= 9:
        bonus_int = -1
    if 10 <= stat <= 11:
        bonus_int = 0
    if 12 <= stat <= 13:
        bonus_int = 1
    if 14 <= stat <= 15:
        bonus_int = 2
    if 16 <= stat <= 17:
        bonus_int = 3
    if 18 <= stat <= 19:
        bonus_int = 4
    if 20 <= stat <= 21:
        bonus_int = 5
    if 22 <= stat <= 23:
        bonus_int = 6
    if 24 <= stat <= 25:
        bonus_int = 7
    if 26 <= stat <= 27:
        bonus_int = 7
    if 28 <= stat <= 29:
        bonus_int = 9
    if stat == 30:
        bonus_int = 10

    if colored:
        if bonus_int < 0:
            bonus_int = f'{cr}{bonus_int:>2}{ce}'
        else:
            bonus_int = f'{cb}{bonus_int:>2}{ce}'

    return bonus_int


def feet_inch(inches: int) -> str:
    """
    Pass function a number of inches and it will return Feet' inches" ex: 5'6"

    :param inches: Pass the number of inches
    :type inches: int
    :return: Feet and inches
    :rtype: str
    """
    converted = divmod(inches, 12)
    feet = converted[0]
    inches = converted[1]
    result = (str(feet) + "'" + str(inches) + '"')
    return result


def list_to_num_dict(list_of: list) -> dict:
    """
    Pass this function a list and it will turn it into a numbered dictionary

    :param list_of: Pass a list type object
    :type list_of: list
    :return: Returns a dictionary with numbers for keys
    :rtype: dict
    """
    try:
        name_dict = {}
        num = 1

        for each in list_of:
            name_dict[f'{num}'] = each
            num += 1

        return name_dict
    except Exception as ex:
        print(f'Something went wrong converting list to numbered dictionary: {ex}')


def print_list(input_var, var_type='dict', begin='', end='', new_line=True) -> None:
    """
    Pass this function a list or dictionary and it will print out all items in the object

    You can specify text to appear both before and after the item for list, and you can choose
    just a list of items (list) or a numbered list (num_list)

    :rtype: None
    :param input_var: List or dictionary
    :type input_var: Any
    :param var_type: Specify list, num_list, or dict
    :type var_type: str
    :param begin: For list option this text will appear before each item
    :type begin: str
    :param end: For list option this text will appear after each item
    :type end: str
    :param new_line: True will print a new line after each item (default True)
    :type new_line: bool
    """
    try:
        if var_type == "list":
            for each in input_var:
                if new_line:
                    typed_print(f'{begin}{each}{end}')
                else:
                    typed_print(f'{begin}{each}{end}', new_line=False)
        elif var_type == 'num_list':
            num = 1
            for each in input_var:
                if new_line:
                    typed_print(f'{Colors.brown}({num}){Colors.end} {each}')
                    num += 1
                else:
                    typed_print(f'{Colors.brown}({num}){Colors.end} {each}', new_line=False)
                    num += 1
        elif var_type == 'dict':
            for i in input_var:
                typed_print(f'{Colors.brown}({i}){Colors.end} {input_var[i]}')
    except Exception as ex:
        print(f'Something went wrong printing from list in print_list: {ex}')


def print_class_data(data_class: any, col_one: str = '<10', col_two: str = '<2') -> dict:
    """
    Pass a class object and this function will print out it's fields and values

    :param data_class: dataclass you want to print
    :type data_class: any
    :param col_one: Width of key column with justification (<^>) Ex. '<2'
    :type col_one: str
    :param col_two: Width of value column with justification (<^>) Ex. '<10'
    :type col_two: str
    :return: Returns a list of the objects field names(key) and their types(value)
    :rtype: dict
    """

    try:
        field_dict = {}
        for field in fields(data_class):
            field_dict[field.name] = field.type
            if field.name == "Desc":
                print()
                print(f'{field.name}:')
                print()
                print(f'{cy}{wrapper.fill(str(getattr(data_class, field.name))):{col_two}}{ce}')
            else:
                print(f'{field.name:{col_one}}: {cb}{str(getattr(data_class, field.name)):{col_two}}{ce}')
        return field_dict
    except Exception as ex:
        print(f'Something went wrong printing class data: {ex}')


def edit_class_data(dataclass, menu_choice: str, field_dict: dict, class_type) -> (any, bool):
    """
    Pass a dataclass(dataclass), a key in the dataclass(menu_choice), and a dictionary of the
    key names as keys and the types as values. It will ensure the data is updated with the correct
    type. It will return the dataclass with the key:value updated.

    :param dataclass: Pass a dataclass object
    :type dataclass: object
    :param menu_choice: Name of key to update
    :type menu_choice: str
    :param field_dict: Dictionary of {keys:types}
    :type field_dict: dict
    :param class_type: Pass dataclass
    :type class_type: any
    :return: Returns a list containing the updated dataclass and a bool if it was successful
    :rtype: (any, bool)
    """
    dataclass: class_type
    try:
        typed_print(f'Editing value {cb}[{menu_choice}]{ce}. Enter list separated by ",". '
                    f'The current value is {cb}[{getattr(dataclass, menu_choice)}]{ce}: {cb}',
                    new_line=False)
        set_type = field_dict[menu_choice]
        while True:
            response = input().strip()
            print(ce, end='')
            responses = []
            if set_type is list:
                response = response.translate(str.maketrans('', '', '[]'))
                response = [i.strip() for i in response.split(',')]
                for each in response:
                    if each.isdigit():
                        responses.append(int(each))
                    else:
                        responses.append(each)
                setattr(dataclass, menu_choice, set_type(responses))
            elif set_type is tuple:
                response = response.translate(str.maketrans('', '', '()'))
                response = [i.strip() for i in response.split(',')]
                for each in response:
                    if each.isdigit():
                        responses.append(int(each))
                    else:
                        responses.append(each)

                setattr(dataclass, menu_choice, set_type((tuple(responses))))
            else:
                if type(set_type(response)) == bool:
                    if response == 'False':
                        response = False
                    elif response == 'True':
                        response = True
                    else:
                        raise Exception(f'"{cb}{response}{ce}" was not a True/False answer!')
                setattr(dataclass, menu_choice, set_type(response))
            clear_screen()
            typed_print(wrapper.fill(f'{cb}{menu_choice}{ce} was updated to {cb}{response}{ce}!'))
            print()
            print_class_data(dataclass)
            success = True
            return dataclass, success
    except Exception as ex:
        exception_log(f'{cr}EXCEPTION:{ce} Problem while editing class data - ', ex)
        success = False
        return dataclass, success


def create_uuid():
    """
    Creates then returns a UUID

    :return: Hex UUID string
    :rtype: str
    """
    id_hex = uuid4()
    return id_hex.hex


def map_items_to_inventory(item, player_name):
    """
    Function to turn standard world items into inventory items. Every item becomes a unique item when added
    to inventory.

    :param item: Item dataclass object
    :type item: any
    :param player_name: Player who's item it's now become
    :type player_name: str
    :return: Returns a unique inventory dataclass item
    :rtype: any
    """
    item: Items = item
    inv: Inventory = Inventory()
    inv.Player_name = player_name
    inv.Name = item.Name
    inv.UUID = create_uuid()
    inv.Class = item.Class
    inv.Type = item.Type
    inv.Damage_dice = item.Damage_dice
    inv.Uses = item.Uses
    inv.AC = item.AC
    inv.Weight = item.Weight
    inv.Wear = item.Wear
    inv.Wear_chance = item.Wear_chance
    inv.Desc = item.Desc

    return inv
