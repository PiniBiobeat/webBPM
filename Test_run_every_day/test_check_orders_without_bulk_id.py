import os
import pyodbc
from datetime import datetime, timedelta
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from data_base import mysql

operators = ['pinim@lupa.co.il']
hours = 8

class TestMe:

    my_dict_lupa = {}

    def connect_to_db(self, server, database, username, password):
        try:
            cnxn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
            return cnxn
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def fetch_data(self, cnxn, query):
        try:
            with cnxn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return []

    def test_connect_to_db(self, database, query, product_type):
        server = '104.155.49.95'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'

        cnxn = self.connect_to_db(server, database, username, password)
        if cnxn:
            rows = self.fetch_data(cnxn, query)
            for row in rows:
                self.my_dict_lupa[row[0]] = {
                    "product_type": product_type,
                    "charged_date": row[1]  # Assuming charged_date is the second column
                }
            print(self.my_dict_lupa)
            cnxn.close()

    def test_connect_to_db_in_lupa_DB(self):
        query = f"""
             SELECT a_num,FORMAT(CONVERT(datetime, charged_date), 'yyyy-MM-dd HH:mm:ss.fff') AS charged_date
             FROM [lupa].[dbo].[orders_tbl]
             WHERE  isnull(bulk_id, 0) = 0
             AND consolidate IS NULL
             AND in_status = 'Printing process'
             AND CONVERT(datetime, charged_date) < DATEADD(hour, -{hours}, GETDATE())
        """
        self.test_connect_to_db('lupa', query, "🖼️ Photo Album Desktop")

    def test_connect_to_db_in_lupa_online_DB(self):
        query = f"""
            SELECT order_id, charged_date FROM [lupa_online].[dbo].[order_item_tbl]
            WHERE in_status = 21 AND isnull(bulk_id, 0) = 0
            AND charged_date < DATEADD(hour, -{hours}, GETDATE())
        """
        self.test_connect_to_db('lupa_online', query, "📓 Photo Album Online")

    def test_connect_to_db_in_lupa_tiles_DB(self):
        query = f"""
            SELECT order_id, charged_date
            FROM [lupa_square].[dbo].[order_item_tbl]
            WHERE  isnull(bulk_id, 0) = 0
			AND (in_status = 21 OR in_status = 22) 
            AND charged_date < DATEADD(hour, -{hours}, GETDATE())
        """
        self.test_connect_to_db('lupa_square', query, "🖼️ Tiles Photo")

        if self.my_dict_lupa:
            self.send_to_email(self.my_dict_lupa)
            self.send_to_slack(self.my_dict_lupa)

            update_without_bulk = f"""
                UPDATE [lupa_online].[dbo].[order_item_tbl]
                SET in_status = 26
                WHERE bulk_id = 0 AND in_status = 21
                AND product_id = 3
                AND charged_date < DATEADD(hour, -{hours}, GETDATE())
            """
            update_without_bulk2 = f"""
                UPDATE [lupa_square].[dbo].[order_item_tbl]
                SET in_status = 26
                WHERE bulk_id = 0 AND in_status = 21
                AND charged_date < DATEADD(hour, -{hours}, GETDATE())
            """
            mysql(update_without_bulk)
            mysql(update_without_bulk2)

    def calculate_days_difference(self, provided_date_str):
        if isinstance(provided_date_str, datetime):
            provided_date = provided_date_str
        else:
            provided_date = datetime.strptime(provided_date_str, "%Y-%m-%d %H:%M:%S.%f")
        current_date = datetime.utcnow()
        difference = current_date - provided_date
        return difference.days + 1

    def json_to_slack_message(self, json_data):
        keys_list = list(json_data.keys())
        value_list = "\n".join([
            f"• <https://admin.lupa.co.il/admin_book/Order_Details.aspx?id={key}|{key}>" if str(key).startswith('19') else
            f"• <https://admin.lupa.co.il/admin_online/Order_Details.aspx?id={key}|{key}>" for key in keys_list
        ])

        blocks = [
            {"type": "section", "text": {"type": "mrkdwn", "text": "הזמנות ללא באלק :wave:"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": value_list}}
        ]

        payload = {"blocks": blocks}
        return json.dumps(payload)

    def json_to_html_table(self, json_data):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)

        rows = [f"<tr><td>{key}</td><td>{value['product_type']}</td></tr>" for key, value in json_data.items()]
        table = f"<table><tr><th>Key</th><th>Value</th></tr>{''.join(rows)}</table>"

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

    def send_to_email(self, my_dict_lupa):
        requests.post(
            "https://api.mailgun.net/v3/lupa.co.il/messages",
            auth=("api", os.getenv('MAILGUN_API_KEY')),
            data={
                "from": "Orders without bulk id <monitor@lupa.co.il>",
                "to": operators,
                "subject": "All orders without bulk id in 24 hours and with status Printing process!",
                "html": self.json_to_html_table(my_dict_lupa)
            }
        )

    def send_to_slack(self, my_dict_lupa):
        if datetime.now().weekday() != 4:
            message_text = "\n".join(
                f"{value['product_type']} Order {key} was charged {self.calculate_days_difference(value['charged_date'])} days ago."
                for key, value in my_dict_lupa.items())

            payload = {"text": "Orders without bulk id\n" + message_text}

            response = requests.post(
                "https://hooks.slack.com/services/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",
                json=payload
            )
            print(response.status_code, response.text)