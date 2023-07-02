import pyodbc
from datetime import datetime
import datetime
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

operators = ['pinim@lupa.co.il']
#'ben@lupa.co.il','pinim@lupa.co.il'
my_dict_lupa = dict()

hours = 8
class Test_me():



    def test_orders_with_orders_not_equal_items(self):
        server = '104.155.49.95'
        database = 'lupa_online'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute('''      select 
                                a.insert_date,
                                a.in_status,
                                --tree_version,
                                a.order_id,
                                a.total_items_quantity,
                                b.quantity
                                from orders_tbl a
                                join (select order_id ,SUM(quantity) as quantity 	from order_item_tbl group by order_id ) b
                                on  b.order_id = a.order_id
                                where b.quantity <> a.total_items_quantity
                                --and tree_version = '2.1.0' 
                               -- and a.in_status = 21
                               -- and a.in_status = 22 
                                and a.in_status = 21 
                                --and a.insert_date > DATEADD(HOUR, -24, GETDATE())
                                order by a.insert_date desc''')
        rows = cursor.fetchall()
        if rows != []:
            for row in rows:
                key = row[1]
                value = row[2]
                if key in my_dict_lupa:
                    my_dict_lupa[key].append(value)
                else:
                    my_dict_lupa[key] = [value]

               # my_dict_lupa[row[1]] = row[2]
            print(my_dict_lupa)
            self.send_to_email(my_dict_lupa)
            #self.send_to_email(my_dict_lupa)

        cursor.close()

        #self.send_to_slack(my_dict_lupa)


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
                    "text": "בדיקה של הזמנות עם הבדל במספר פריטים :wave:"
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

    def send_to_email(self, my_dict_lupa):
        requests.post(
            "https://api.mailgun.net/v3/lupa.co.il/messages",
            auth=("api", "key-d2ed6868aa56bfda882f84b173693a2a"),
            data={
                "from": "order_with_orders_not_equal_items  <monitor@lupa.co.il>",
                "to": operators,
                "subject": "בדיקה של הזמנות עם הבדל במספר פריטים! ",
                "html": self.json_to_html_table(my_dict_lupa)
            }
        )

    def send_to_slack(self, my_dict_lupa):
        payload = self.json_to_slack_message(my_dict_lupa)
        requests.post("https://hooks.slack.com/services/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",data=payload)
        print(payload)








