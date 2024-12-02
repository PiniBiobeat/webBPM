import os
import json
import pyodbc
import requests
import psycopg2
from datetime import time
import configparser
from dotenv import load_dotenv
config = configparser.ConfigParser()
config.read('config.ini'), load_dotenv()



#MySQL database
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
    if query1.strip().lower().startswith('select'):
        result1 = cursor.fetchall()
    else:
        result1 = cursor.rowcount
    cursor.close()
    cnxn.commit()
    return result1



#Postgres database: PaymentV4 / calendar
def postgres14(postgres_execute,database="Tariff"):
    connection = psycopg2.connect(user="machineDBA",
                                  password="A#214Fdse!35dDC214XAzRDA12^79",
                                  host="35.187.190.6",
                                  port="5432",
                                  database=database)
    cursor = connection.cursor()
    query2 = postgres_execute
    cursor.execute(query2)
    if query2.strip().lower().startswith('select'):
        result2 = cursor.fetchall()
    else:
        result2 = cursor.rowcount
        print(f"{result2} rows affected")
    connection.commit()
    cursor.close()
    return result2



#Postgres database: Groupa / App V3
def groupa(groupa_execute):
    connection = psycopg2.connect(user="machineDBA",
                                  password="A#214Fdse!35dDC214XAzRDA12^79",
                                  host="35.233.19.13",
                                  port="5432",
                                  database="groupa")
    cursor = connection.cursor()
    query3 = groupa_execute
    cursor.execute(query3)
    if query3.strip().lower().startswith('select'):
        result3 = cursor.fetchall()
    else:
        result3 = cursor.rowcount
        print(f"{result3} rows affected")
    connection.commit()
    cursor.close()
    return result3



#postgress database: PaymentV4 prod and test
def postgres_env(postgres_execute):
    connection = psycopg2.connect(user="machineDBA",
                                  password="A#214Fdse!35dDC214XAzRDA12^79",
                                  host="35.187.190.6",
                                  port="5432",
                                  database=config['DATABASE']['postgress_' + os.getenv('env')])
    cursor = connection.cursor()
    query4 = postgres_execute
    cursor.execute(query4)
    if query4.strip().lower().startswith('select'):
        result4 = cursor.fetchall()
    else:
        result4 = cursor.rowcount
        print(f"{result4} rows affected")
    connection.commit()
    cursor.close()
    return result4

















































# without if to select/upate/delete
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

