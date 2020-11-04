# Dungeons And Dives main file
from modules.menu import *
from modules.options import user_options

# This is the main script for the program
if __name__ == '__main__':
    if user_options.Loading_screen:
        opening_banner()
    clear_screen()
    start_menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
