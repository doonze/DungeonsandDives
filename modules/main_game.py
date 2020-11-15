# This is the main game file
try:
    import curses
    from modules.custom_classes import Player, SubWin
    from modules.functions import clear_screen


    def start_main(screen, loaded_game):
        loaded_game: Player
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
        cyan = curses.color_pair(1)
        blue = curses.color_pair(2)
        yellow = curses.color_pair(3)
        green = curses.color_pair(4)
        magenta = curses.color_pair(5)
        red = curses.color_pair(6)
        white = curses.color_pair(7)

        def stats(name, hp, ac, xp, load_cur, load_max):
            length = len(name) + len(str(hp)) + len(str(ac)) + len(str(xp)) + \
                     len(str(load_cur)) + len(str(load_max)) + 31
            sub = SubWin(3, length, 0, 0)
            stat = screen.subwin(sub.ht, sub.lg, sub.y, sub.x)
            stat.attron(cyan)
            stat.box()
            stat.addstr(0, 1, "Stats:", yellow)
            stat.addstr(1, 1, 'Name: ', yellow)
            stat.addstr(f'{name} ', white)
            stat.addstr('HP: ', yellow)
            stat.addstr(f'{hp} ', green)
            stat.addstr('AC: ', yellow)
            stat.addstr(f'{ac} ', green)
            stat.addstr(f'Load: ', yellow)
            stat.addstr(f'{load_cur}/{load_max} ', green)
            stat.addstr('XP: ', yellow)
            stat.addstr(f'{xp}', blue)
            stat.refresh()
            screen.refresh()

        stats(loaded_game.Player_name,
              loaded_game.Current_HP,
              loaded_game.AC,
              loaded_game.XP,
              loaded_game.Current_weight,
              loaded_game.Carry_weight)
        screen.getch()

except Exception as ex:
    print(ex)
    input()
