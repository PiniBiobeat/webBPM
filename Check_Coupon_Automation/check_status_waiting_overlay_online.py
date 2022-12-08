import pyodbc
from datetime import datetime
import datetime
import requests


def test_connect_to_db():
    server = '104.155.49.95'
    database = 'lupa_online'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    list_orders_with_status_WO = list()
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()
    print(cursor)
    cursor.execute("select * from (select DATEADD(hour, -1 , GETDATE()) AS DATEADD  , order_id,master_id,in_status,update_date,order_comments FROM [lupa_online].[dbo].[orders_tbl] where in_status = 26) as t where DATEADD>t.update_date")
    row = cursor.fetchall()
    for i in row:
        print(str(i[1]))
        list_orders_with_status_WO.append(i[1])
    if len(list_orders_with_status_WO) != 0:
        token_url = 'https://monitor.lupa.co.il/api/api.aspx?method=write_error&source=AutomationMonitor&service_api=&error_code=15&active=true&token=&extra_params=' + str(
            {"orders_waiting_overlay": list_orders_with_status_WO})
        response = requests.get(token_url)
        print(response)

    cursor.close()
test_connect_to_db()

