# Map functions file
def input_list(win, yellow, green):
    input_dict = {1: '║',
                  2: '═',
                  3: '╝',
                  4: '╗',
                  5: '╔',
                  6: '╣',
                  7: '╚',
                  8: '╠',
                  9: '╦',
                  0: '╩'
                  }

    ly = 0
    for key in input_dict:
        win.addstr(ly, 0, f'{str(key)}:', yellow)
        win.addstr(ly, 3, f' {input_dict[key]}', green)
        ly += 1

    return input_dict


def set_colors(screen, curses, color):
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

    if color == 'cyan':
        return cyan
    elif color == 'blue':
        return blue
    elif color == 'yellow':
        return yellow
    elif color == 'green':
        return green
    elif color == 'magenta':
        return magenta
    elif color == 'red':
        return red
    elif color == 'white':
        return white
    else:
        return None










