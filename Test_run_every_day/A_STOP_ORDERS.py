import pyodbc
from Test_run_every_day.B_STOP_ORDERS import *

def test_connect_to_db():
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
    cursor.execute(f"""
        
        
 

    update lupa_online.dbo.orders_tbl set in_status = '24' where master_id in ({master_ids}) AND in_status NOT IN (22, 23) AND in_status <> '24';
    update lupa_online.dbo.order_item_tbl set in_status = '24' where master_id in ({master_ids}) AND in_status NOT IN (22, 23) AND in_status <> '24';
    

    
    update lupa_square.dbo.orders_tbl set in_status = '24' where master_id in ({master_ids}) AND in_status NOT IN (22, 23, 10) AND in_status <> '24';
    update lupa_square.dbo.order_item_tbl set in_status = '24' where master_id in ({master_ids}) AND in_status NOT IN (22, 23, 10) AND in_status <> '24';


    update lupa.dbo.orders_tbl set in_status = 'Stopped' where order_customer_id in ({user_ids}) AND in_status NOT IN ('Delivered', 'Printed', 'Phone order') AND in_status <> 'Stopped'; 
    
    """)
    cnxn.commit()
