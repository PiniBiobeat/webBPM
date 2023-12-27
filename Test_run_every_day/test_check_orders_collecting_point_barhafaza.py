import pyodbc
import requests
import json

my_dict_lupa = dict()
data_to_send = []

class Test_me():
    my_dict_lupa = dict()

    def test_connect_to_and_check_orders_collecting_point_barhafaza(self):
        server = '104.155.49.95'
        database = 'master'
        username = 'MachineDBA'
        password = 'Kk28!32Zx'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        print(cursor)
        cursor.execute('''
                SELECT TOP (1000) [RowId]
                      ,[SiteId]
                      ,[SiteName]
                      ,[Address]
                      ,[City]
                      ,[Area]
                      ,[MapLink]
                      ,[Enable]
                      ,[InsertDate]
                  FROM [lupa].[dbo].[collecting_point_barhafaza_tbl]
                  WHERE InsertDate > DATEADD(day, -3, GETDATE())
                ORDER BY InsertDate DESC;
        ''')
        rows = cursor.fetchall()
        cursor.close()
        if rows == []:
            self.send_to_slack()
        else:
            assert True


    def send_to_slack(self):
        # Replace 'YOUR_WEBHOOK_URL' with your actual webhook URL
        webhook_url = 'https://hooks.slack.com/services/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'

        # Create a dictionary containing the message payload
        message_payload = {
            'text': f'orders without collecting point barhafaza !',
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








