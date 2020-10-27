# Dungeons and Dives functions
from random import random
from random import randint
from time import sleep

import os


def typed_print(input_text, speed='1000', nl='\n'):
    input_text = input_text + nl
    for char in input_text:
        sleep(random() * 10.0 / float(speed))
        print(char, end='', flush=True)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def scroll(time, amount):
    for x in range(1, amount):
        print()
        sleep(time)


def dice(sides, rolls=1):
    roll = 0
    for d in range(rolls):
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
