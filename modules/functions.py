# Dungeons and Dives functions
import json
import logging
import os
from dataclasses import fields
from random import randint
from random import random
from time import sleep
from typing import Dict
from modules.custom_classes import Colors
from modules.options import user_options
try:
    import readline
except ImportError:
    import pyreadline as readline
readline.parse_and_bind("tab: complete")


cb = Colors.brown
ce = Colors.end
cr = Colors.red
cbl = Colors.blink
cg = Colors.green
cbol = Colors.bold


def comp(comp_list=None):
    if comp_list is None:
        comp_list = []
    try:
        def completer(text, state):
            options = [cmd for cmd in comp_list if cmd.startswith(text)]
            if state < len(options):
                return options[state]
            else:
                return None

        readline.set_completer(completer)

    except Exception as ex:
        print(ex)


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


def stat_bonus(stat: int):
    """
    Pass the function a stat, and it will return the correct bonus value

    :param stat: Pass the stat
    :type stat: int
    :return: Stat bonus
    :rtype: int
    """
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


def save_char(save_dict: dict, file_name: str) -> None:
    """
    Pass function a character dictionary and a file name. It will save it to the specified file.

    If the file exist it will append to it, if not it will create it.

    :param save_dict: Dictionary to save
    :type save_dict: dict
    :param file_name: Filename to save to
    :type file_name: str
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


def list_to_num_dict(char_list: list) -> Dict[str, str]:
    """
    Pass this function a list and it will turn it into a numbered dictionary

    :param char_list: Pass a list type object
    :type char_list: list
    :return: Returns a dictionary with numbers for keys
    :rtype: dict
    """
    try:
        name_dict = {}
        num = 1

        for name in char_list:
            name_dict[f'{num}'] = name
            num += 1

        return name_dict
    except Exception as ex:
        print(f'Something went wrong converting list to numbered dictionary: {ex}')


def print_list(input_var, var_type='list', begin='', end='', new_line=True) -> None:
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


def pull_saved_data_indexes(path_file_name) -> list:
    """
    Pulls all the "indexes" from a saved json file. As all our saved data are indexed]
    dictionaries of dictionaries this pulls all the main index keys for that file.

    :param path_file_name: path/filename.extension format
    :type path_file_name: str
    :return: Returns a list of the indexes
    :rtype: list
    """
    try:
        with open(f'{path_file_name}') as f:
            loaded_json = json.load(f)
            index_list = []
            for index in loaded_json:
                index_list.append(index)
            return sorted(index_list, key=str.lower)
    except Exception as ex:
        print(f'Something went wrong pulling saved data indexes from dictionary: {ex}')


def pull_saved_data(path_file_name: str, index_name: str, class_name: type) -> object:
    """
    Pulls data from provided path for the provided index, returns a class object filled with the data from file

    :param path_file_name: path/filename.extension format
    :type path_file_name: str
    :param index_name: Index to pull info from in file
    :type index_name: str
    :param class_name: Class to fill with pulled info
    :type class_name: type
    :return: Returns a dataclass object
    :rtype: type
    """
    try:
        with open(f'{path_file_name}') as f:
            loaded_json = json.load(f)
            index_dict = loaded_json[index_name]
            filled_class = class_name(**index_dict)
            return filled_class
    except Exception as ex:
        print(f'Something went wrong pulling saved data: {ex}')


def print_class_data(data_class: object, col_one: str = '<10', col_two: str = '<2') -> dict:
    """
    Pass a class object and this function will print out it's fields and values

    :param data_class: dataclass you want to print
    :type data_class: object
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
            print(f'{field.name.capitalize():{col_one}}: {cb}{str(getattr(data_class, field.name)):{col_two}}{ce}')
        return field_dict
    except Exception as ex:
        print(f'Something went wrong printing class data: {ex}')


def edit_class_data(dataclass, menu_choice: str, field_dict: dict) -> (object, bool):
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
    :return: Returns a list containing the updated dataclass and a bool if it was successful
    :rtype: (object, bool)
    """
    try:
        typed_print(f'Editing value {cb}[{menu_choice.capitalize()}]{ce}. Enter list separated by ",". '
                    f'The current value is {cb}[{getattr(dataclass, menu_choice)}]{ce}: {cb}',
                    new_line=False)
        set_type = field_dict[menu_choice]
        while True:
            response = input()
            print(ce, end='')
            if set_type is list:
                response = response.translate(str.maketrans('', '', ' []'))
                response = [int(i) for i in response.split(',')]
                setattr(dataclass, menu_choice, set_type(response))
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
            print_class_data(dataclass)
            success = True
            return dataclass, success
    except Exception as ex:
        exception_log('', ex)
        # print(f'{cr}EXCEPTION RAISED:{ce} {ex}')
        success = False
        return dataclass, success


def save_dictionary(save_dict: dict, path_file_name: str, index: str, del_dict=False) -> None:
    """
     Pass function a dictionary (save_dict), a full path name (path_file_name), and the key
    you want the dictionary to be indexed by (index). You can also pass a empty dictionary, a path,
    an index to delete, and the del_dict=TRUE bool to delete a dictionary index.

     It will create the file if it doesn't exist or append to the file if it does,
    creating a dictionary of dictionaries indexed by (index). Files are saved in json format.

    Valid paths:
     data/races.json\n
     data/classes.json\n
     data/options.json\n
     saves/char.json\n

     :param save_dict: Dictionary to save to file (not used for deletes)
     :type save_dict: dict
     :param path_file_name: path/filename.extension format
     :type path_file_name: str
     :param index: Index to save it into the file under (or to delete)
     :type index: str
     :param del_dict: Bool on if the is for deleting a dictionary
     :type del_dict: bool
     """
    try:
        keyed_dict = {}  # Just to avoid assignment errors in code

        if not del_dict:  # If this wasn't called to delete a dictionary this runs
            #  We convert the passed dictionary to a dictionary list so we can then pull value out we
            #  want to index by. Then we index the whole dictionary by that value.
            save_dict = [save_dict]
            keyed_dict = dict((item[index], item) for item in save_dict)

        if os.path.exists(f'{path_file_name}'):
            with open(f'{path_file_name}') as f:
                loaded_json = json.load(f)
            if del_dict:  # If it was called to delete a dictionary just need the index to delete
                loaded_json.pop(index)  # This pops (deletes) the passed index name from dictionary
            else:
                loaded_json.update(keyed_dict)  # Adds the indexed dictionary to the existing dictionary of dictionaries
            json_save = json.dumps(loaded_json, indent=4)  # Then converts it to a json
        else:  # If file didn't already exist we create it with one single dict inside
            json_save = json.dumps(keyed_dict, indent=4)

        f = open(f"{path_file_name}", 'w')
        f.write(json_save)
        f.close()
    except Exception as ex:
        exception_log(f'Something went wrong in the save_dictionary function', ex)
