# The file is just for creating global options
# from modules.functions import pull_saved_data
from modules.custom_classes import Useroptions
import json


def pull_saved_data(path_file_name: str, index_name: str, class_name):
    with open(f'{path_file_name}') as f:
        loaded_json = json.load(f)
        index_dict = loaded_json[index_name]
        filled_class = class_name(**index_dict)
        return filled_class


user_options = Useroptions
user_options = pull_saved_data('data/options.json', 'User Options', Useroptions)
