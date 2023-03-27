import pyodbc
from datetime import datetime
import datetime
import requests


def test_connect_to_db():
    server = '104.155.49.95'
    database = 'lupa_square'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    print(cursor)
    cursor.execute("SELECT TOP (1000) [order_id] FROM [lupa_square].[dbo].[orders_tbl] where in_status  = 14")
    row = cursor.fetchall()
    if len(row) > 9 :
        token_url = 'https://monitor.lupa.co.il/api/api.aspx?method=write_error&source=AutomationMonitor&service_api=&error_code=43&active=true&token=&extra_params=' + str({f"There are more than {len(row)} orders in Charge failed status in tiles->": len(row)})
        requests.get(token_url)

    cursor.close()
test_connect_to_db()