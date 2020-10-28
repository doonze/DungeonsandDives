# Dungeons and Dives functions
from random import random
from random import randint
from time import sleep
import json
import os


def typed_print(input_text, speed='200', nl='\n'):
    # input_text = input_text + nl
    # for char in input_text:
    #     sleep(random() * 10.0 / float(speed))
    #     print(char, end='', flush=True)

    # when ready to turn back on, uncomment the above and delete the below
    if nl == '\n':
        print(f'{input_text}')
    else:
        print(f'{input_text}', end='')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def scroll(time, amount):
    for x in range(1, amount):
        print()
        sleep(time)


def dice(sides, rolls=1, reroll_ones=False):
    roll = 0
    for d in range(rolls):
        loop_roll = randint(1, int(sides))
        if reroll_ones:
            while loop_roll == 1:
                loop_roll = randint(1, int(sides))
        roll += loop_roll
    return roll


def stat_bonus(stat):
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


def feet_inch(inches):
    converted = divmod(inches, 12)
    feet = converted[0]
    inches = converted[1]
    result = (str(feet) + "'" + str(inches) + '"')
    return result


def save_char(save_dict, file_name):
    save_dict = [save_dict]
    keyed_dict = dict((item['name'], item) for item in save_dict)

    if os.path.exists(f'saves/{file_name}.json'):
        with open(f'saves/{file_name}.json') as f:
            loaded_json = json.load(f)
        loaded_json.update(keyed_dict)
        json_save = json.dumps(loaded_json, indent=2)
    else:
        list_dict = [keyed_dict]
        json_save = json.dumps(keyed_dict, indent=2)

    f = open(f"saves/{file_name}.json", 'w')
    f.write(json_save)
    f.close()


def pull_saved_char(file_name='char', pull_type="name"):
    with open(f'saves/{file_name}.json') as f:
        loaded_json = json.load(f)

    if pull_type == 'name':
        name_list = []
        for name in loaded_json:
            name_list.append(name)
        return name_list


def saved_char_list(char_list):
    name_dict = {}
    num = 1

    for name in char_list:
        name_dict[f'{num}'] = name
        num += 1

    return name_dict
