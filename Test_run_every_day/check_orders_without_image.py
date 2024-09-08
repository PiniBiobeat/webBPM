import pyodbc
import requests
import json

def test_check_orders_without_image():
        server = '104.155.49.95'
        database = 'master'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute('''
                      SELECT MAX(insert_date) AS insert_date, fileName, in_status, order_id 
                    FROM [lupa_square].[dbo].[order_item_tbl] 
                    WHERE fileName = '.jpg'
                      AND insert_date > '2024-09-08 10:00:00.010'
                      AND in_status <> 24
                    GROUP BY fileName, in_status, order_id;
        ''')
        rows = cursor.fetchall()
        cursor.close()
        if len(rows) > 0:
            send_slack(len(rows))
        else:
            assert True and print("is goood")

def send_slack(order_count):

    slack_webhook_url = "https://hooks.slack.com/services/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"

    # Formatted message with dynamic order count
    message = f":warning: *Alert:* We have {order_count} orders Tiles without pictures. Please investigate the issue and resolve it as soon as possible."

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








