import pyodbc
from datetime import datetime
import datetime
import requests
import random
import string
import logging as logger

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

def sql_get_status_newsletter(Email):

        server = '104.155.49.95'
        database = 'lupa'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute("select * FROM [lupa].[dbo].[newslleter] where email =?",Email)
        row = cursor.fetchall()
        for i in row:
            return i[5]
        cursor.close()


def sql_get_status_master_id(Email):
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


#[lupa].[dbo].[newslleter].newsletter_ststus