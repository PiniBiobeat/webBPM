import os
import time
#import mysql.connector  # if using mysql-connector-python
import psycopg2
import pyodbc
from datetime import datetime
import datetime
import requests
import random
import string
import logging as logger
from infra.config.config_provider import configuration

def generate_random_email_and_password(domain=None,email_prefix=None):

    if not domain:
        domain = 'lupa.co.il'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase,k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain


    logger.info(f"Generated random email: {email}")

    rand_paawd_length = 15
    rand_password = ''.join(random.choices(string.ascii_letters,k=rand_paawd_length ))

    random_info = {"email":email,"password":rand_password}

    return random_info

def sql_updade_status_in_order_V3():

        server = '104.155.49.95'
        database = 'lupa'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        ctx = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password
        )
        cursor = ctx.cursor()
        cursor.execute('''
                       UPDATE TOP (3) [lupa_online].[dbo].[order_item_tbl]
                       SET in_status = 1
                       WHERE master_id = 3657774 AND in_status = 30
                       ''')
        ctx.commit()


def sql_get_status_newsletter(Email):

        server = '104.155.49.95'
        database = 'lupa'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        ctx = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password
        )

        cursor = ctx.cursor()
        print(cursor)
        cursor.execute("select * FROM [lupa].[dbo].[newslleter] where email =?",Email)
        row = cursor.fetchall()
        for i in row:
            return i[5]
        cursor.close()


def sql_get_status_master_id(Email):
    time.sleep(5)
    server = '104.155.49.95'
    database = 'lupa'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    print(cursor)
    cursor.execute("SELECT  *  FROM [lupa].[dbo].[user_master] where user_email =?", Email)
    row = cursor.fetchall()

    for i in row:
        return i[15]
    cursor.close()

def sql_get_calendar():
    time.sleep(5)
    connection = psycopg2.connect(user="machineDBA",
                                  password="A#214Fdse!35dDC214XAzRDA12^79",
                                  host="10.116.96.32",
                                  port="5432",
                                  database=configuration['data_from_'+os.getenv('env')])
    cursor = connection.cursor()
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute(
        '''
    SELECT format, theme,path FROM public.calendars_tbl
    WHERE master_id = 3189204 
    ORDER BY id DESC LIMIT 1
    ''', )
    record = cursor.fetchall()
    cursor.close()
    return record

def sql_get_path_calendar(token_after_calendar):
    time.sleep(5)
    connection = psycopg2.connect(user="machineDBA",
                                  password="A#214Fdse!35dDC214XAzRDA12^79",
                                  host="10.116.96.32",
                                  port="5432",
                                  database=configuration['data_from_'+os.getenv('env')])
    cursor = connection.cursor()
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute(
        '''
    SELECT path FROM public.calendars_tbl
    WHERE token = %s
    ORDER BY id DESC LIMIT 100
    ''', (token_after_calendar,))
    record = cursor.fetchall()
    cursor.close()
    return record

def sql_get_event_date(master_id):
    time.sleep(5)
    connection = psycopg2.connect(user="machineDBA",
                                  password="A#214Fdse!35dDC214XAzRDA12^79",
                                  host="10.116.96.32",
                                  port="5432",
                                  database=configuration['data_from_'+os.getenv('env')])
    cursor = connection.cursor()
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute(
        '''
    SELECT * FROM public.personal_dates_tbl
    WHERE master_id = %s
    ORDER BY date_id DESC LIMIT 100
    ''', (master_id,))
    record = cursor.fetchall()
    cursor.close()
    return record

def sql_delete_personal_date(master_id):
    time.sleep(5)
    connection = psycopg2.connect(user="machineDBA",
                                  password="A#214Fdse!35dDC214XAzRDA12^79",
                                  host="10.116.96.32",
                                  port="5432",
                                  database=configuration['data_from_'+os.getenv('env')])
    cursor = connection.cursor()
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute(
        '''
    DELETE FROM public.personal_dates_tbl
	WHERE master_id = %s
    ''', (master_id,))
    connection.commit()
    cursor.close()

def sql_get_total_order_price(order):
    time.sleep(5)
    server = '104.155.49.95'
    database = 'lupa_online'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    print(cursor)

    query = """
    SELECT total_order_price 
    FROM [lupa_online].[dbo].[orders_tbl] 
    WHERE order_id = ?

    UNION ALL

    SELECT total_order_price 
    FROM [lupa_square].[dbo].[orders_tbl] 
    WHERE order_id = ?
    """
    cursor.execute(query, order, order)
    rows = cursor.fetchall()
    cursor.close()
    return rows




def get_order_status(cursor, order_id):
    query = """
    SELECT in_status
    FROM [lupa_online].[dbo].[orders_tbl]
    WHERE order_id = ?

    UNION ALL

    SELECT in_status
    FROM [lupa_square].[dbo].[orders_tbl]
    WHERE order_id = ?
    """
    cursor.execute(query, order_id, order_id)
    row = cursor.fetchone()
    return row[0] if row else None

def monitor_order_status(order_id, interval=5):
    time.sleep(5)
    server = '104.155.49.95'
    database = 'lupa_online'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    while True:
        last_status = get_order_status(cursor, order_id)
        if 21 == last_status:
            break
        time.sleep(interval)

def sql_get_transact_online_tbl(order_id):
    time.sleep(5)
    server = '104.155.49.95'
    database = 'matrix_db'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    query = """
     SELECT TOP (10)
      [order_id]
      ,[price]
      ,[catalog_num]
      ,[error_description]
      ,[invoice]
        FROM [matrix_db].[dbo].[transact_online_tbl] where  catalog_num = 'BK-Mr-Dlv-000025'  and order_id = ?
     """
    cursor.execute(query, order_id)
    row = cursor.fetchone()
    return str(row[1]) if row else None

def update_order_status_online(order_id):
    time.sleep(5)

    server = '104.155.49.95'
    database = 'lupa_online'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    ctx = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password
    )
    cursor = ctx.cursor()

    # Use a CTE to update the top 3 records
    cursor.execute('''
                   WITH CTE AS (
                       SELECT TOP (3) *
                       FROM [lupa_online].[dbo].[orders_tbl]
                       WHERE master_id = 3657774 AND order_id = ?
                   )
                   UPDATE CTE
                   SET in_status = 21
                   ''', order_id)

    # Commit the changes
    ctx.commit()

    # Close the cursor and connection
    cursor.close()
    ctx.close()


def update_order_status_tiles(order_id):
        time.sleep(5)

        server = '104.155.49.95'
        database = 'lupa_square'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        ctx = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password
        )
        cursor = ctx.cursor()

        # Use a CTE to update the top 3 records
        cursor.execute('''
                       WITH CTE AS (
                           SELECT TOP (3) *
                           FROM [lupa_square].[dbo].[orders_tbl]
                           WHERE master_id = 3657774 AND order_id = ?
                       )
                       UPDATE CTE
                       SET in_status = 21
                       ''', order_id)

        # Commit the changes
        ctx.commit()

        # Close the cursor and connection
        cursor.close()
        ctx.close()
