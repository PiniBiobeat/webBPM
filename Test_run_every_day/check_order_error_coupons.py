import json

import psycopg2
import requests
import jsonpath


def check_orders_with_error_coupons():

    class Error:
        def __init__(self, url, siteName):
            self.siteName = siteName
            self.url = url
    try:
        connection = psycopg2.connect(user="machineDBA",
                                      password="A#214Fdse!35dDC214XAzRDA12^79",
                                      host="35.233.19.13",
                                      port="5432",
                                      database="Tariff")
        cursor = connection.cursor()
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        cursor.execute('''
                SELECT order_id,user_id,finished,error_code,error_message FROM cpn.service_log_tbl
                WHERE error_code <> 0 AND error_code <> 900 
                AND finished > '2024-01-30' AND finished > NOW() - INTERVAL '5 minutes' LIMIT 1;
        ''')
        record = cursor.fetchall()

        print(len(record))
        print("You are connected to - ", record, "\n")

        if len(record) != 0:

            # Slack webhook URL (you need to obtain this from Slack)
            webhook_url = "YOUR_SLACK_WEBHOOK_URL"

            # Create the message payload
            message = {
                "text": f"need check errors on new coupons.\n error ->  {record[0][4]} .\n order num -> {record[0][0]} .\n master id -> {record[0][1]}. ",
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


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



check_orders_with_error_coupons()

