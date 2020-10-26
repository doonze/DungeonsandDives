from modules.functions import *
from modules.opening_text import *
from modules.create_char import char_creation


def start_menu():
    clear_screen()
    typed_print('Welcome to Dungeons and Dives!')
    typed_print('(1) Start a new game')
    typed_print('(2) Continue a saved game')
    typed_print('(3) Create a character')
    typed_print('(e) Exit game!')
    typed_print("Please enter an option [1-3,e]: ", nl='')
    while True:
        load_saved = input()
        if load_saved == '1':
            opening_text()
        elif load_saved == '3':
            char_creation()
        elif load_saved.lower() == 'e':
            raise SystemExit
        else:
            typed_print('Invalid option! Enter a number 1-3 or e to exit! [1-3,e]: ',nl='')





