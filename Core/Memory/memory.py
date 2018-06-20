#
# Memory API Version 1.0
#
# This module plays as a mid-way communicator between the database and users
# To easily Read, Modify or Insert data.
# Written By: Ahmed Abdeldaim
#
# To use this module well:
# please read the following lines.
#
# Database Schema:
# ---------------------------------------------------------------------------------------------------------
# - Table Name(*)   | column1(type)   | column2(type)     | column3(type) ...                             -
# ---------------------------------------------------------------------------------------------------------
# - users(1)        | user_id(int)   | user_name(string)  | user_face(string)  | a_t(string)              -
# ---------------------------------------------------------------------------------------------------------
# - light(2)        | user_id(int)   | val(bool)         | u_val(bool)       | flag(bool)                 -
# ---------------------------------------------------------------------------------------------------------
# - air_con(2)      | user_id(int)   | o_val(int)        | in_val(int)       | u_val(int)   | flag(int)   -
#  ---------------------------------------------------------------------------------------------------------
# - tv(2)           | user_id(int)   | val(int)          | u_val(int)        | flag(bool)                 -
# ---------------------------------------------------------------------------------------------------------
# - light_DS(3)     | user_id(int)   | val(bool)         | day(int)          | date(date)   | time(time)  -
# ---------------------------------------------------------------------------------------------------------
# - air_con_DS(3)   | user_id(int)   | val(int)          | day(int)          | date(date)   | time(time)  -
# ---------------------------------------------------------------------------------------------------------
# - tv_DS(3)        | user_id(int)   | val(int)          | day(int)          | date(date)   | time(time)  -
# ---------------------------------------------------------------------------------------------------------
# - camera(4)       | user_id(int)   | src(string)                                                        -
# ---------------------------------------------------------------------------------------------------------
# - user_pref(5)    | user_id(int)                                                                        -
# ---------------------------------------------------------------------------------------------------------
# *:
#   1: contains users basic data.
#   2: contains the current state of the device.
#   3: contains the data-set of the device.
#   4: contains the latest images which passed to the camera.
#   5: contains the user preferences>
#
# To load this module in your script, use:
# >>> from Memory import memory
# or
# >>> import Memory.memory
# or
# >>> import Memory.memory as anyName
##############################################################################################
# To read data from this module:
# use function getValues(params)
# - this function takes 3 parameters:
#   1- table name. Ex: air_con_DS.
#   2- a list of columns you need. Ex: ['o_val', 'in_val', 'flag'].
#   3- the user-Id of the values you need.
#
# - and returning 2 values:
#   1- code. Ex: 101.
#   2- a dictionary with the values. Ex: {'o_val': 33, 'in_val': 24, 'flag': true}
#
#   code meaning:
#   101: this means the operation succeeded.
#   102: this means that the user-ID is not exist and the dictionary will be None.
#   103: this means failed to connect to the database and the dictionary will be None.
#   104: this means wrong table name.
#   105: this means wrong columns name.
#
# Ex:
#   code, data = getValues('air_con_DS', ['o_val', 'in_val', 'flag'], 13)
#   if code == 101:
#       outSideVal  = data['o_val']
#       inSideVal   = data['in_val']
#       flag        = data['flag']
#   elif code == 102:
#       logging.warning('the user_id is not exist.')
#   elif code == 103:
#       logging.warning('Failed to connect to the Database.')
#   else:
#       logging.warning('unrecognized code: ' + code)
#############################################################################################
#
# To insert data to a table:
# use function insertValues(params)
# - this function takes 2 parameters:
#   1- table name. Ex: air_con_DS.
#   2- a dictionary of columns and the values you want. Ex: {'o_val': 33, 'in_val': 22}.
#
# - and returning 1 value:
#   1- code. Ex: 201.
#
#   code meaning:
#   201: this means the operation succeeded.
#   203: this means failed to connect to the database.
#   204: this means wrong table name.
#   205: this means wrong columns name.
#
# Ex:
#   code = insertValues('air_con_DS', {'o_val': 33, 'in_val': 22})
#   if code == 202:
#       logging.warning('the user_id is not exist.')
#   elif code == 203:
#       logging.warning('Failed to connect to the Database.')
#   elif code != 201:
#       logging.warning('unrecognized code: ' + code)
#############################################################################################
#
# To Modify data in a table:
# use function modifyValues(params)
#
# WARNING: this function doesn't work for tables of type (2 or 3).
#
#  - this function takes 3 parameters:
#   1- table name. Ex: air_con.
#   2- a dictionary of columns and the values you want to modify. Ex: {'o_val': 33, 'in_val': 22}.
#   3- the user-Id of the values you need.
#
# - and returning 1 value:
#   1- code. Ex: 301.
#
#   code meaning:
#   301: this means the operation succeeded.
#   302: this means that the user-ID is not exist.
#   303: this means failed to connect to the database.
#   304: this means wrong table name.
#   305: this means wrong columns name.
#   306: this can't use this function for this type of table.
#
# Ex:
#   code = modifyValues(air_con, {'o_val': 33, 'in_val': 22}, 13)
#   if code == 302:
#       logging.warning('the user_id is not exist.')
#   elif code == 303:
#       logging.warning('Failed to connect to the Database.')
#   elif code != 301:
#       logging.warning('unrecognized code: ' + code)
#
#

import psycopg2
import logging

conn = None


def connect():
    try:
        global conn
        conn = psycopg2.connect(host="ec2-54-83-19-244.compute-1.amazonaws.com", database="d5uhoo3lgbrk23", user="divambbotwesnb", password="57647f395a1a22b82f4bc6e64dc5111ebd621bf305ffe902bd1737f534832b27")
        #conn = psycopg2.connect(host="localhost", database="wattary", user="wattary", password="seven23")
        # create a cursor
        cur = conn.cursor()
        return cur

    except (Exception, psycopg2.DatabaseError) as error:
        logging.warning('Connection Error: ' + str(error))
        return False


def getValues(tableName, columnNames, user_id):
    data = None
    cur = connect()
    if cur is not False:
        try:
            columnNamesStr = ', '.join(columnNames)
            # execute a statement
            cur.execute("SELECT " + columnNamesStr + " FROM " + tableName + " WHERE user_id=" + str(user_id))
            # fetch data
            row = cur.fetchone()

            if cur.rowcount > 0:
                while row is not None:
                    data = {}
                    for idx, name in enumerate(columnNames):
                        data[name] = row[idx]
                    row = cur.fetchone()
                cur.close()
                return 101, data
            else:
                return 102, data

        except (Exception, psycopg2.ProgrammingError) as error:
            if 'column' in str(error) and 'not exist' in str(error):
                return 105, data
            elif 'relation' in str(error) and 'not exist' in str(error):
                return 104, data
            else:
                return error, data
    else:
        return 103, data


def getValuesAll(tableName, columnNames):
    data = None
    cur = connect()
    if cur is not False:
        try:
            columnNamesStr = ', '.join(columnNames)
            # execute a statement
            cur.execute("SELECT " + columnNamesStr + " FROM " + tableName)
            # fetch data
            return 401, cur.fetchall()

        except (Exception, psycopg2.ProgrammingError) as error:
            if 'column' in str(error) and 'not exist' in str(error):
                return 405, data
            elif 'relation' in str(error) and 'not exist' in str(error):
                return 404, data
            else:
                return error, data
    else:
        return 403, data


def insertValues(tableName, data):
    cur = connect()
    if cur is not False:
        try:
            columnNames = list(data)
            values = []
            for name in columnNames:
                values.append((str(data[name])))
            columnNamesStr = ', '.join(columnNames)
            valuesStr = "', '".join(values)
            # execute a statement
            cur.execute("INSERT INTO " + tableName + "(" + columnNamesStr + ") VALUES('" + valuesStr + "') RETURNING user_id")
            # fetch data
            conn.commit()
            ID = cur.fetchone()[0]
            cur.close()
            return 201,ID
        except (Exception, psycopg2.Error) as error:
            if 'column' in str(error) and 'not exist' in str(error):
                return 205,''
            elif 'relation' in str(error) and 'not exist' in str(error):
                return 204,''
            else:
                return error,''
    else:
        return 203,''


def modifyValues(tableName, data, user_id):
    cur = connect()
    if cur is not False:
        try:
            columnNames = list(data)
            values = []
            for name in columnNames:
                values.append((str(data[name])))

            query = ""
            for idx, i in enumerate(columnNames):
                query += str(i) + "='" + str(values[idx]) + "'"
                if idx < len(columnNames) - 1:
                    query += ", "

            # execute a statement
            cur.execute("UPDATE " + tableName + " SET " + query + " WHERE user_id=" + str(user_id) )
            # fetch data
            if cur.rowcount > 0:
                conn.commit()
                cur.close()
                return 301
            else:
                return 302

        except (Exception, psycopg2.Error) as error:
            if 'column' in str(error) and 'not exist' in str(error):
                return 305
            elif 'relation' in str(error) and 'not exist' in str(error):
                return 304
            else:
                return error
    else:
        return 303


def selectValue(query):
    cur = connect()
    if cur is not False:
        try:
            cur.execute(query)
            # fetch data
            row = cur.fetchone()

            if cur.rowcount > 0:
                output = row[0]
                row = cur.fetchone()
                cur.close()
                return 501, output
            else:
                return 502, ''

        except (Exception, psycopg2.Error) as error:
            if 'column' in str(error) and 'not exist' in str(error):
                return 505, ''
            elif 'relation' in str(error) and 'not exist' in str(error):
                return 504, ''
            else:
                return error
    else:
        return 503, ''
