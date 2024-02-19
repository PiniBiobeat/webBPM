import json

import psycopg2
import requests
import jsonpath


def check_if_have_user_with_delete():

        connection = psycopg2.connect(user="machineDBA",
                                      password="A#214Fdse!35dDC214XAzRDA12^79",
                                      host="35.233.19.13",
                                      port="5432",
                                      database="monitor_db")
        cursor = connection.cursor()
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        cursor.execute('''
                SELECT extra_params FROM public.error_tbl
                WHERE error_code = 85
                ORDER BY id DESC LIMIT 100
        ''')
        record = cursor.fetchall()

        print(len(record))
        print("You are connected to - ", record, "\n")

        if len(record) != 0:

            # Slack webhook URL (you need to obtain this from Slack)
            webhook_url = "YOUR_SLACK_WEBHOOK_URL"

            # Create the message payload
            message = {
                "text": f"need check user deleted.\n data ->  {record[0][0]}  ",
                "channel": "#general"
            }

            # Convert the message payload to JSON format
            print(message)
            payload = json.dumps(message)

            try:
                # Send the message to Slack
                response = requests.post("https://hooks.slack.com/services/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", data=payload)

                # Check the response status code
                if response.status_code == 200:
                    print("Message sent to Slack successfully.")
                else:
                    print("Failed to send the message to Slack. Status code:", response.status_code)

            except requests.RequestException as error:
                print("Error:", error)



check_if_have_user_with_delete()

