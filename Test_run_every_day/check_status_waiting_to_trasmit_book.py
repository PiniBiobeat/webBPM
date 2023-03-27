import pyodbc
from datetime import datetime
import datetime
import requests


def test_connect_to_db():
    server = '104.155.49.95'
    database = 'lupa'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()
    print(cursor)
    cursor.execute("select * from (select DATEADD(hour, -5 , GETDATE()) AS DATEADD  , barcode,orders,kind,insertdate,updatedate,status,closeddate FROM [lupa].[dbo].[shippingbill] where status = 'WaitingToTrasmit') as t where DATEADD>t.updatedate")
    row = cursor.fetchall()
    if row != []:
        token_url = 'https://monitor.lupa.co.il/api/api.aspx?method=write_error&source=AutomationMonitor&service_api=&error_code=42&active=true&token=&extra_params=' + str(
            {"ERROR_WAITING_TO_TRASMIT_ONLINE": len(row)})
        response = requests.get(token_url)
        print(response)


    cursor.close()
test_connect_to_db()