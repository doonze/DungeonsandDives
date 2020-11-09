# This is the main game file
from modules.functions import clear_screen


def start_game(player: str):
    clear_screen()
    input(f"And so it begins! You'll be playing as {player}!")
