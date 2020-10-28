from modules.functions import *
from modules.opening_text import *
from modules.create_char import char_creation


# This is the initial start menu
def start_menu():
    clear_screen()
    typed_print('Welcome to Dungeons and Dives!')
    typed_print('(1) Start a new game')
    typed_print('(2) Continue a saved game')
    typed_print('(3) Create a character')
    typed_print('(4) Load saved game')
    typed_print('(e) Exit game!')
    typed_print("Please enter an option [1-3,e]: ", nl='')

    while True:
        load_saved = input()
        if load_saved == '1':
            opening_text()
            break
        elif load_saved == '3':
            char_creation()
            break
        elif load_saved == '4':
            saved_game_menu()
            break
        elif load_saved.lower() == 'e':
            raise SystemExit
        else:
            typed_print('Invalid option! Enter a number 1-3 or e to exit! [1-3,e]: ', nl='')


def saved_game_menu():
    clear_screen()
    saved_games = pull_saved_char()
    typed_print('Here are the current saved games:')
    name_dict = saved_char_list(saved_games)
    num = 1
    for i in name_dict:
        typed_print(f"({i}) {name_dict[i]}")
        num += 1
    typed_print('Select a saved game above: ')

    while True:
        load_saved = input()
        if load_saved == '1':
            opening_text()
            break
        elif load_saved == '3':
            char_creation()
            break
        elif load_saved == '4':
            saved_game_menu()
            break
        elif load_saved.lower() == 'e':
            raise SystemExit
        else:
            typed_print('Invalid option! Enter a number 1-3 or e to exit! [1-3,e]: ', nl='')

