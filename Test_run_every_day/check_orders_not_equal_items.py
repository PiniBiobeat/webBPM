import pyodbc
import requests
import json


my_dict_lupa = dict()

hours = 8

def check_orders_not_equal_items():
        server = '104.155.49.95'
        database = 'lupa_square'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute('''      select
                                a.order_id
                                from [lupa_square].[dbo].[orders_tbl] a
                                join (select order_id ,SUM(quantity) as quantity 	from [lupa_square].[dbo].[order_item_tbl] group by order_id ) b
                                on  b.order_id = a.order_id
                                where b.quantity <> a.total_items_quantity
                                and a.in_status <> 23
                                and a.in_status <> 13
                                and a.in_status <> 24
                                and a.in_status <> 21
								and a.in_status <> 22
                                order by a.insert_date desc''')
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
                    "text": "הזמנת טיילס עם כמות פריטים לא נכונה  :wave:"
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

check_orders_not_equal_items()








