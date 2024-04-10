import json

import psycopg2
import requests
import jsonpath


def check_PDF_calendar():

    class Error:
        def __init__(self, url, siteName):
            self.siteName = siteName
            self.url = url

    try:
        connection = psycopg2.connect(user="machineDBA",
                                      password="A#214Fdse!35dDC214XAzRDA12^79",
                                      host="35.187.190.6",
                                      port="5432",
                                      database="monitor_db")
        cursor = connection.cursor()
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        cursor.execute('''
                    SELECT * FROM public.reporting_log_tbl
                    WHERE "source" ='Create_Calendar_PDF_Service' and error_code <>0
                    AND  created > NOW() - INTERVAL '5 minutes' LIMIT 1
            ''')
        record = cursor.fetchall()

        print(len(record))
        print("You are connected to - ", record, "\n")

        if len(record) != 0:

            message = {
                                "blocks": [
                                    {
                                        "type": "section",
                                        "text": {
                                            "type": "mrkdwn",
                                            "text": ":warning: *Error Alert* :warning:"
                                        }
                                    },
                                    {
                                        "type": "divider"
                                    },
                                    {
                                        "type": "section",
                                        "fields": [
                                            {
                                                "type": "mrkdwn",
                                                "text": "*Order ID:*"
                                            },
                                            {
                                                "type": "mrkdwn",
                                                "text": f'{record[0][0]}'
                                            }
                                        ]
                                    },
                                    {
                                        "type": "section",
                                        "fields": [
                                            {
                                                "type": "mrkdwn",
                                                "text": "*Error Message:*"
                                            },
                                            {
                                                "type": "mrkdwn",
                                                "text": f'{record[0][14]}'
                                            }
                                        ]
                                    },
                                    {
                                        "type": "section",
                                        "fields": [
                                            {
                                                "type": "mrkdwn",
                                                "text": "*Source:*"
                                            },
                                            {
                                                "type": "mrkdwn",
                                                "text": f'{record[0][3]}'
                                            }
                                        ]
                                    },
                                    {
                                        "type": "section",
                                        "fields": [
                                            {
                                                "type": "mrkdwn",
                                                "text": "*Transaction:*"
                                            },
                                            {
                                                "type": "mrkdwn",
                                                "text":f'{record[0][1]}'
                                            }
                                        ]
                                    }
                                ]
                            }

            # Convert the message payload to JSON format
            print(message)

            payload = json.dumps(message)
            json_data = json.loads(payload)

            try:
                # Send the message to Slack
                response = requests.post(
                    "https://hooks.slack.com/services/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", data=payload)

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



check_PDF_calendar()

