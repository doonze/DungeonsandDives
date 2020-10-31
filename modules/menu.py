from modules.create_char import char_creation
from modules.opening_text import *

# todo: build options menu, with pull, edit, save
# This is the initial start menu
def start_menu():
    """Main menu"""
    clear_screen()
    typed_print(f'Welcome to Dungeons and Dives!')
    print()
    main_menu = {
        1: 'Start a new game',
        2: 'Continue a saved game',
        3: 'Skip intro and create a new character',
        4: 'Admin Menu',
        5: 'Options',
        'e': 'Exit game!'
    }
    print_list(main_menu, var_type='dict')
    print()
    typed_print(f"Please enter an option {cb}[1-5,e]{ce}: {cb}", new_line=False)

    while True:
        load_saved = input()
        print(f'{ce}', end='')
        if load_saved == '1':
            opening_text()
            break
        elif load_saved == '2':
            saved_game_menu()
            break
        elif load_saved == '3':
            char_creation()
            break
        elif load_saved == '4':
            admin_menu()
            break
        elif load_saved.lower() == 'e':
            raise SystemExit
        else:
            typed_print('Invalid option! Enter a number 1-3 or e to exit! [1-3,e]: ', new_line=False)


def saved_game_menu():
    clear_screen()
    typed_print('Here are the current saved games:')
    print()
    print_list(list_to_num_dict(pull_saved_char()), var_type='dict')
    print()
    typed_print(f'Select a saved game above or (C) to cancel {cb}[?, c]{ce}:{cb} ', new_line=False)

    while True:
        load_saved = input()
        print(ce, end='')
        if load_saved == '1':

            break
        elif load_saved == '3':

            break
        elif load_saved == '4':

            break
        elif load_saved.lower() == 'c':
            break
        else:
            typed_print(f'Invalid option! Select a saved game above or (C) to cancel {cb}[1-3,e]{ce}:{cb} '
                        f'', new_line=False)

    start_menu()


def admin_menu():
    clear_screen()
    typed_print(f'{cbl}{cr}WARNING!!!{ce} Use at your own risk, these are creation tools!!\n'
                f'It would be easy to break the game messing with these settings!')
    print()
    admin_items = {
        1: 'Races admin',
        2: 'Class admin',
        3: '...',
        4: '...',
        'c': 'Return to main menu!'
    }
    print_list(admin_items, var_type='dict')
    print()
    typed_print(f'Select 1-4 above or (C) to cancel {cb}[1-4, c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice == '1':
            races_admin_menu()
            break
        elif menu_choice == '3':

            break
        elif menu_choice == '4':

            break
        elif menu_choice.lower() == 'c':
            break
        else:
            typed_print(f'Invalid option! Enter a number 1-4 or e to exit! {cb}[1-4,c]{ce}:{cb} ', new_line=False)

    start_menu()

# todo: Need to add ways to create NEW races, and delete races
def races_admin_menu():
    clear_screen()
    pulled_saved_items = pull_saved_data_names('data/races.json')
    item_dict = list_to_num_dict(pulled_saved_items)
    typed_print('This is the administration menu for Races.')
    print()
    print_list(item_dict, var_type='dict')
    print()
    typed_print(f'Choose a choice above or (C) to return to the admin menu {cb}[?, c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            races_admin_edit(item_dict[menu_choice])
            break
        elif menu_choice.lower() == 'c':
            break
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)

    admin_menu()


def races_admin_edit(race):
    clear_screen()
    typed_print(f'You chose to edit {race}, here are the current values:')
    print()
    pulled_race = pull_saved_data('data/races.json', race, Race)
    field_list = print_class_data(pulled_race)
    print()
    typed_print(f'Enter a field to edit, or (C) to return to Races menu. '
                f'Example {cb}[str]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice in field_list:
            edited_race = edit_class_data(pulled_race, menu_choice)
            print()
            typed_print(f"Value was updated, enter another to edit or (S) to save: {cb}", new_line=False)
            continue
        elif menu_choice == 'c':
            break
        elif menu_choice == 's':
            save_dictionary(edited_race.__dict__, 'data/races.json', 'race')
            break
        else:
            typed_print(f'Value entered: {cb}{menu_choice}{ce} is not valid, please reenter: {cb} ', new_line=False)

    # If 'c' is chosen the loop it broken and we return to prev menu, this is used so we don't get unending while
    # loops nestled going through the menu's
    races_admin_menu()


def options_menu():
    clear_screen()
    typed_print(f'Options menu:')
    print()
    options_choices = {
        1: "User Menu"
    }
    print_list(options_choices, var_type='dict')
    print()
    typed_print(f'Enter options menu to view, or (C) to return to main menu {cb}[1,c]{ce}:{cb}')

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice == '1':

            break
        elif menu_choice == 'c':
            break
        else:
            typed_print(f' Value entered {cb}{menu_choice}{ce} is not valid, please reenter: {cb} ', new_line=False)

    start_menu()
