import os
from datetime import datetime
from io import BytesIO
import pyodbc
import sqlite3
import requests
from openpyxl.workbook import Workbook


def bring_users_to_cancel():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testDb')
    sqliteConnection = sqlite3.connect(db_path)
    cursor = sqliteConnection.cursor()
    query = 'select master_id , bower_id from users_for_cancel'
    cursor.execute(query)
    result = cursor.fetchall()
    return result
def join_column_values(result, column_index):
    return ','.join(str(row[column_index]) for row in result)

def test_connect_to_db_2():
    result = bring_users_to_cancel()
    master_ids = join_column_values(result, 0)
    user_ids = join_column_values(result, 1)

    server = '104.155.49.95'
    database = 'lupa'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()
    query1 = f"""
    SELECT [master_id]
          ,[order_id]
          ,[invoice_number]
          ,[total_order_price]
          ,[order_date]
    FROM [lupa_online].[dbo].[orders_tbl] where master_id in ({master_ids})
    AND no_charge_reason <> 'TEST'
    AND invoice_number <> ''
    AND CONVERT(DATE, order_date) = CONVERT(DATE, GETDATE())
    order by order_date desc
    """

    query2 = f"""
    SELECT [master_id]
          ,[order_id]
          ,[invoice_number]
          ,[total_order_price]
          ,[order_date]
    FROM [lupa_square].[dbo].[orders_tbl] where master_id in ({master_ids})
    AND no_charge_reason <> 'TEST'
    AND invoice_number <> ''
    AND CONVERT(DATE, order_date) = CONVERT(DATE, GETDATE())
    order by order_date desc
    """

    query3 = f"""
    SELECT o.[order_customer_id]
          ,o.[a_num]
          ,o.[receipt]
          ,o.[total_order_price]
          ,e.[order_date]
    FROM [lupa].[dbo].[orders_tbl] o
    JOIN [lupa].[dbo].[orders_extra_data_tbl] e ON o.order_id = e.order_id
    WHERE o.order_customer_id in ({user_ids})
    AND CONVERT(DATE, e.order_date) = CONVERT(DATE, GETDATE())
    AND o.receipt <> ''
    ORDER BY e.order_date DESC
    """

    #online
    cursor.execute(query1)
    result1 = cursor.fetchall()
    #tiles
    cursor.execute(query2)
    result2 = cursor.fetchall()
    #bower
    cursor.execute(query3)
    result3 = cursor.fetchall()

    # יצירת קובץ אקסל
    workbook = Workbook()
    sheet = workbook.active
    # כותרות
    columns = [column[0] for column in cursor.description]
    sheet.append(columns)
    # הוספת תוצאות שאילתות לאקסל
    rows = result1 + result2 + result3
    for row in rows:
        sheet.append(list(row))
    # שמירת הקובץ בזיכרון
    output = BytesIO()
    workbook.save(output)
    output.seek(0)
    second_row = list(sheet.iter_rows(min_row=2, max_row=2, values_only=True))[0]
    if all(cell is None or cell == '' for cell in second_row):
        print("No orders today. Email will not be sent.")
    else:
        send_to_email(output)
        print("Email sent.")

def send_to_email(excel_file):
    today = datetime.now().strftime("%d-%m-%Y")
    return requests.post(
        "https://api.mailgun.net/v3/lupa.co.il/messages",
        auth=("api", "key-d2ed6868aa56bfda882f84b173693a2a"),
        files={"attachment": (
        f"Orders {today}.xlsx", excel_file, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")},
        data={
            "from": "lupa automation<monitor@lupa.co.il>",
            "to": "shiranc@lupa.co.il,ofirtnc@gmail.com",
            "subject": "ביטול הזמנות טסטים פיתוח",
            "text": " :) תודה והמשך יום נפלא"
        }
    )
