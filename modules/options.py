# The file is just for creating global options

from modules.db_functions import db_return_class_object, db_create_connection
from modules.custom_classes import UserOptions


def pull_options():
    conn = db_create_connection('db/dnd.db')
    with conn:
        user_option = db_return_class_object(conn, 'useroptions', 'type', 'User Options', UserOptions)
    conn.close()
    return user_option


user_options = pull_options()
