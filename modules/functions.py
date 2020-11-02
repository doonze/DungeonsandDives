# Dungeons and Dives functions
from dataclasses import fields
from random import random
from random import randint
from time import sleep
from modules.custom_classes import Colors, Race
import json
import os
from modules.options import user_options
from typing import get_type_hints

cb = Colors.BROWN
ce = Colors.END
cr = Colors.RED
cbl = Colors.BLINK
cg = Colors.GREEN


# todo: need to give all classes doc


def typed_print(input_text: str, speed=user_options.type_speed, typeing=user_options.type_print, new_line=True):
    """Simulates typed print output (typing). Feed it a string and it will type it out.\n
    input_text = String to type out\n
    speed = int for WPM to ne typed out (default pulled from user options)\n
    typing = True will show typing, false does normal prints (default pulled from user options)\n
    newline = True will return a new line once finished, False will not
    """

    if typeing:
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


def clear_screen():
    """Sends the clear screen command. Should work with both windows an linux"""
    os.system('cls' if os.name == 'nt' else 'clear')


def scroll(time: int, amount: int):
    """Scrolls the screen at a certain speed (time) and a certain amount (amount)."""
    for x in range(1, amount):
        print()
        sleep(time)


def dice(sides: int, rolls=1, reroll_ones=False):
    """Returns the results of simulated dice rolls.\n
    Provide (sides): d4 = 4, d6 =6 and so on\n
    If needed provide how many times to roll the dice (rolls), default is 1\n
    To reroll ones provide reroll_ones=True, default is False
    """
    roll = 0
    for d in range(rolls):
        loop_roll = randint(1, int(sides))
        if reroll_ones:
            while loop_roll == 1:
                loop_roll = randint(1, int(sides))
        roll += loop_roll
    return roll


def stat_bonus(stat: int):
    """Pass the function a stat, and it will return the correct bonus value"""
    if stat == 1:
        return -5
    if 2 <= stat <= 3:
        return -4
    if 4 <= stat <= 5:
        return -3
    if 6 <= stat <= 7:
        return -2
    if 8 <= stat <= 9:
        return -1
    if 10 <= stat <= 11:
        return 0
    if 12 <= stat <= 13:
        return 1
    if 14 <= stat <= 15:
        return 2
    if 16 <= stat <= 17:
        return 3
    if 18 <= stat <= 19:
        return 4
    if 20 <= stat <= 21:
        return 5
    if 22 <= stat <= 23:
        return 6
    if 24 <= stat <= 25:
        return 7
    if 26 <= stat <= 27:
        return 7
    if 28 <= stat <= 29:
        return 9
    if stat == 30:
        return 10


def feet_inch(inches: int):
    """Pass function a number of inches and it will return Feet' inches" ex: 5'6"
    """
    converted = divmod(inches, 12)
    feet = converted[0]
    inches = converted[1]
    result = (str(feet) + "'" + str(inches) + '"')
    return result


def save_char(save_dict: dict, file_name: str):
    """Pass function a character dictionary and a file name. It will save it to the specified file.\n
     If the file exist it will append to it, if not it will create it.
     """
    try:
        save_dict = [save_dict]
        keyed_dict = dict((item['name'], item) for item in save_dict)

        if os.path.exists(f'saves/{file_name}.json'):
            with open(f'saves/{file_name}.json') as f:
                loaded_json = json.load(f)
            loaded_json.update(keyed_dict)
            json_save = json.dumps(loaded_json, indent=2)
        else:
            json_save = json.dumps(keyed_dict, indent=2)

        f = open(f"saves/{file_name}.json", 'w')
        f.write(json_save)
        f.close()
    except Exception as ex:
        print(f'Something went wrong converting list to numbered dictionary: {ex}')


def list_to_num_dict(char_list):
    try:
        name_dict = {}
        num = 1

        for name in char_list:
            name_dict[f'{num}'] = name
            num += 1

        return name_dict
    except Exception as ex:
        print(f'Something went wrong converting list to numbered dictionary: {ex}')


def print_list(input_var, var_type='list', begin='', end='', new_line=True):
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
                    typed_print(f'{Colors.BROWN}({num}){Colors.END} {each}')
                    num += 1
                else:
                    typed_print(f'{Colors.BROWN}({num}){Colors.END} {each}', new_line=False)
                    num += 1
        elif var_type == 'dict':
            for i in input_var:
                typed_print(f'{Colors.BROWN}({i}){Colors.END} {input_var[i]}')
    except Exception as ex:
        print(f'Something went wrong printing from list in print_list: {ex}')


def pull_saved_data_indexes(path_file_name):
    try:
        with open(f'{path_file_name}') as f:
            loaded_json = json.load(f)
            index_list = []
            for index in loaded_json:
                index_list.append(index)
            return sorted(index_list, key=str.lower)
    except Exception as ex:
        print(f'Something went wrong pulling saved data indexes from dictionary: {ex}')


def pull_saved_data(path_file_name: str, index_name: str, class_name):
    try:
        with open(f'{path_file_name}') as f:
            loaded_json = json.load(f)
            index_dict = loaded_json[index_name]
            filled_class = class_name(**index_dict)
            return filled_class
    except Exception as ex:
        print(f'Something went wrong pulling saved data: {ex}')


def print_class_data(data_class):
    try:
        field_dict = {}
        for field in fields(data_class):
            field_dict[field.name] = field.type
            print(f'{field.name.capitalize():<8}: {cb}{str(getattr(data_class, field.name)):>2}{ce}')
        return field_dict
    except Exception as ex:
        print(f'Something went wrong printing class data: {ex}')


def edit_class_data(pulled_race, menu_choice: str, field_dict: dict):
    try:
        typed_print(f'Editing value {cb}[{menu_choice.capitalize()}]{ce}. Enter list separated by ,. '
                    f'The current value is {cb}[{getattr(pulled_race, menu_choice)}]{ce}: {cb}',
                    new_line=False)
        set_type = field_dict[menu_choice]
        while True:
            response = input()
            print(ce, end='')
            if set_type is list:
                response = response.translate(str.maketrans('', '', ' []'))
                response = [int(i) for i in response.split(',')]
                setattr(pulled_race, menu_choice, set_type(response))
            else:
                setattr(pulled_race, menu_choice, set_type(response))
            clear_screen()
            print_class_data(pulled_race)
            success = True
            return pulled_race, success
    except Exception as ex:
        print(f'Something went wrong: {ex}')
        success = False
        return pulled_race, success


def save_dictionary(save_dict: dict, path_file_name: str, index: str):
    """Pass function a dictionary (save_dict), a full path name (path_file_name), and the key you want
     the dictionary to be indexed by (index). It will create the file if it doesn't exist or append to the
     file if it does, creating a dictionary of dictionaries indexed by (index). Files are saved in json format.\n

     Valid paths:\n
     data/races.json\n
     data/classes.json\n
     data/options.json\n
     saves/char.json\n
     """
    try:
        save_dict = [save_dict]
        keyed_dict = dict((item[index], item) for item in save_dict)

        if os.path.exists(f'{path_file_name}'):
            with open(f'{path_file_name}') as f:
                loaded_json = json.load(f)
            loaded_json.update(keyed_dict)
            json_save = json.dumps(loaded_json, indent=4)
        else:
            json_save = json.dumps(keyed_dict, indent=4)

        f = open(f"{path_file_name}", 'w')
        f.write(json_save)
        f.close()
    except Exception as ex:
        print(f'Something went wrong in the save_dictionary function: {ex}')
