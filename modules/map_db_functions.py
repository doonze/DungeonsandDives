# module for map related database functions
import sqlite3
from pickle import dumps, loads
from typing import List

from modules.map_classes import MapYXZ


def db_create_connection(db_file: str = 'db/map.db') -> sqlite3.Connection:
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
    except sqlite3.Error as e:
        print(e)

    return conn


def db_pull_saved_map_to_dict(conn, mapyxz: MapYXZ):
    sql = f'SELECT * FROM MAPS WHERE zone = ? AND zone_y = ? AND zone_x = ? AND zone_z = ?'
    params = (mapyxz.zone, mapyxz.y, mapyxz.x, mapyxz.z)
    with conn:
        cur = conn.cursor()
        cur.execute(sql, params)
        rows = cur.fetchall()
    cur.close()
    map_dict = {}
    if len(rows) > 0:
        for row in rows:
            map_cords = (row['y'], row['x'])
            map_dict[map_cords] = (loads(row['point_data']), row['id'], row['char'])

        return map_dict
    else:
        map_dict['map_dec'] = mapyxz

        return map_dict


def db_select_value_distinct(conn, table, value) -> list:
    """
    Select multiple rows from a single value from a table where you only want one
    return for each distinct value

    SELECT DISTINCT {value} FROM {table}

    EX: SELECT zone FROM maps

    Returns a sqlite3 addressable list of rows ex: row['name']

    :param conn: DB connection
    :type conn: sqlite3.Connection
    :param table: table to pull from (single value)
    :type table: str
    :param value: Column value to pull
    :type value: str
    :return: list
    :rtype: list
    """

    sql = f"SELECT DISTINCT {value} FROM {table}"
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
    cur.close()

    list_return = []
    for row in rows:
        list_return.append(row[value])

    return list_return


def db_select_values_distinct(conn, table, value, where, where_what) -> list:
    """
    Select multiple rows from a single value from a table where you only want one
    return for each distinct value

    SELECT DISTINCT {value} FROM {table}

    EX: SELECT zone FROM maps

    Returns a sqlite3 addressable list of rows ex: row['name']

    :param conn: DB connection
    :type conn: sqlite3.Connection
    :param table: table to pull from
    :type table: str
    :param value: Column value(s) to pull
    :type value: str
    :return: list
    :rtype: list
    """

    sql = f"SELECT DISTINCT {value} FROM {table} WHERE {where} = ?"
    params = [where_what]
    with conn:
        cur = conn.cursor()
        cur.execute(sql, params)
        rows = cur.fetchall()
    cur.close()

    return rows


def db_insert_point_data(conn, cords, mapyxz: MapYXZ, row_id,  dataclass):
    if not row_id == 0:
        sql = f'UPDATE maps SET point_data = ?, char = ? WHERE id = ?'
        params = (dumps(dataclass), dataclass.char, row_id)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, params)
        cur.close()
        return row_id
    else:
        sql = f'INSERT INTO maps (zone, zone_y, zone_x, zone_z, y, x, char, point_data) ' \
              f'VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        params = (mapyxz.zone, mapyxz.y, mapyxz.x, mapyxz.z, cords[0], cords[1], dataclass.char, dumps(dataclass))
        with conn:
            cur = conn.cursor()
            cur.execute(sql, params)
        cur.close()

        return cur.lastrowid
