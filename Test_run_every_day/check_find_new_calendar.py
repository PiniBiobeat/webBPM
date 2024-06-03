import pyodbc
import requests
import json


my_dict_lupa = dict()

hours = 8

def check_find_new_calendar():
        server = '104.155.49.95'
        database = 'lupa_online'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute('''         SELECT *
          FROM [lupa_online].[dbo].order_item_tbl
         WHERE tree_version = 'v3.0.0' and in_status = 21 and order_id <> 7139119
         AND insert_date >= DATEADD(hour, -24, GETDATE()) 
''')
        rows = cursor.fetchall()
        if rows != []:

            a = len(rows)
            print(my_dict_lupa)
            send_to_slack(a)
        cursor.close()

def json_to_slack_message(json_data):

        # Build the Slack message blocks
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": " הזמנה של לוח שנה חדשה לולולולולול !!!!!!!! :wave:"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": str(json_data)
                }
            }
        ]

        # Build the Slack message payload
        payload = {
            "blocks": blocks
        }

        # Convert the payload to JSON and return it
        return json.dumps(payload)

def json_to_html_table(json_data):
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

def send_to_slack(my_dict_lupa):
        payload = json_to_slack_message(my_dict_lupa)
        requests.post("https://hooks.slack.com/services/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",data=payload)
        print(payload)

check_find_new_calendar()