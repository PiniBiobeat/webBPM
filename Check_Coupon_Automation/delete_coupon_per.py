import pyodbc
from datetime import datetime
import datetime
def test_connect_to_db():
    server = '104.155.49.95'
    database = 'lupa'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()
    print(cursor)
    a = cursor.execute("EXEC [lupa].[dbo].[delete_expired_coupons]")
    cursor.commit()
    print(a)
    cursor.close()

    x = datetime.datetime.now()

    with open("C:\\Users\\tester\\Desktop\\all_logs_from_delete_coupon\\log_" + x.strftime("_%B") + x.strftime("_%d") + x.strftime("_%Y")+".txt", 'x') as f:
        f.write('create file for check if open file   ')
    f.close()
test_connect_to_db()