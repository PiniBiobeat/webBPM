import json

import pyodbc
from datetime import datetime
import datetime

import requests


def test_connect_to_db():
    server = '104.155.49.95'
    database = 'lupa_square'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    list_orders_with_status_WO = list()
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()
    print(cursor)
    cursor.execute("select * from (select DATEADD(hour, -1 , GETDATE()) AS DATEADD  , order_id,master_id,in_status,charged_date,order_comments FROM [lupa_square].[dbo].[orders_tbl] where in_status = 26) as t where DATEADD>t.charged_date")
    row = cursor.fetchall()
    for i in row:
        print(str(i[1]))
        list_orders_with_status_WO.append(i[1])
    if len(list_orders_with_status_WO) != 0:

        send_to_slack(list_orders_with_status_WO)
    cursor.close()
def json_to_slack_message(list):
            """
            Converts a JSON object to a formatted Slack message.

            Args:
                json_data (dict): The JSON data to convert to a Slack message.

            Returns:
                str: The formatted Slack message string.
            """
            # Create a bulleted list of the key values

            value_list = "\n".join([f"•{key}" for key in list])

            # Build the Slack message blocks
            blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "orders with status waiting :wave:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": value_list
                    }
                }
            ]

            # Build the Slack message payload
            payload = {
                "blocks": blocks
            }

            # Convert the payload to JSON and return it
            return json.dumps(payload)
def send_to_slack(my_dict_lupa):
            payload = json_to_slack_message(my_dict_lupa)
            requests.post("https://hooks.slack.com/services/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",
                          data=payload)



test_connect_to_db()