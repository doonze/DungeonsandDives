from modules.races import *
from modules.functions import dice, typed_print, clear_screen
import modules.menu


def char_creation():

    clear_screen()
    typed_print("Now let's pick a race!")
    typed_print("(1) Human")
    typed_print('(2) Elf')
    typed_print('(3) Dwarf')
    typed_print('Please choose one of the above or exit game [1-3,c]: ', nl='')

    while True:
        char_choice = input()
        if char_choice == '1':
            new_char_race(human)
        elif char_choice == '2':
            new_char_race(elf)
        elif char_choice == '3':
            new_char_race(dwarf)
        elif char_choice.lower() == 'c':
            modules.menu.start_menu()
        else:
            typed_print('Choice was not valid. Enter 1-3, or c to go back to main menu! [1-3,c]: ', nl='')


def new_char_race(race):
    new_char_stats = {
        'race': race['race'],
        'str': int(race['str']) + dice(6),
        'dex': int(race['dex']) + dice(6),
        'con': int(race['con']) + dice(6),
        'wis': int(race['wis']) + dice(6),
        'int': int(race['int']) + dice(6),
        'chr': int(race['chr']) + dice(6),
    }
    clear_screen()
    typed_print('Here are your characters stats:')
    typed_print('Race: ' + new_char_stats['race'])
    typed_print('Strength:     ' + str(new_char_stats['str']))
    typed_print('Dexterity:    ' + str(new_char_stats['dex']))
    typed_print('Constitution: ' + str(new_char_stats['con']))
    typed_print('Wisdom:       ' + str(new_char_stats['wis']))
    typed_print('Intelligence: ' + str(new_char_stats['int']))
    typed_print('Charisma:     ' + str(new_char_stats['chr']))
    print()
    typed_print("Do you want to cancel creation, reroll, or accept these stats? [C/R/A]: ", nl='')
    reroll = input()
    if reroll.lower() == "r":
        new_char_race(race)
    elif reroll.lower() == 'c':
        modules.menu.char_creation()
