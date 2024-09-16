import pyodbc



def test_connect_to_db():
    server = '104.155.49.95'
    database = 'lupa'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()
    cursor.execute("""
          
 
    --------------Online--------------
    update top(1000) lupa_online.dbo.orders_tbl set in_status = '24' where master_id in (3275315) AND in_status NOT IN (22, 23) AND in_status <> '24';
    update top(1000) lupa_online.dbo.order_item_tbl set in_status = '24' where master_id in (3275315) AND in_status NOT IN (22, 23) AND in_status <> '24';
    
    --------------Tiles--------------
    
    update top(1000) lupa_square.dbo.orders_tbl set in_status = '24' where master_id in (3275315) AND in_status NOT IN (22, 23, 10) AND in_status <> '24';
    update top(1000) lupa_square.dbo.order_item_tbl set in_status = '24' where master_id in (3275315) AND in_status NOT IN (22, 23, 10) AND in_status <> '24';

    --------------Desktop--------------
    update top(1000) lupa.dbo.orders_tbl set in_status = 'Stopped' where order_customer_id in (271755) AND in_status NOT IN ('Delivered', 'Printed', 'Phone order') AND in_status <> 'Stopped'; 
    
    """)

