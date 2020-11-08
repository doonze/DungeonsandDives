from modules.functions import *
from modules.terminalsize import get_terminal_size


CRED = '\033[91m'
CEND = '\33[0m'
CBLINK = '\33[5m'


def opening_banner():
    col, rows = get_terminal_size()
    sp = center_text(int((col/2) - (34/2)))
    clear_screen()
    scroll(0, rows - 12)
    print(f'{sp}'r"        ,     \    /      , ")
    print(f'{sp}'r"       / \    )\__/(     / \ ")
    print(f'{sp}'r"      /   \  (_\  /_)   /   \ ")
    print(f'{sp}'" ____/_____\\__\\" + Colors.red + "@  @" + Colors.end + "/___/_____\\____")
    print(f'{sp}'r"|             |\../|              |")

    print(f'{sp}'r"|              \VV/               |")
    print(f'{sp}'r"|        " + Colors.red + "Dungeons & Dives" + Colors.end + "         |")
    print(f'{sp}'r"|_________________________________|")
    print(f'{sp}'r" |    /\ /      \\       \ /\    |")
    print(f'{sp}'r" |  /   V        ))       V   \  |")
    print(f'{sp}'r" |/     `       //        '     \|")
    print(f'{sp}'r" `              V                '")
    scroll(0.1, int(round(rows/2 - 6)))
    sleep(3)
    scroll(0.1, int(round(rows / 2 + 7)))


def opening_text():
    clear_screen()
    typed_print("You are walking down the street...")
    sleep(1)
    print()
    typed_print('Minding your own damn business...')
    sleep(1)
    print()
    typed_print('The drone of traffic fills your ears, echoing off the skyscrapers\n'
                'that crowd the busy street. The air smells like rain, but a glance\n'
                'at the night sky still shows some stars shining through the racing\n'
                'clouds overhead.')
    print()
    sleep(2)
    input("Press enter to continue...")
    clear_screen()
    typed_print('Now some more stuff')
    sleep(2)
    print()
    input("Press enter to continue...")
