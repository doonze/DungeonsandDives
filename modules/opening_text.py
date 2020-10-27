from modules.functions import *

CRED = '\033[91m'
CEND = '\33[0m'
CBLINK = '\33[5m'


def opening_banner():
    clear_screen()
    # scroll(0, 18)
    # print(r"                                    ,     \    /      , ")
    # print(r"                                   / \    )\__/(     / \ ")
    # print(r"                                  /   \  (_\  /_)   /   \ ")
    # print("                             ____/_____\\__\\" + CRED + "@  @" + CEND + "/___/_____\\____")
    # print(r"                            |             |\../|              |")
    # print(r"                            |              \VV/               |")
    # print(r"                            |        " + CRED + "Dungeons & Dives" + CEND + "         |")
    # print(r"                            |_________________________________|")
    # print(r"                             |    /\ /      \\       \ /\    |")
    # print(r"                             |  /   V        ))       V   \  |")
    # print(r"                             |/     `       //        '     \|")
    # print(r"                             `              V                '")
    # scroll(0.2, 18)
    # sleep(4)


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
