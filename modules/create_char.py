from modules.races import *
from modules.classes import *
from modules.functions import dice, typed_print, clear_screen, stat_bonus, feet_inch, save_char
import modules.menu
from random import randint


# This function lets you pick your race
def char_creation():

    clear_screen()

    typed_print("Now let's pick a race!")
    typed_print("(1) Human")
    typed_print('(2) Elf')
    typed_print('(3) Dwarf')
    typed_print('(4) Gnome')
    typed_print('(5) Halfling')
    typed_print('(6) Orc')
    typed_print('Please choose one of the above or cancel character creation [1-6,c]: ', nl='')

    while True:
        char_choice = input()
        if char_choice == '1':
            new_char_race(human)
            break
        elif char_choice == '2':
            new_char_race(elf)
            break
        elif char_choice == '3':
            new_char_race(dwarf)
            break
        elif char_choice == '4':
            new_char_race(gnome)
            break
        elif char_choice == '5':
            new_char_race(halfling)
            break
        elif char_choice == '6':
            new_char_race(orc)
            break
        elif char_choice.lower() == 'c':
            modules.menu.start_menu()
            break
        else:
            typed_print('Choice was not valid. Enter 1-6, or c to go back to main menu! [1-6,c]: ', nl='')


# This function creates the chosen race and displays the results
def new_char_race(race):

    # This creates the new_char_stats dictionary, pulls the race settings from the races.py file
    # and randomly creates the details of the character using the parameters specified in the races file.
    new_char_stats = {
        'race': race['race'],
        'str': int(race['str']) + dice(6, rolls=3, reroll_ones=True),
        'dex': int(race['dex']) + dice(6, rolls=3, reroll_ones=True),
        'con': int(race['con']) + dice(6, rolls=3, reroll_ones=True),
        'wis': int(race['wis']) + dice(6, rolls=3, reroll_ones=True),
        'int': int(race['int']) + dice(6, rolls=3, reroll_ones=True),
        'chr': int(race['chr']) + dice(6, rolls=3, reroll_ones=True),
        'height': feet_inch(randint(int(race['height'][0]), int(race['height'][1]))),
        'weight': str(randint(race['weight'][0], race['weight'][1])),
        'age': str(randint(race['age'][0], race['age'][1]))
    }

    # Here we figure out what the modifiers are for the above rolled stats
    str_stat = new_char_stats['str']
    str_bonus = stat_bonus(int(str_stat))
    dex_stat = new_char_stats['dex']
    dex_bonus = stat_bonus(int(dex_stat))
    con_stat = new_char_stats['con']
    con_bonus = stat_bonus(int(con_stat))
    wis_stat = new_char_stats['wis']
    wis_bonus = stat_bonus(int(wis_stat))
    int_stat = new_char_stats['int']
    int_bonus = stat_bonus(int(int_stat))
    chr_stat = new_char_stats['chr']
    chr_bonus = stat_bonus(int(chr_stat))
    clear_screen()

    # Here we start printing out the created character stats
    typed_print('Here are your characters stats:')
    typed_print(f"Race: {new_char_stats['race']}")
    typed_print(f"Height: {new_char_stats['height']}")
    typed_print(f"Weight: {new_char_stats['weight']} lbs")
    typed_print(f"Age: {new_char_stats['age']}")
    print()
    typed_print(f"{'Attribute':<14} {'Stat':<4} Mod")
    typed_print('-----------------------')
    typed_print(f"{'Strength:':<14} {str(str_stat):<4} {str(str_bonus):>2}")
    typed_print(f"{'Dexterity:':<14} {str(dex_stat):<4} {str(dex_bonus):>2}")
    typed_print(f"{'Constitution:':<14} {str(con_stat):<4} {str(con_bonus):>2}")
    typed_print(f"{'Wisdom:':<14} {str(wis_stat):<4} {str(wis_bonus):>2}")
    typed_print(f"{'Intelligence:':<14} {str(int_stat):<4} {str(int_bonus):>2}")
    typed_print(f"{'Charisma:':<14} {str(chr_stat):<4} {str(chr_bonus):>2}")
    print()
    typed_print("Do you want to (C)ancel creation, (R)eroll, or (A)ccept these stats? [c,r,a]: ", nl='')

    while True:
        reroll = input()
        if reroll.lower() == "r":
            new_char_race(race)
            break
        elif reroll.lower() == 'c':
            modules.menu.char_creation()
            break
        elif reroll.lower() == 'a':
            char_class_choice(new_char_stats)
            break
        else:
            typed_print('Invalid choice! Choose (C)ancel creation, (R)eroll, or (A)ccept! [c,r,a]:  ')


# This function is for choosing a class. The new_char_stats dictionary was passed to this function that was
# created in the previous function. This is so it can then be passed on and added to by the class creation function
def char_class_choice(char_stats):
    clear_screen()
    typed_print('Ok, now to choose a class!')
    typed_print('(1) Warrior')
    typed_print('(2) Thief')
    typed_print('(3) Magi')
    typed_print('(4) Monk')
    typed_print('(5) Strider')
    typed_print('(6) Cleric')
    typed_print('(7) Paladin')
    typed_print('Please choose a class or quit character creation [1-7,c]: ', nl='')

    while True:
        class_choice = input()
        if class_choice == '1':
            char_class(warrior, char_stats)
            break
        elif class_choice == '2':
            char_class(thief, char_stats)
            break
        elif class_choice == '3':
            char_class(magi, char_stats)
            break
        elif class_choice == '4':
            char_class(monk, char_stats)
            break
        elif class_choice == '5':
            char_class(strider, char_stats)
            break
        elif class_choice == '6':
            char_class(cleric, char_stats)
            break
        elif class_choice == '7':
            char_class(paladin, char_stats)
            break
        elif class_choice.lower() == 'c':
            modules.menu.start_menu()
            break
        else:
            typed_print('Choice was not valid. Enter 1-7, or c to go back to main menu! [1-7,c]: ', nl='')


# Once a class is chosen, here we start building the final aspects of the character, the new_char_stats dictionary
# has been passed down to the function and renamed char_stats
def char_class(class_choice, char_stats):

    # Here we're going to roll for hit points, breaking the processes out into the different parts so we can
    # lay it all out for the user then add the total hit points rolled into the dictionary
    hit_die = class_choice['stats']['hit_die']
    con_mod = stat_bonus(char_stats['con'])
    hp_roll = dice(hit_die, reroll_ones=True)
    tot_hp = hp_roll + con_mod + 8
    this_class = class_choice['stats']['class']
    this_race = char_stats['race']
    char_stats['hp'] = tot_hp
    char_stats['class'] = this_class

    # Now well figure out the base AC (10 + Dex mod) and add that to the dictionary
    base_ac = 10 + stat_bonus(char_stats['dex'])
    char_stats['ac'] = base_ac

    clear_screen()
    typed_print(f'You have chosen to become a {this_race} {this_class}!')
    print()
    typed_print('Every race starts with 8 hit points. ')
    typed_print(f'You rolled a d{hit_die} for class hit points getting a roll of {hp_roll}')
    typed_print(f'with your constitution modifier of {con_mod} your total hit points are now {tot_hp}')
    print()
    typed_print(f'Your base armor class will be {base_ac}. (10 + Dexterity modifier)')
    print()
    char_stats['name'] = input('Now enter a name for you character, then review character creation: ')

    clear_screen()

    # Here we figure out what the final stats and modifiers are
    str_stat = char_stats['str']
    str_bonus = stat_bonus(int(str_stat))
    dex_stat = char_stats['dex']
    dex_bonus = stat_bonus(int(dex_stat))
    con_stat = char_stats['con']
    con_bonus = stat_bonus(int(con_stat))
    wis_stat = char_stats['wis']
    wis_bonus = stat_bonus(int(wis_stat))
    int_stat = char_stats['int']
    int_bonus = stat_bonus(int(int_stat))
    chr_stat = char_stats['chr']
    chr_bonus = stat_bonus(int(chr_stat))
    typed_print('Here are your final characters stats:')
    print()
    typed_print(f"You are a {char_stats['race']} {char_stats['class']} named {char_stats['name']}")
    typed_print(f"Height: {char_stats['height']}")
    typed_print(f"Weight: {char_stats['weight']} lbs")
    typed_print(f"Age: {char_stats['age']}")
    typed_print(f'Hit point: {char_stats["hp"]}')
    typed_print(f'Armor Class: {char_stats["ac"]}')
    print()
    typed_print(f"{'Attribute':<14} {'Stat':<4} Mod")
    typed_print('-----------------------')
    typed_print(f"{'Strength:':<14} {str(str_stat):<4} {str(str_bonus):>2}")
    typed_print(f"{'Dexterity:':<14} {str(dex_stat):<4} {str(dex_bonus):>2}")
    typed_print(f"{'Constitution:':<14} {str(con_stat):<4} {str(con_bonus):>2}")
    typed_print(f"{'Wisdom:':<14} {str(wis_stat):<4} {str(wis_bonus):>2}")
    typed_print(f"{'Intelligence:':<14} {str(int_stat):<4} {str(int_bonus):>2}")
    typed_print(f"{'Charisma:':<14} {str(chr_stat):<4} {str(chr_bonus):>2}")
    print()

    typed_print('Choose (A)ccept to continue with this character or (C) to try again [a,c]: ', nl='')

    while True:
        final_choice = input()
        if final_choice.lower() == 'a':
            save_char(char_stats, 'char')
            break
        elif final_choice.lower() == 'c':
            char_creation()
            break
        else:
            typed_print('Choice was not valid. Enter A or C! [a,c]: ', nl='')
