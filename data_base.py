import json
import pyodbc
import requests


# def mysql(mysql_execute):
#     server = '104.155.49.95'
#     database = 'lupa'
#     username = 'MachineDBA'
#     password = 'Kk28!32Zx'
#     cnxn = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
#
#     cursor = cnxn.cursor()
#     query1 = mysql_execute
#     cursor.execute(query1)
#     result1 = cursor.fetchall()
#     cursor.close()
#     cnxn.commit()
#     return result1


def mysql(mysql_execute):
    server = '104.155.49.95'
    database = 'lupa'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server +
        ';DATABASE=' + database +
        ';Encrypt=No;UID=' + username +
        ';PWD=' + password)

    cursor = cnxn.cursor()
    query1 = mysql_execute
    cursor.execute(query1)
    # בודקים אם השאילתה היא SELECT
    if query1.strip().lower().startswith('select'):
        result1 = cursor.fetchall()  # מחזירים תוצאות רק עבור SELECT
    else:
        result1 = None  # עבור UPDATE/DELETE לא מחזירים תוצאה

    cursor.close()
    cnxn.commit()
    return result1


