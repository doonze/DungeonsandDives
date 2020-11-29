# Main map making file
from pickle import loads

from modules.db_functions import db_select_values_where, db_update_value, db_delete_row
from modules.map_classes import *

# from modules.map_classes import MapYXZ, ZoneMapList, Wall
from modules.map_db_functions import db_pull_saved_map_to_dict, db_create_connection, db_select_value_distinct, \
    db_insert_point_data, db_select_values_distinct

try:
    import curses
    import curses.textpad
    import curses.panel
    import locale
    from modules.functions import save_dictionary, pull_saved_data, clear_screen, print_list, \
        list_to_num_dict, cb, ce, cy, print_class_data, edit_class_data
    import jsonpickle
    from modules.map_functions import input_list, set_colors, pull_saved_map, save_map, pull_maps

    locale.setlocale(locale.LC_ALL, '')


    def start_map_maker(screen, map_to_pull: MapYXZ):

        # set default curses colors
        cyan = set_colors(screen, curses, 'cyan')
        yellow = set_colors(screen, curses, 'yellow')
        green = set_colors(screen, curses, 'green')
        red = set_colors(screen, curses, 'red')
        # blue = set_colors(screen, curses, 'blue')
        # white = set_colors(screen, curses, 'white')
        # magenta = set_colors(screen, curses, 'magenta')

        # setup windows
        win_border = screen.subwin(22, 52, 0, 0)
        map_win = win_border.subwin(21, 51, 1, 1)
        list_win = screen.subwin(25, 5, 0, 54)
        output_bor = screen.subwin(12, 71, 22, 0)
        output_win = output_bor.derwin(11, 70, 0, 1)

        output_win.scrollok(True)

        # Get the possible special wall chars
        input_dict = input_list(list_win, yellow, green)
        key_list = []
        for key in input_dict:
            key_list.append(str(key))

        # Pull the map specified on start, or create it if it doesn't exist. The row id and char
        # it is added to the point_data tuple. Point_data is [0] index, row id is [1] index, and
        # char is [2] index
        conn = db_create_connection()
        map_dict = db_pull_saved_map_to_dict(conn, map_to_pull)

        # Setup some color for pulled map
        color_list_yellow = ['D', 'C']
        color_list_cyan = ['E', 'u', 'd']

        # Here we build the map in curses. We pull the point and char data from the
        # map_dict and plot it on the map window.
        if 'map_dec' not in map_dict:
            for key in map_dict:
                if map_dict[key][2] in color_list_yellow:
                    map_win.addstr(key[0], key[1], f'{map_dict[key][2]}', yellow)
                elif map_dict[key] in color_list_cyan:
                    map_win.addstr(key[0], key[1], f'{map_dict[key][2]}', cyan)
                else:
                    map_win.addstr(key[0], key[1], f'{map_dict[key][2]}', green)

        # After drawing map, put the cursor at 0, 0 so we don't have to find it
        map_win.move(0, 0)

        # Start drawing and  awaiting input
        while True:
            output_win.addstr(1, 0, f'Cursor is at: {str(map_win.getyx())}')
            output_win.refresh()
            win_border.box()
            win_border.refresh()
            output_bor.box()
            output_bor.refresh()
            map_win.refresh()
            list_win.refresh()
            screen.refresh()
            key = map_win.getkey()
            y, x = map_win.getyx()
            output_win.clear()
            output_win.addstr(2, 0, f'We got {key}')
            output_win.refresh()
            try:
                if str(key) == 'e':
                    curses.endwin()
                    break
                elif str(key) == 'KEY_DOWN':
                    y += 1
                    map_win.move(y, x)
                elif str(key) == 'KEY_UP':
                    y += -1
                    map_win.move(y, x)
                elif str(key) == 'KEY_RIGHT':
                    x += 1
                    map_win.move(y, x)
                elif str(key) == 'KEY_LEFT':
                    x += -1
                    map_win.move(y, x)
                elif str(key) == 'KEY_DC':
                    y, x = map_win.getyx()
                    map_win.addstr(y, x, ' ')
                    map_win.move(y, x)
                    cords_key = (y, x)
                    result = db_delete_row(conn, 'maps', 'id', map_dict[cords_key][1])
                    if result.rowcount > 0:
                        del map_dict[cords_key]
                elif key in key_list:
                    # Get current position of cursor in the map window
                    y, x = map_win.getyx()
                    # Turn those into a (y, x) tuple
                    cords = (y, x)
                    # Grab the correct char from input_dict (walls only)
                    char = input_dict[int(key)]
                    # Check if the cords already exist, so we know if to insert or update the DB, returns
                    # the row id if it exist, or sets it to 0 if we need to insert
                    if cords in map_dict:
                        row_id = map_dict[(y, x)][1]
                    else:
                        row_id = 0
                    # Declare the dataclass we're using for point_data and assign the correct char to it
                    wall = Wall()
                    wall._char = char
                    # write the char on the screen
                    map_win.addstr(y, x, f'{char}', green)
                    # move the cursor back to where we started (or it always moves right)
                    map_win.move(y, x)
                    # Now were going to either insert or updated the correct row in DB
                    conn = db_create_connection()
                    row_id = db_insert_point_data(conn, cords, map_to_pull, row_id, wall)
                    # Lastly we set the point_data and correct row id into the dictionary
                    map_dict[(y, x)] = (wall, row_id, char)
                elif str(key.lower()) == 'i':
                    curses.endwin()
                    y, x = map_win.getyx()
                    cords = (y, x)
                    map_dict = create_cell(map_dict, cords, 'wall')
                    screen.refresh()
                else:
                    y, x = map_win.getyx()
                    map_win.addstr(y, x, f'{key}', yellow)
                    map_win.move(y, x)
                    map_dict[(y, x)] = key
                    # save_map(map_dict, 'data/maps.json', map_to_pull)
            except Exception as e:
                output_win.addstr(3, 0, f'Exception caught!!: {e}', red)
                continue

            output_win.addstr(3, 0, f'Y = {y} X = {x}')
            # output_win.addstr(5, 0, f'Dict: {map_dict}')
            output_win.refresh()
            win_border.refresh()
            map_win.refresh()
            screen.refresh()
            continue


    def launch_map_maker():
        clear_screen()

        # Pulls all the distinct zones for user to choose from to work with
        conn = db_create_connection()
        all_zones = db_select_value_distinct(conn, 'maps', 'zone')

        # Next we'll let the user choose a zone to work with
        print('Here are all the zones in the map file: ')
        print()

        zone_dict = list_to_num_dict(all_zones)
        print_list(zone_dict)

        print()
        print(f'Please choose a zone to work with from above, ({cb}c{ce})ancel'
              f' or ({cb}n{ce})ew {cb}[?, c, n]{ce}: {cb}', end='')

        while True:
            zone_choice = input()
            print(ce, end='')
            if zone_choice in zone_dict.keys():
                zone = zone_dict[zone_choice]
                conn = db_create_connection()
                zoneyxz = db_select_values_distinct(conn, 'maps', 'zone_y, zone_x, zone_z', 'zone', zone)
                conn.close()
                yxz_list = []
                for row in zoneyxz:
                    yxz_list.append((row['zone_y'], row['zone_x'], row['zone_z']))

                clear_screen()
                print(f"Here are the maps in zone: {cb}{zone_dict[zone_choice]}{ce}")
                print()

                zone_maps_dict = list_to_num_dict(yxz_list)
                print_list(zone_maps_dict)

                print()
                print(f'Choose a map to load it, ({cb}d{ce})elete a map, ({cb}n{ce})ew, or '
                      f'({cb}c{ce})ancel {cb}[?, d, n, c]{ce}: {cb}', end='')

                while True:
                    map_choice = input()
                    print(ce, end='')
                    if map_choice in zone_maps_dict:
                        mapyxz = MapYXZ(zone, zone_maps_dict[map_choice][0],
                                        zone_maps_dict[map_choice][1],
                                        zone_maps_dict[map_choice][2])
                        return curses.wrapper(start_map_maker, mapyxz)
                    elif map_choice.lower == 'c':
                        return launch_map_maker()
                    elif map_choice.lower == 'd':
                        # delete the map
                        break
                    elif map_choice.lower == 'n':
                        # create new map in zone
                        break
                    else:
                        print(f'{cb}{map_choice}{ce} invalid for map choice. '
                              f'Please try again! {cb}[?, d, n, c]{ce}: {cb}', end='')

            elif zone_choice.lower == 'c':
                break
            elif zone_choice.lower == 'd':
                print()
                # delete a zone (wow, scary!!!)
            elif zone_choice.lower == 'n':
                print()
                # create a new zone
            else:
                print(f'{cb}{zone_choice}{ce} was invalid zone choice option. '
                      f'Please try again! {cb}[?, c, d, n]{ce}: {cb}', end='')


    def create_cell(pulled_map: dict, cords: tuple, cell_type: str):
        if cell_type == 'wall':
            clear_screen()
            print('Here is the cell data:')
            print()
            cell_data = pulled_map[cords]
            if type(cell_data) == str:
                edited_data = Wall(_char=cell_data)
                field_dict = print_class_data(edited_data)
                print()
                print(f'Choose a attribute to edit: []: ', end='')

                while True:
                    choice = input()
                    if choice in field_dict:
                        edited_data = edit_class_data(edited_data, choice, field_dict, Wall)
                        print(edited_data)
                    elif choice == '':
                        break



except Exception as ex:
    print(ex)
    input()
