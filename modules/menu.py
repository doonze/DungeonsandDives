import curses
from modules.db_functions import db_create_connection, db_select_values_where, db_return_class_object, \
    db_insert_class_in_table, db_update_class_in_table, db_delete_row, db_select_values, db_create_inventory_dict
from modules.map_maker import launch_map_maker
from modules.create_char import char_creation
from modules.custom_classes import Race, Archetype, Player, UserOptions, Items, NPCRace
from modules.opening_text import *
from modules.main_game import start_main


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
            return opening_text()
        elif response == '2':
            return saved_game_menu()
        elif response == '3':
            return char_creation()
        elif response == '4':
            return admin_menu()
        elif response == '5':
            return options_menu()
        elif response.lower() == 'e':
            raise SystemExit
        else:
            typed_print(f'Invalid option! Enter a number 1-5 or e to exit! {cb}[1-5,e]{ce}: ', new_line=False)


def saved_game_menu():
    """List all saved games"""
    clear_screen()
    saves_list = []
    conn = db_create_connection()
    pulled_saves = db_select_values(conn, 'saves', 'player_name')
    if len(pulled_saves) > 0:
        for row in pulled_saves:
            saves_list.append(row['player_name'])
    else:
        typed_print('There are no saved games yet, hit enter key to return to start menu......',
                    new_line=False)
        input()
        return start_menu()

    item_dict = list_to_num_dict(saves_list)
    typed_print('Here are the current saved games:')
    print()
    print_list(item_dict, var_type='dict')
    print()
    typed_print(f'Select a saved game above or (C) to cancel {cb}[?, c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            return load_saved(item_dict[menu_choice])
        elif menu_choice == 'c':
            return start_menu()
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)


def load_saved(saved_game: str):
    clear_screen()

    typed_print(f'Here are the current values for {cy}{saved_game}{ce}:')
    print()

    # char_build: Player
    conn = db_create_connection()
    char_build: Player = db_return_class_object(conn, 'saves', 'player_name', saved_game, Player)
    char_build.Race_details = db_return_class_object(conn, 'races', 'name', char_build.Player_race, Race)
    char_build.Arch_details = db_return_class_object(conn, 'archetype', 'name', char_build.Player_type, Archetype)
    char_build.Inventory = db_create_inventory_dict(conn, char_build.Player_name)
    conn.close()

    typed_print(f"You are a {cb}{char_build.Player_race} {char_build.Player_type}{ce}"
                f" named {cy}{char_build.Player_name}{ce}.")
    print()
    typed_print(f"{'Level:':<14} {cb}{char_build.Level}{ce}")
    typed_print(f"{'XP:':<14} {cb}{char_build.XP}{ce}")
    typed_print(f"{'Height:':<14} {cb}{char_build.Height}{ce}")
    typed_print(f"{'Weight:':<14} {cb}{char_build.Weight} lbs{ce}")
    typed_print(f"{'Age:':<14} {cb}{char_build.Age}{ce}")
    typed_print(f"{'Hit points:':<14} {cb}{char_build.Current_HP}{ce}")
    typed_print(f"{'Armor Class:':14} {cb}{char_build.AC}{ce}")
    typed_print(f"{'Load/Max Load:':14} {cb}{char_build.Current_weight}/{char_build.Carry_weight}{ce}")
    print()
    typed_print(f"{cbol}{lg}{'Attribute':<14} {'Stat':<4} Mod{ce}")
    typed_print('-----------------------')
    typed_print(f"{'Strength:':<14} {cb}{char_build.Str:<4}{ce} {stat_bonus(char_build.Str, colored=True)}")
    typed_print(f"{'Dexterity:':<14} {cb}{char_build.Dex:<4}{ce} {stat_bonus(char_build.Dex, colored=True)}")
    typed_print(f"{'Constitution:':<14} {cb}{char_build.Con:<4}{ce} {stat_bonus(char_build.Con, colored=True)}")
    typed_print(f"{'Wisdom:':<14} {cb}{char_build.Wis:<4}{ce} {stat_bonus(char_build.Wis, colored=True)}")
    typed_print(f"{'Intelligence:':<14} {cb}{char_build.Int:<4}{ce} {stat_bonus(char_build.Int, colored=True)}")
    typed_print(f"{'Charisma:':<14} {cb}{char_build.Cha:<4}{ce} {stat_bonus(char_build.Cha, colored=True)}")
    print()
    typed_print(f'Type ({cb}l{ce})oad, ({cb}c{ce})ancel, or ({cb}d{ce})elete '
                f'to continue: {cb}[l, d, c]{ce}:{cb} ', new_line=False)

    while True:
        load_response = input()
        print(ce, end='')
        if load_response.lower() == 'l':
            return curses.wrapper(start_main, char_build)
        elif load_response.lower() == 'd':
            typed_print(f'{cr}WARNING!!!{ce} are you SURE you wish to delete saved game {cy}{saved_game}{ce}?'
                        f' {cb}[Yes,no]{ce}:{cb} ', new_line=False)
            delete = input()
            print(ce, end='')
            if delete.lower() == 'yes':
                conn = db_create_connection()
                db_delete_row(conn, 'saves', 'player_name', saved_game)
                conn.close()
            return saved_game_menu()
        elif load_response.lower() == 'c':
            return saved_game_menu()
        else:
            typed_print(f'Invalid response: "{cb}{load_response}{ce}". Type ({cb}l{ce})oad'
                        f', ({cb}c{ce})ancel, or ({cb}d{ce})elete to continue: {cb}[l, d, c]{ce}:{cb} ', new_line=False)
            continue


def admin_menu():
    """Menu for game admin options"""
    clear_screen()
    typed_print(f'{cbl}{cr}WARNING!!!{ce} Use at your own risk, these are creation tools!!\n'
                f'It would be easy to break the game messing with these settings!')
    print()
    admin_items = {
        1: 'Races admin',
        2: 'Archetype admin',
        3: 'Item admin',
        4: 'Map admin',
        'c': 'Return to start menu!'
    }
    print_list(admin_items, var_type='dict')
    print()
    typed_print(f'Select 1-4 above or (C) to cancel {cb}[1-4, c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice == '1':
            return races_admin_menu()
        elif menu_choice == '2':
            return archetype_admin_menu()
        elif menu_choice == '3':
            return item_admin_menu()
        elif menu_choice == '4':
            launch_map_maker()
            return admin_menu()
        elif menu_choice.lower() == 'c':
            return start_menu()
        else:
            typed_print(f'Invalid option! Enter a number 1-4 or e to exit! {cb}[1-4,c]{ce}:{cb} ', new_line=False)


def races_admin_menu():
    """Menu for editing, creating, or deleting races"""
    conn = db_create_connection()
    clear_screen()
    print('What type of race do you wish to work with?')
    print()

    race_type = {1: 'Player Character (PC)',
                 2: 'Non-Player Character (NPC)'}
    print_list(race_type, var_type='dict')

    print()
    print(f'Choose an option or ({cb}c{ce}) to cancel: {cb}', end='')

    while True:
        type_choice = input()
        print(ce, end='')

        if type_choice == '1' or type_choice == '2':
            races_list = []
            if type_choice == '1':
                dataclass_type = Race()
                table = 'races'
                results = db_select_values(conn, 'races', 'name')
                for row in results:
                    races_list.append(row['name'])
            else:
                dataclass_type = NPCRace()
                table = 'npcraces'
                results = db_select_values(conn, 'npcraces', 'name')
                for row in results:
                    races_list.append(row['name'])
            conn.close()
            item_dict = list_to_num_dict(races_list)
            break
        elif type_choice == 'c':
            return admin_menu()
        else:
            print(f'{cb}{type_choice}{ce} was not a valid choice, try again: {cb}', end='')

    clear_screen()

    typed_print(f'This is the administration menu for {"Player" if type_choice == "1" else "NPC"} Races.')
    print()
    print_list(item_dict, var_type='dict')
    print()
    typed_print(f'Choose a Race above, ({cb}N{ce}) to create new race,  or ({cb}C{ce}) to return to the admin menu'
                f' {cb}[?, n, c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            return races_admin_edit(dataclass_type, table, item_dict[menu_choice])
        elif menu_choice.lower() == 'c':
            return admin_menu()
        elif menu_choice.lower() == 'n':
            return races_admin_edit(dataclass_type, table, new=True)
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)


def races_admin_edit(dataclass, table, race=None, new=False):
    """The actual edit interface for races"""

    edited: dataclass = dataclass
    clear_screen()
    if new:
        typed_print(f"You've chosen to create a new Race.")
    else:
        typed_print(f'You chose to edit {cb}{race}{ce}, here are the current values:')
    print()

    if not new:
        conn = db_create_connection()
        pulled_race = db_return_class_object(conn, table, 'name', race, dataclass)
        conn.close()
    else:
        pulled_race = dataclass

    field_dict = print_class_data(pulled_race)
    print()
    typed_print(f'Enter a field to edit, ({cb}d{ce}) to delete race, or ({cb}c{ce}) to return to Races menu. '
                f'Example {cb}[Name]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice in field_dict:
            edited_race = edit_class_data(pulled_race, menu_choice, field_dict, dataclass)
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
            return races_admin_menu()
        elif menu_choice.lower() == 's':
            conn = db_create_connection()
            if not new:
                db_update_class_in_table(conn, edited, table, 'name', edited.Name)
            else:
                db_insert_class_in_table(conn, edited, table)
            conn.close()
            return races_admin_menu()
        elif menu_choice.lower() == 'd':
            result = input(f'Are you SURE you wish to {cr}DELETE{ce} Race: {cb}{race}{ce} [yes,n]? ')
            if result.lower() == 'yes':
                conn = db_create_connection()
                db_delete_row(conn, table, 'name', race)
                conn.close()
                return races_admin_menu()
            else:
                input(f'Race: {cb}{race}{ce} was not deleted. Press enter to continue...')
                return races_admin_menu()
        else:
            typed_print(f'Value entered: {cb}{menu_choice}{ce} is not valid, please reenter: {cb} ', new_line=False)


def options_menu():
    clear_screen()
    typed_print(f'Options menu:')
    print()
    options_list = []
    conn = db_create_connection()
    results = db_select_values(conn, 'useroptions', 'type')
    for row in results:
        options_list.append(row['type'])
    conn.close()
    item_dict = list_to_num_dict(options_list)
    print_list(item_dict, 'dict')
    print()
    typed_print(f'Enter options menu to view, or (C) to return to start menu {cb}[?,c]{ce}:{cb} ',
                new_line=False)

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            return options_edit(item_dict[menu_choice])
        elif menu_choice == 'c':
            return start_menu()
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)


def options_edit(options):
    """The actual edit interface for options"""
    edited: UserOptions = UserOptions()
    clear_screen()
    typed_print(f'You chose to edit {options}, here are the current values:')
    print()

    conn = db_create_connection()
    pulled_options = db_return_class_object(conn, 'useroptions', 'type', options, UserOptions)
    conn.close()

    field_dict = print_class_data(pulled_options, "<15", '')

    print()
    typed_print(f'Enter a field to edit or (C) to return to options menu. '
                f'Example {cb}[Type_print]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice in field_dict:
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
            return options_menu()
        elif menu_choice.lower() == 's':
            conn = db_create_connection()
            with conn:
                db_update_class_in_table(conn, edited, 'useroptions', 'type', 'User Options')
            conn.close()
            return options_menu()
        else:
            typed_print(f'Value entered: {cb}{menu_choice}{ce} is not valid, please reenter: {cb} ', new_line=False)

    # If 'c' is chosen the loop it broken and we return to prev menu, this is used so we don't get unending while
    # loops nestled going through the menu'


def archetype_admin_menu():
    """Menu for editing, creating, or deleting archetypes"""
    clear_screen()
    options_list = []
    conn = db_create_connection()
    results = db_select_values(conn, 'archetype', 'name')
    for row in results:
        options_list.append(row['name'])
    conn.close()
    item_dict = list_to_num_dict(options_list)
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
            return archetype_admin_edit(item_dict[menu_choice])
        elif menu_choice == 'c':
            return admin_menu()
        elif menu_choice == 'n':
            return archetype_admin_edit(Archetype(), new=True)
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)


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
        conn = db_create_connection()
        pulled_archetype = db_return_class_object(conn, 'archetype', 'name', archetype, Archetype())
    else:
        pulled_archetype = archetype

    field_dict = print_class_data(pulled_archetype)
    print()
    typed_print(f'Enter a field to edit, (D) to delete race, or (C) to return to Races menu. '
                f'Example {cb}[Str]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        if menu_choice in field_dict:
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
            return archetype_admin_menu()
        elif menu_choice.lower() == 's':
            conn = db_create_connection()
            if new:
                db_insert_class_in_table(conn, edited, 'archetype')
            else:
                db_update_class_in_table(conn, edited, 'archetype', 'name', edited.Name)
            conn.close()
            return archetype_admin_menu()
        elif menu_choice.lower() == 'd':
            result = input(f'Are you SURE you wish to {cr}DELETE{ce} Archetype: {cb}{archetype}{ce} [yes,n]? ')
            if result.lower() == 'yes':
                conn = db_create_connection()
                db_delete_row(conn, 'archetype', 'name', archetype)
                conn.close()
                return archetype_admin_menu()
            else:
                input(f'Archetype: {cb}{archetype}{ce} not deleted! Press enter to continue...')
                return archetype_admin_menu()
        else:
            typed_print(f'Value entered: {cb}{menu_choice}{ce} is not valid, please reenter: {cb} ', new_line=False)


def item_admin_menu():
    """Menu for editing, creating, or deleting items"""
    clear_screen()
    conn = db_create_connection()
    item_list = []
    pulled_items = db_select_values(conn, 'items', 'name')
    for row in pulled_items:
        item_list.append(row['name'])
    item_dict = list_to_num_dict(item_list)
    typed_print('This is the administration menu for Items.')
    print()
    print_list(item_dict, var_type='dict')
    print()
    typed_print(f'Choose an item above, ({cb}n{ce})ew to create new item,  or ({cb}c{ce})ancel to return to '
                f'the admin menu{cb}[?, n, c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            return item_admin_edit(item_dict[menu_choice])
        elif menu_choice == 'c':
            return admin_menu()
        elif menu_choice == 'n':
            return item_admin_edit(Items(), new=True)
        else:
            typed_print(f'Invalid option! Enter a number, n, or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)


def item_admin_edit(item, new=False):
    """The actual edit interface for items"""
    edited: Items = Items()
    clear_screen()
    if new:
        typed_print(f"You've chosen to create a new Item.")
    else:
        typed_print(f'You chose to edit {cb}{item}{ce}, here are the current values:')
    print()
    if not new:
        conn = db_create_connection()
        pulled_item = db_return_class_object(conn, 'items', 'name', item, Items)
    else:
        pulled_item = item
    field_dict = print_class_data(pulled_item, col_one='<12', col_two='<30')
    print()
    typed_print(f'Enter a field to edit, ({cb}d{ce})elete to delete item, or ({cb}c{ce})ancel to return'
                f' to Items menu. Example {cb}[Name]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input()
        print(ce, end='')
        edited: Items
        if menu_choice in field_dict:
            edited_item = edit_class_data(pulled_item, menu_choice, field_dict, Items)
            edited = edited_item[0]
            success = edited_item[1]
            if success is True:
                print()
                typed_print(f"{cy}SUCCESS!{ce}, enter another to edit, ({cb}C{ce}) to cancel,"
                            f" or ({cb}S{ce}) to save: {cb}", new_line=False)
            else:
                typed_print(f'There was an error. Enter a field to edit, or ({cb}C{ce}) to return to Items menu. '
                            f'Example {cb}[Name]{ce}:{cb} ', new_line=False)
            continue
        elif menu_choice.lower() == 'c':
            return item_admin_menu()
        elif menu_choice.lower() == 's':
            conn = db_create_connection()
            if new:
                db_insert_class_in_table(conn, edited, 'items')
            else:
                db_update_class_in_table(conn, edited, 'items', 'name', edited.Name)
            conn.close()
            return item_admin_menu()
        elif menu_choice.lower() == 'd':
            result = input(f'Are you SURE you wish to {cr}DELETE{ce} item: {cb}{item}{ce} [yes,n]? ')
            if result.lower() == 'yes':
                conn = db_create_connection()
                db_delete_row(conn, 'items', 'name', item)
                return item_admin_menu()
            else:
                input(f'Item: {cb}{item}{ce} was not deleted. Press enter to continue...')
                return item_admin_menu()
        else:
            typed_print(f'Value entered: {cb}{menu_choice}{ce} is not valid, please reenter: {cb} ', new_line=False)
