import pyodbc
import requests
import json




class Test_coupon_invalid():


    def test_coupon_invalid(self):
        server = '104.155.49.95'
        database = 'lupa_online'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute(f"select charged_date,order_id from [lupa_online].[dbo].[order_item_tbl] where charged_date > '2023-08-27 14:09:32.347' and discount_sale_name = 'ספר מתנה'")
        rows = cursor.fetchall()
        if rows != []:
            self.send_to_slack(rows[0][1])
        cursor.close()


    def send_to_slack(self, my_dict_lupa):

        # Replace 'YOUR_WEBHOOK_URL' with your actual webhook URL
        webhook_url = 'https://hooks.slack.com/services/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'

        # Create a dictionary containing the message payload
        message_payload = {
            'text': f'Order Number!{my_dict_lupa}',
            'username': 'monitor',  # Optional: Customize the username
            'icon_emoji': ':robot_face:',  # Optional: Customize the icon
        }

        # Convert the payload to JSON format
        payload_json = json.dumps(message_payload)

        # Send the POST request to the Slack webhook URL
        response = requests.post(webhook_url, data=payload_json, headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            print("Message sent successfully")
        else:
            print(f"Error sending message: {response.text}")







