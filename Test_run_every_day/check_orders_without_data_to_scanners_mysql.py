import time

import mysql.connector
import requests
import json
import sqlite3 as sl

my_dict_lupa = dict()

#'ben@lupa.co.il','pinim@lupa.co.il'

operators = ['ben@lupa.co.il','pinim@lupa.co.il','shlomi@lupa.co.il','ofer@lupa.co.il','ofir@lupa.co.il','igor_r@lupa.co.il']
hours = 8
class Test_me():
    my_dict_lupa = dict()

    def test_connect_to_mysql(self):
        cnx = mysql.connector.connect(
            user='printahead',
            passwd='kklixd883',
            host='10.116.97.3',
            db='printahead')

        cursor = cnx.cursor()
        print(cursor)
        counter = 0
        rows = []

        while counter < 3:
            cursor.execute(
                "SELECT * FROM EASYPHOTOBOOK WHERE JOBID IS NULL AND CAST(ORDER_CHANGED AS DATE) > '2023-06-10' ORDER BY TRANSFERTIME DESC;")
            new_rows = cursor.fetchall()
            if len(new_rows) != 0:
                if rows == new_rows:
                    counter += 1
                else:
                    counter = 0
                    rows = new_rows
                    time.sleep(5)
            else:
                break

        self.check_again(rows)
        cursor.close()
        cnx.close()

    def check_again(self, rows):
        if rows:
            for row in rows:
                my_dict_lupa[row[0]] = row[1]
            if len(my_dict_lupa) > 0:
                self.send_to_email(my_dict_lupa)
                self.send_to_slack(my_dict_lupa)



    import json

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
                    "text": "הזמנות ללא check_orders_without_data_to_scanners_mysql :wave:"
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

    def send_to_email(self,my_dict_lupa):
      requests.post(
            "https://api.mailgun.net/v3/lupa.co.il/messages",
            auth=("api", "key-d2ed6868aa56bfda882f84b173693a2a"),
            data={
                "from": "check_orders_without_data_to_scanners_mysql   <monitor@lupa.co.il>",
                "to": operators,
                "subject": "check_orders_without_data_to_scanners_mysql ! ",
                "html": self.json_to_html_table(my_dict_lupa)
            }
          )

    def send_to_slack(self, my_dict_lupa):
        payload = self.json_to_slack_message(my_dict_lupa)
        requests.post("https://hooks.slack.com/services/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",data=payload)
        print(payload)








