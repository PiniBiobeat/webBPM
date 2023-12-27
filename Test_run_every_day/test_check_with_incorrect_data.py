import pyodbc
import requests
import json

def connect_to_db():
        global cursor
        server = '104.155.49.95'
        database = 'lupa'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        print(cursor)
def test_check_if_have_orders_in_table():
            connect_to_db()
            cursor.execute(
                '''  
             SELECT * FROM lupa.[dbo].orders_generic_errors_tbl  AS o
             RIGHT   JOIN (select  order_id,master_id,shipping_bill_id,insert_date,platform FROM [lupa].[dbo].[shippment_errors_tbl] ) AS e ON o.order_id = e.order_id where  ISNULL(payload,'') = '' 
           ''')
            row = cursor.fetchall()
            for i in row:
                if i[2] == None:
                    send_to_slack(i[6])
                    insert_to_table_error(i[6], i[7], i[10], i[10], i[8], i[9])
                else:
                    continue
            cursor.close()
def insert_to_table_error(order_id, master_id, platform, payload, code, insert_date):
            try:
                query = '''INSERT INTO lupa.[dbo].orders_generic_errors_tbl (order_id, master_id, platform, payload, code, insert_date)
                       VALUES (?, ?, ?, ?, ?, ?);'''
                cursor.execute(query, (order_id, master_id, platform, payload, code, insert_date))
                cursor.commit()
                print("Insert successful!")
            except Exception as e:
                print(f"Error: {e}")

def json_to_slack_message( value_list):
    """
            Converts a JSON object to a formatted Slack message.

            Args:
                json_data (dict): The JSON data to convert to a Slack message.

            Returns:
                str: The formatted Slack message string.
            """
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "orders with incorrect data Bar hafaza :wave:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": str(value_list)
            }
        }
    ]

    # Build the Slack message payload
    payload = {
        "blocks": blocks
    }

    # Convert the payload to JSON and return it
    return json.dumps(payload)

def send_to_slack( my_dict_lupa):
        payload = json_to_slack_message(my_dict_lupa)
        requests.post("https://hooks.slack.com/services/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",data=payload)
        print(payload)
test_check_if_have_orders_in_table()







