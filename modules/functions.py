# Dungeons and Dives functions
from random import random
from random import randint
from time import sleep
import os


def typed_print(input_text, speed='200', nl='\n'):
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


def dice(sides):
    roll = randint(1, int(sides))
    return roll
