#check_orders_without_order_item



import pyodbc
import sqlite3
from datetime import datetime, timedelta
import datetime
import requests
import json
import sqlite3 as sl
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
my_dict_lupa = dict()
data_to_send = []

class Test_me():
    my_dict_lupa = dict()

    def test_connect_to_db(self):
        server = '104.155.49.95'
        database = 'master'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute('''
            SELECT top(1) o.order_id
			FROM [lupa_online].[dbo].[orders_tbl] AS o
			LEFT JOIN [lupa_online].[dbo].[order_item_tbl] AS oi
			ON o.order_id = oi.order_id
			WHERE o.in_status = 21 and  oi.order_id IS NULL 
        ''')
        rows = cursor.fetchall()
        cursor.close()
        if rows != []:
            for row in rows:
                my_dict_lupa[row[0]] = row
            self.send_to_slack(my_dict_lupa)
        else:
            assert True



    def json_to_slack_message(self, json_data):
        """
        Converts a JSON object to a formatted Slack message.

        Args:
            json_data (dict): The JSON data to convert to a Slack message.

        Returns:
            str: The formatted Slack message string.
        """
        # Create a bulleted list of the key values
        keys_list = list(json_data.keys())
        value_list = "\n".join([f"• <https://admin.lupa.co.il/admin_book/Order_Details.aspx?id={key}|{key}>" if str(key).startswith('18') else f"• <https://admin.lupa.co.il/admin_online/Order_Details.aspx?id={key}|{key}>" if str(key).startswith('76') else f"• <https://admin.lupa.co.il/admin_online/Order_Details.aspx?id={key}|{key}>" for key in keys_list])

        # Build the Slack message blocks
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "check orders without order item  :wave:"
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


    def json_to_html_table(self,json_data):
        """
        Converts a JSON object to an HTML table.

        Args:
            json_data (str or dict): The JSON data to convert to an HTML table.

        Returns:
            str: The HTML table string.
        """
        # Load JSON data if it's a string
        if isinstance(json_data, str):
            json_data = json.loads(json_data)

        # Build the table rows
        rows = []
        for key, value in json_data.items():
            rows.append(f"<tr><td>{key}</td><td>{value}</td></tr>")

        # Build the HTML table
        table = f"<table><tr><th>Key</th><th>Value</th></tr>{''.join(rows)}</table>"

        # Build the HTML template
        template = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>JSON to HTML Table</title>
                </head>
                <body>
                    {table}
                </body>
            </html>
        """

        return template

    def send_to_slack(self, my_dict_lupa):
        payload = self.json_to_slack_message(my_dict_lupa)
        requests.post("https://hooks.slack.com/services/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",data=payload)
        print(payload)









