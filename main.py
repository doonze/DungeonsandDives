# Dungeons And Dives start_map_maker file
from modules.functions import clear_screen
from modules.menu import start_menu
from modules.options import user_options

# This is the start_map_maker script for the program
from modules.opening_text import opening_banner

if __name__ == '__main__':

    if user_options.Loading_screen:
        opening_banner()
    clear_screen()
    start_menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
