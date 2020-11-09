# The file is just for creating global options
# from modules.functions import pull_saved_data
import jsonpickle
from modules.custom_classes import UserOptions
import json


def pull_saved_data(path_file_name: str, index_name: str) -> UserOptions:
    """
    One off function just to pull game options.

    :param path_file_name: Full path to file name
    :type path_file_name: str
    :param index_name: Indexed name to pull
    :type index_name: str
    :return: UserOptions
    :rtype: any
    """
    with open(f'{path_file_name}') as f:
        loaded_json = json.load(f)
        index_dict = loaded_json[index_name]
        filled_class = jsonpickle.decode(index_dict)
        return filled_class


user_options: UserOptions
user_options = pull_saved_data('data/options.json', 'User Options')

