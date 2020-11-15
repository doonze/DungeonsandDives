import curses

import modules.menu as menu
from modules.main_game import start_main
from modules.custom_classes import *
from modules.functions import *


# This function lets you pick your race
def char_creation():
    clear_screen()

    pulled_saved_items = pull_saved_data_indexes('data/races.json')
    item_dict = list_to_num_dict(pulled_saved_items)
    typed_print("Now let's pick a race!")
    print()
    print_list(item_dict, var_type='dict')
    print()
    typed_print(f'Please choose one of the above or cancel character creation {cb}[?,c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            return new_char_race(item_dict[menu_choice])
        elif menu_choice == 'c':
            return menu.start_menu()
        else:
            typed_print(f'Invalid option! Enter a number or c to return to admin menu! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)


# This function creates the chosen race and displays the results
def new_char_race(race):
    # This creates the new_char_stats dictionary, pulls the race settings from the races.py file
    # and randomly creates the details of the character using the parameters specified in the races file.
    pulled_race = pull_saved_data('data/races.json', race)
    first_run: bool = True

    def roll_char():
        pre_char_build = Player(Player_race=pulled_race)
        pre_char_build.Str = dice(6, rolls=3, reroll_ones=True) + pre_char_build.Player_race.Str
        pre_char_build.Dex = dice(6, rolls=3, reroll_ones=True) + pre_char_build.Player_race.Dex
        pre_char_build.Con = dice(6, rolls=3, reroll_ones=True) + pre_char_build.Player_race.Con
        pre_char_build.Wis = dice(6, rolls=3, reroll_ones=True) + pre_char_build.Player_race.Wis
        pre_char_build.Int = dice(6, rolls=3, reroll_ones=True) + pre_char_build.Player_race.Int
        pre_char_build.Cha = dice(6, rolls=3, reroll_ones=True) + pre_char_build.Player_race.Cha
        pre_char_build.Height = feet_inch(randint(int(pre_char_build.Player_race.Height[0]),
                                                  int(pre_char_build.Player_race.Height[1])))
        pre_char_build.Weight = randint(pre_char_build.Player_race.Weight[0], pre_char_build.Player_race.Weight[1])
        pre_char_build.Age = randint(pre_char_build.Player_race.Age[0], pre_char_build.Player_race.Age[1])

        # Here we figure out what the modifiers are for the above rolled stats
        str_bonus = stat_bonus(int(pre_char_build.Str), colored=True)
        dex_bonus = stat_bonus(int(pre_char_build.Dex), colored=True)
        con_bonus = stat_bonus(int(pre_char_build.Con), colored=True)
        wis_bonus = stat_bonus(int(pre_char_build.Wis), colored=True)
        int_bonus = stat_bonus(int(pre_char_build.Int), colored=True)
        cha_bonus = stat_bonus(int(pre_char_build.Cha), colored=True)
        clear_screen()

        # Here we start printing out the created character stats
        typed_print('Here are your characters stats:')
        print()
        typed_print(f"Race: {cb}{pre_char_build.Player_race.Race_name}{ce}")
        typed_print(f"Height: {cb}{pre_char_build.Height}{ce}")
        typed_print(f"Weight: {cb}{pre_char_build.Weight} lbs{ce}")
        typed_print(f"Age: {cb}{pre_char_build.Age}{ce}")
        print()
        typed_print(f"{'Attribute':<14} {'Stat':<4} Mod")
        typed_print('-----------------------')
        typed_print(f"{'Strength:':<14} {cb}{pre_char_build.Str:<4}{ce} {str(str_bonus):>2}")
        typed_print(f"{'Dexterity:':<14} {cb}{pre_char_build.Dex:<4}{ce} {str(dex_bonus):>2}")
        typed_print(f"{'Constitution:':<14} {cb}{pre_char_build.Con:<4}{ce} {str(con_bonus):>2}")
        typed_print(f"{'Wisdom:':<14} {cb}{pre_char_build.Wis:<4}{ce} {str(wis_bonus):>2}")
        typed_print(f"{'Intelligence:':<14} {cb}{pre_char_build.Int:<4}{ce} {str(int_bonus):>2}")
        typed_print(f"{'Charisma:':<14} {cb}{pre_char_build.Cha:<4}{ce} {str(cha_bonus):>2}")
        print()
        typed_print(f"Do you want to {cb}(C){ce}ancel creation, {cb}(R){ce}eroll, "
                    f"or {cb}(A){ce}ccept these stats? {cb}[c,r,a]{ce}:{cb} ", new_line=False)

        return pre_char_build

    char_build: Player = Player()
    if first_run:
        first_run ^= first_run
        char_build = roll_char()

    while True:
        reroll = input()
        print(ce, end='')
        if reroll.lower() == "r":
            char_build = roll_char()
            continue
        elif reroll.lower() == 'c':
            return menu.start_menu()
        elif reroll.lower() == 'a':
            return char_class_choice(char_build)
        else:
            typed_print('Invalid choice! Choose (C)ancel creation, (R)eroll, or (A)ccept! [c,r,a]:  ')


# This function is for choosing a class. The new_char_stats dictionary was passed to this function that was
# created in the previous function. This is so it can then be passed on and added to by the class creation function
def char_class_choice(char_build: Player):
    clear_screen()
    pulled_saved_items = pull_saved_data_indexes('data/archetype.json')
    item_dict = list_to_num_dict(pulled_saved_items)
    typed_print(f'Now choose an Archetype for your {char_build.Player_race.Race_name}!')
    print()
    print_list(item_dict, var_type='dict')
    print()
    typed_print(f'Please choose a class or ({cb}C{ce})ancel character creation {cb}[?,c]{ce}:{cb} ', new_line=False)

    while True:
        menu_choice = input().lower()
        print(ce, end='')
        if menu_choice in item_dict.keys():
            return char_class_build(char_build, item_dict[menu_choice])

        elif menu_choice == 'c':
            return {'Success': False}
        else:
            typed_print(f'Invalid option! Enter a number or ({cb}C{ce})ancel character creation! '
                        f'{cb}[?,c]{ce}:{cb} ', new_line=False)


# Once a class is chosen, here we start building the final aspects of the character, the new_char_stats dictionary
# has been passed down to the function and renamed char_stats
def char_class_build(char_build: Player, player_choice: str) -> dict:
    pulled_archetype = pull_saved_data('data/archetype.json', player_choice)
    char_build.Player_type = pulled_archetype

    # Here we're going to roll for hit points, breaking the processes out into the different parts so we can
    # lay it all out for the user then add the total hit points rolled into the dictionary
    try:
        hit_die = char_build.Player_type.Hit_die
        con_mod = stat_bonus(char_build.Con)
        dex_mod = stat_bonus(char_build.Dex)
        hp_roll = dice(hit_die, reroll_ones=True)
        tot_hp = hp_roll + con_mod + 8
        this_class = char_build.Player_type.Name
        this_race = char_build.Player_race.Race_name
        char_build.Max_HP = tot_hp

        # Now well figure out the base AC (10 + Dex mod) and add that to the dataclass
        char_build.AC = 10 + stat_bonus(char_build.Dex)

        # And the carry weight
        char_build.Carry_weight = 10 * char_build.Str

        clear_screen()
        typed_print(f'You have chosen to become a {this_race} {this_class}!')
        print()
        typed_print(f'Every race starts with {cb}8{ce} hit points. ')
        typed_print(f'You rolled a {cb}d{hit_die}{ce} for class hit points getting a roll of {cb}{hp_roll}{ce}.')
        typed_print(f'With your constitution modifier of {cb if con_mod >= 0 else cr}{con_mod}{ce} '
                    f'your total hit points are now {cb}{tot_hp}{ce}')
        print()
        typed_print(f'Your base armor class will be {cb}{char_build.AC}{ce}. '
                    f'(10 + Dexterity modifier of {cb if dex_mod >= 0 else cr}{dex_mod}{ce})')
        print()
        typed_print(f'Your carry weight will be {cb}{char_build.Carry_weight} lbs{ce} This is figured by'
                    f'(10 x Strength)')
        typed_print('Now enter a name for your character, then review character creation: ', new_line=False)
        char_build.Player_name = input()

        clear_screen()

        # Here we figure out what the final stats and modifiers are
        typed_print('Here are your final characters stats:')
        print()
        typed_print(f"You are a {cb}{char_build.Player_race.Race_name} {char_build.Player_type.Name}{ce}"
                    f" named {cy}{char_build.Player_name}{ce}.")
        print()
        typed_print(f"{'Height:':<14} {cb}{char_build.Height}{ce}")
        typed_print(f"{'Weight:':<14} {cb}{char_build.Weight} lbs{ce}")
        typed_print(f"{'Age:':<14} {cb}{char_build.Age}{ce}")
        typed_print(f"{'Hit points:':<14} {cb}{char_build.Max_HP}{ce}")
        typed_print(f"{'Armor Class:':<14} {cb}{char_build.AC}{ce}")
        typed_print(f"{'Max Load:':14} {cb}{char_build.Carry_weight}{ce}")
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
        typed_print('Choose (A)ccept to continue with this character or (C) to try again [a,c]: ', new_line=False)

        while True:
            final_choice = input()
            if final_choice.lower() == 'a':
                char_build.Current_HP = char_build.Max_HP
                save_dictionary(jsonpickle.encode(char_build), 'saves/char.json', char_build.Player_name)
                return curses.wrapper(start_main, char_build)
            elif final_choice.lower() == 'c':
                return menu.start_menu()
            else:
                typed_print('Choice was not valid. Enter A or C! [a,c]: ', new_line=False)
    except Exception as ex:
        print(f'Something went wrong in final character creation: {ex}')
        input('Press enter to continue to start menu....')
        return menu.start_menu()
