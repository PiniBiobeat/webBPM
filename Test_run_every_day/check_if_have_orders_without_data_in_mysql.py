import pyodbc
import requests
import json

def check_if_have_orders_without_data_in_mysql():
        server = '104.155.49.95'
        database = 'master'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute('''
                      SELECT o.[order_id]
                              ,o.[a_num]
                              ,o.[order_price]
                              ,o.[deliv_company]
                              ,o.[deliv_city]
                              ,o.[deliv_country]
                              ,o.charged_date
                              ,o.in_status
                                FROM [lupa].[dbo].[orders_tbl] AS o
                                LEFT JOIN [lupa].[dbo].[orders_extra_data_tbl] AS e
                                ON o.[order_id] = e.[order_id]
                                WHERE e.[order_id] IS NULL and o.in_status <> 'Delivered' and  o.in_status <> 'Canceled' and  o.in_status <> 'Stopped' and o.a_num > 1911781
                                order by o.a_num desc
        ''')
        rows = cursor.fetchall()
        cursor.close()
        if len(rows) > 0:
            send_slack(len(rows))
        else:
             print("is goood")

def send_slack(order_count):

    slack_webhook_url = "https://hooks.slack.com/services/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"

    # Formatted message with dynamic order count
    message = f":warning: *Alert:* We have {order_count} orders Desktop without line in order extra data. Please investigate the issue and resolve it as soon as possible."

    payload = {
        "text": message,  # Use the formatted message
        "username": "Order Monitor Bot",  # Bot name
        "channel": "#מוניטור-הזמנות",  # Slack channel
        "icon_emoji": ":camera:"  # Optional: Bot icon emoji
    }

    response = requests.post(slack_webhook_url, json=payload)

    # Handle Slack response
    if response.status_code != 200:
        print(f"Failed to send message to Slack. Status Code: {response.status_code}, Response: {response.text}")
    else:
        print("Message sent successfully to Slack!")

check_if_have_orders_without_data_in_mysql()








