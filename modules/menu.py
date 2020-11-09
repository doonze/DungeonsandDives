from modules.create_char import char_creation
from modules.custom_classes import Race, Archetype, Player, UserOptions
from modules.opening_text import *


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
    typed_print(f"Please enter an option {cb}[1-5,e]{ce}:{cb} ", new_line=False)

    while True:
        response = input()
        print(f'{ce}', end='')
        if response == '1':
            opening_text()
            break
        elif response == '2':
            saved_game_menu()
            break
        elif response == '3':
            char_creation()
            break
        elif response == '4':
            admin_menu()
            break
        elif response == '5':
            options_menu()
            break
        elif response.lower() == 'e':
            raise SystemExit
        else:
            typed_print(f'Invalid option! Enter a number 1-5 or e to exit! {cb}[1-5,e]{ce}: ', new_line=False)


def saved_game_menu():
    """List all saved games"""
    clear_screen()
    pulled_saved_items = pull_saved_data_indexes('saves/char.json')
    item_dict = list_to_num_dict(pulled_saved_items)
    typed_print('Here are the current saved games:')
    print()
    print_list(item_dict, var_type='dict')
    print()
    typed_print(f'Select a saved game above or (C) to cancel {cb}[?, c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            load_saved(item_dict[menu_choice])
            break
        elif menu_choice == 'c':
            break
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)

    start_menu()


def load_saved(saved_game: str):
    clear_screen()
    typed_print(f'You chose to edit {saved_game}, here are the current values:')
    print()

    char_build: Player
    char_build = pull_saved_data('saves/char.json', saved_game)

    typed_print(f"You are a {char_build.Player_race.Race_name} {char_build.Player_type.Name}"
                f" named {char_build.Player_name}")
    typed_print(f"Height: {char_build.Height}")
    typed_print(f"Weight: {char_build.Weight} lbs")
    typed_print(f"Age: {char_build.Age}")
    typed_print(f'Hit point: {char_build.HP}')
    typed_print(f'Armor Class: {char_build.AC}')
    print()
    typed_print(f"{'Attribute':<14} {'Stat':<4} Mod")
    typed_print('-----------------------')
    typed_print(f"{'Strength:':<14} {char_build.Str:<4} {stat_bonus(char_build.Str, colored=True)}")
    typed_print(f"{'Dexterity:':<14} {char_build.Dex:<4} {stat_bonus(char_build.Dex, colored=True)}")
    typed_print(f"{'Constitution:':<14} {char_build.Con:<4} {stat_bonus(char_build.Con, colored=True)}")
    typed_print(f"{'Wisdom:':<14} {char_build.Wis:<4} {stat_bonus(char_build.Wis, colored=True)}")
    typed_print(f"{'Intelligence:':<14} {char_build.Int:<4} {stat_bonus(char_build.Int, colored=True)}")
    typed_print(f"{'Charisma:':<14} {char_build.Cha:<4} {stat_bonus(char_build.Cha, colored=True)}")
    print()
    input()


def admin_menu():
    """Menu for game admin options"""
    clear_screen()
    typed_print(f'{cbl}{cr}WARNING!!!{ce} Use at your own risk, these are creation tools!!\n'
                f'It would be easy to break the game messing with these settings!')
    print()
    admin_items = {
        1: 'Races admin',
        2: 'Archetype admin',
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
        elif menu_choice == '2':
            archetype_admin_menu()
            break
        elif menu_choice == '4':

            break
        elif menu_choice.lower() == 'c':
            break
        else:
            typed_print(f'Invalid option! Enter a number 1-4 or e to exit! {cb}[1-4,c]{ce}:{cb} ', new_line=False)

    start_menu()


def races_admin_menu():
    """Menu for editing, creating, or deleting races"""
    clear_screen()
    pulled_saved_items = pull_saved_data_indexes('data/races.json')
    item_dict = list_to_num_dict(pulled_saved_items)
    typed_print('This is the administration menu for Races.')
    print()
    print_list(item_dict, var_type='dict')
    print()
    typed_print(f'Choose a Race above, ({cb}N{ce}) to create new race,  or ({cb}C{ce}) to return to the admin menu'
                f' {cb}[?, c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            races_admin_edit(item_dict[menu_choice])
            break
        elif menu_choice == 'c':
            break
        elif menu_choice == 'n':

            races_admin_edit(Race(), new=True)
            break
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)

    admin_menu()


def races_admin_edit(race, new=False):
    """The actual edit interface for races"""
    edited: Race = Race()
    clear_screen()
    if new:
        typed_print(f"You've chosen to create a new Race.")
    else:
        typed_print(f'You chose to edit {cb}{race}{ce}, here are the current values:')
    print()
    if not new:
        pulled_race = pull_saved_data('data/races.json', race)
    else:
        pulled_race = race
    field_dict = print_class_data(pulled_race)
    print()
    typed_print(f'Enter a field to edit, ({cb}D{ce}) to delete race, or ({cb}C{ce}) to return to Races menu. '
                f'Example {cb}[Str]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice.lower().capitalize() in field_dict:
            menu_choice = menu_choice.lower().capitalize()
            edited_race = edit_class_data(pulled_race, menu_choice, field_dict, Race)
            edited = edited_race[0]
            success = edited_race[1]
            if success is True:
                print()
                typed_print(f"{cy}SUCCESS!{ce}, enter another to edit, ({cb}C{ce}) to cancel,"
                            f" or ({cb}S{ce}) to save: {cb}", new_line=False)
            else:
                typed_print(f'There was an error. Enter a field to edit, or ({cb}C{ce}) to return to Races menu. '
                            f'Example {cb}[Str]{ce}:{cb} ', new_line=False)
            continue
        elif menu_choice.lower() == 'c':
            break
        elif menu_choice.lower() == 's':
            save_dictionary(jsonpickle.encode(edited), 'data/races.json', edited.Race_name)
            break
        elif menu_choice.lower() == 'd':
            result = input(f'Are you SURE you wish to {cr}DELETE{ce} Race: {cb}{race}{ce} [yes,n]? ')
            if result.lower() == 'yes':
                edited_race = {}
                save_dictionary(edited_race, 'data/races.json', race, del_dict=True)
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
    pulled_saved_items = pull_saved_data_indexes('data/options.json')
    item_dict = list_to_num_dict(pulled_saved_items)
    print_list(item_dict, 'dict')
    print()
    typed_print(f'Enter options menu to view, or (C) to return to main menu {cb}[?,c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            options_edit(item_dict[menu_choice])
            break
        elif menu_choice == 'c':
            start_menu()
            break
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)

    start_menu()


def options_edit(options):
    """The actual edit interface for options"""
    edited: UserOptions = UserOptions()
    clear_screen()
    typed_print(f'You chose to edit {options}, here are the current values:')
    print()

    pulled_options = pull_saved_data('data/options.json', options)

    field_dict = print_class_data(pulled_options, "<15", '')

    print()
    typed_print(f'Enter a field to edit or (C) to return to options menu. '
                f'Example {cb}[Type_print]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice.lower().capitalize() in field_dict:
            menu_choice = menu_choice.lower().capitalize()
            edited_options = edit_class_data(pulled_options, menu_choice, field_dict, UserOptions)

            edited = edited_options[0]
            success = edited_options[1]
            if success is True:
                print()
                typed_print(f"Value was updated, enter another to edit, (C) to cancel,"
                            f" or (S) to save: {cb}", new_line=False)
            else:
                typed_print(f'That did not work. Enter a field to edit, or (C) to return to Races menu. '
                            f'Example {cb}[Type_speed]{ce}:{cb} ', new_line=False)
            continue
        elif menu_choice.lower() == 'c':
            break
        elif menu_choice.lower() == 's':
            save_dictionary(jsonpickle.encode(edited), 'data/options.json', edited.Type)
            break
        else:
            typed_print(f'Value entered: {cb}{menu_choice}{ce} is not valid, please reenter: {cb} ', new_line=False)

    # If 'c' is chosen the loop it broken and we return to prev menu, this is used so we don't get unending while
    # loops nestled going through the menu's
    options_menu()


def archetype_admin_menu():
    """Menu for editing, creating, or deleting archetypes"""
    clear_screen()
    pulled_saved_items = pull_saved_data_indexes('data/archetype.json')
    item_dict = list_to_num_dict(pulled_saved_items)
    typed_print('This is the administration menu for Archetypes.')
    print()
    print_list(item_dict, var_type='dict')
    print()
    typed_print(f'Choose a choice above, (N) to create new Archetype,  or (C) to return to the admin menu'
                f' {cb}[?, c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            archetype_admin_edit(item_dict[menu_choice])
            break
        elif menu_choice == 'c':
            break
        elif menu_choice == 'n':
            archetype_admin_edit(Archetype(), new=True)
            break
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)

    admin_menu()


def archetype_admin_edit(archetype, new=False):
    """The actual edit interface for archetype"""
    edited: Archetype = Archetype()
    clear_screen()
    if new:
        typed_print(f"You've chosen to create a new Archetype.")
    else:
        typed_print(f'You chose to edit {archetype}, here are the current values:')
    print()

    if not new:
        pulled_archetype = pull_saved_data('data/archetype.json', archetype)
    else:
        pulled_archetype = archetype
    field_dict = print_class_data(pulled_archetype)
    print()
    typed_print(f'Enter a field to edit, (D) to delete race, or (C) to return to Races menu. '
                f'Example {cb}[Str]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice.lower().capitalize() in field_dict:
            menu_choice = menu_choice.lower().capitalize()
            edited_archetype = edit_class_data(pulled_archetype, menu_choice, field_dict, Archetype)
            edited = edited_archetype[0]
            success = edited_archetype[1]
            if success is True:
                print()
                typed_print(f"Value was updated, enter another to edit or (S) to save: {cb}", new_line=False)
            else:
                typed_print(f'There was an error. Enter a field to edit, or (C) to return to Races menu. '
                            f'Example {cb}[Str]{ce}:{cb} ', new_line=False)
            continue
        elif menu_choice.lower() == 'c':
            break
        elif menu_choice.lower() == 's':
            save_dictionary(jsonpickle.encode(edited), 'data/archetype.json', edited.Name)
            break
        elif menu_choice.lower() == 'd':
            result = input(f'Are you SURE you wish to {cr}DELETE{ce} Race: {cb}{archetype}{ce} [yes,n]? ')
            if result.lower() == 'yes':
                edited_archetype = {}
                save_dictionary(edited_archetype, 'data/archetype.json', archetype, del_dict=True)
            break
        else:
            typed_print(f'Value entered: {cb}{menu_choice}{ce} is not valid, please reenter: {cb} ', new_line=False)

    # If 'c' is chosen the loop it broken and we return to prev menu, this is used so we don't get unending while
    # loops nestled going through the menu's
    archetype_admin_menu()
