import pyodbc
from datetime import datetime
import datetime
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
my_dict_lupa = dict()
from data_base import mysql


#'ben@lupa.co.il','pinim@lupa.co.il'

operators = ['pinim@lupa.co.il']
hours = 8
class Test_me():
    my_dict_lupa = dict()

    def test_connect_to_db_in_lupa_DB(self):
        server = '104.155.49.95'
        database = 'lupa'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute(f"select *  FROM [lupa].[dbo].[orders_tbl] where bulk_id is null and consolidate IS NULL and in_status = 'Printing process' and charged_date < DATEADD(hour, -{hours}, GETDATE())")
        rows = cursor.fetchall()
        if rows != []:
            for row in rows:
                my_dict_lupa[row[0]] = " 🖼️ Photo Album Desktop"
        print(my_dict_lupa)


        cursor.close()

    def test_connect_to_db_in_lupa_online_DB(self):
        server = '104.155.49.95'
        database = 'lupa_online'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute(f"select *  FROM [lupa_online].[dbo].[order_item_tbl] where bulk_id = 0   and in_status = 21 and  charged_date < DATEADD(hour, -{hours}, GETDATE())")
        rows = cursor.fetchall()
        if rows != []:
            for row in rows:
                if row[37] == 3:  # Check if row[37] equals 1
                    my_dict_lupa[row[1]] =  " 🗓️ Calendar"
                else:
                    my_dict_lupa[row[1]] = " 📓 Photo Album Online"
            print(my_dict_lupa)
            #self.send_to_email(my_dict_lupa)


        cursor.close()

    def test_connect_to_db_in_lupa_tiles_DB(self):
        server = '104.155.49.95'
        database = 'lupa_square'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute(f"select *  FROM [lupa_square].[dbo].[order_item_tbl] where bulk_id = 0   and in_status = 21 and charged_date < DATEADD(hour, -{hours}, GETDATE())")
        rows = cursor.fetchall()
        if rows != []:
            for row in rows:
                my_dict_lupa[row[1]] = " 🖼️ Tiles Photo"
            print(my_dict_lupa)
        cursor.close()
        if len(my_dict_lupa) > 0:
            self.send_to_email(my_dict_lupa)
            self.send_to_slack(my_dict_lupa)



            #set 26 to orders without bulk id
            update_withoutbalk = f"update [lupa_online].[dbo].[order_item_tbl] set in_status = 26 where bulk_id = 0 and in_status = 21 and product_id = 3 and charged_date < DATEADD(hour, -{hours}, GETDATE())"
            update_withoutbalk2 = f"update [lupa_square].[dbo].[order_item_tbl] set in_status = 26 where bulk_id = 0 and in_status = 21 and charged_date < DATEADD(hour, -{hours}, GETDATE())"
            mysql(update_withoutbalk)
            mysql(update_withoutbalk2)




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
                    "text": "הזמנות ללא באלק :wave:"
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
                "from": "Orders without bulk id   <monitor@lupa.co.il>",
                "to": operators,
                "subject": "all orders orders without bulk id in 24 hours and with status Printing process ! ",
                "html": self.json_to_html_table(my_dict_lupa)
            }
          )

    def send_to_slack(self, my_dict_lupa):

        if datetime.now().weekday() != 4:


            message_text = "\n".join(f"{key}: {value}" for key, value in my_dict_lupa.items())

            # Build the payload in the format Slack expects
            payload = {
                "text":  "Orders without bulk id\n" + message_text  # Ensure it’s a plain-text string
            }

            # Send the payload as JSON
            response = requests.post(
                "https://hooks.slack.com/services/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",
                json=payload
            )

            # Print response details for debugging
            print(response.status_code, response.text)








