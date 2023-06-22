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
#'ben@lupa.co.il','pinim@lupa.co.il'

operators = ['ben@lupa.co.il','pinim@lupa.co.il','shlomi@lupa.co.il','ofer@lupa.co.il','ofir@lupa.co.il','igor_r@lupa.co.il']

class Test_me():
    my_dict_lupa = dict()

    def test_connect_to_db_in_lupa_DB(self):
        a = self.check_if_send_message()
        if a is True:
            self.connect_to_db()

    def connect_to_db(self):
        server = '104.155.49.95'
        database = 'lupa'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute(f"SELECT TOP (1000) * FROM [lupa].[dbo].[shippment_errors_tbl]")
        rows = cursor.fetchall()
        if rows != []:
            for row in rows:
                my_dict_lupa[row[7]] = row[0]
        print(my_dict_lupa)


        cursor.close()


        self.send_to_slack(my_dict_lupa)

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
                    "text": "orders with incorrect data :wave:"
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
    def check_if_send_message(self):

        # Connect to the database
        con = sqlite3.connect('my-test.db')

        # Define the SQL query
        sql = "SELECT * FROM orders_send WHERE time_insert_test < ?"

        # Calculate the datetime 24 hours ago
        time_threshold = datetime.now() - timedelta(hours=10)

        # Execute the SQL query with the provided parameter
        with con:
            data = con.execute(sql, (time_threshold,))
            for row in data:
                data_to_send.append(row)
                print(row)
            if len(data_to_send) > 0:
                return True

    def insert_to_DB_the_date(self):
        con = sl.connect('my-test.db')
        sql = 'INSERT INTO orders_send (test_name, time_insert_test) values( ?, ?)'
        # Get the current date and time
        current_datetime = datetime.now()

        # Format the current datetime as a string
        current_datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')
        data = [
            (my_dict_lupa, current_datetime_str)
        ]
        with con:
            con.executemany(sql, data)

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
                "from": "orders with incorrect data   <monitor@lupa.co.il>",
                "to": operators,
                "subject": "orders with incorrect data ! ",
                "html": self.json_to_html_table(my_dict_lupa)
            }
          )


    def send_to_slack(self, my_dict_lupa):
        payload = self.json_to_slack_message(my_dict_lupa)
        requests.post("https://hooks.slack.com/services/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",data=payload)
        print(payload)
        self.insert_to_DB_the_date()







