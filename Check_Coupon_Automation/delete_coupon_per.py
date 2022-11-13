import pyodbc

def test_connect_to_db():
    server = '104.155.49.95'
    database = 'lupa'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)


    cursor = cnxn.cursor()
    print(cursor)
    a = cursor.execute("EXEC [lupa].[dbo].[delete_expired_coupons]")
    cursor.commit()
    print(a)
    cursor.close()


test_connect_to_db()