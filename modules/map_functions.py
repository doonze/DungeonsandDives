import curses
import json
import os
import jsonpickle
from modules.functions import exception_log
from modules.map_classes import MapYXZ


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


def save_map(save_dict: dict, path_file_name: str, index: MapYXZ, del_dict=False) -> None:
    """
     Pass function a dictionary (save_dict), a full path name (path_file_name), and the namedtuple

    you want the dictionary to be indexed by (index). You can also pass a empty dictionary, a path,
    an index to delete, and the del_dict=TRUE bool to delete a dictionary index.

     It will create the file if it doesn't exist or append to the file if it does,
    creating a dictionary of dictionaries indexed by (index). Files are saved in json format.

    Valid paths:
     data/races.json\n
     data/classes.json\n
     data/options.json\n
     saves/char.json\n

     :param save_dict: Dictionary to save to file (not used for deletes)
     :type save_dict: typing._SpecialForm
     :param path_file_name: path/filename.extension format
     :type path_file_name: str
     :param index: Index to save it into the file under (or to delete)
     :type index: NamedTuple
     :param del_dict: Bool on if the is for deleting a dictionary
     :type del_dict: bool
     """
    try:
        index_dict = {}  # Just to avoid assignment errors in code

        if not del_dict:  # Runs if del_dict = False
            # Because we're using namedtuple as a dict key, and using tuples as keys for
            # coordinates in maps, we do some special encoding. Mainly we pickle the index
            # key (a namedtuple) and the passed dictionary separately. Then make a new dictionary
            # indexed by the namedtuple key. JSON doesn't allow tuple dict keys so we have to encode it

            index_dict = {jsonpickle.encode(index, keys=True): jsonpickle.encode(save_dict, keys=True)}

        if os.path.exists(f'{path_file_name}'):
            with open(f'{path_file_name}') as f:
                loaded_json = json.load(f)
            if del_dict:  # If it was called to delete a dictionary just need the index to delete
                loaded_json.pop(index)  # This pops (deletes) the passed index name from dictionary
            else:
                loaded_json.update(index_dict)  # Adds the indexed dictionary to the existing dictionary of dictionaries
            json_save = json.dumps(loaded_json, indent=4)  # Then converts it to a json
        else:  # If file didn't already exist we create it with one single dict inside
            json_save = json.dumps(index_dict, indent=4)

        f = open(f"{path_file_name}", 'w')
        f.write(json_save)
        f.close()
    except Exception as ex:
        exception_log(f'Something went wrong in the save_map function - ', ex)


def pull_saved_map(path_file_name: str, map_index: MapYXZ) -> any:
    """
    Pulls data from provided path for the provided index, returns a class object filled with the data from file

    :param path_file_name: path/filename.extension format
    :type path_file_name: str
    :param map_index: Index to pull info from in file
    :type map_index: NamedTuple
    :return: Returns a dataclass object
    :rtype: any
    """
    map_dict = {}
    try:
        with open(f'{path_file_name}') as f:
            loaded_json = json.load(f)
            for key in loaded_json:
                map_key = jsonpickle.decode(key)
                map_value = jsonpickle.decode(loaded_json[key], keys=True)
                map_dict[map_key] = map_value

            index_dict = map_dict[map_index]
            return index_dict
    except Exception as ex:
        print(f'Something went wrong pulling saved data: {ex}')
        return None


def pull_maps(path_file_name: str) -> dict:
    """
    Pulls ALL data from provided path for the provided index, returns a class object filled with the data from file

    :param path_file_name: path/filename.extension format
    :type path_file_name: str
    :return: Returns a dictionary of file
    :rtype: dict
    """
    maps_dict = {}
    try:
        with open(f'{path_file_name}') as f:
            loaded_json = json.load(f)
            for key in loaded_json:
                map_key = jsonpickle.decode(key)
                map_value = jsonpickle.decode(loaded_json[key], keys=True)
                maps_dict[map_key] = map_value

            return maps_dict
    except Exception as ex:
        print(f'Something went wrong pulling saved data: {ex}')

