import json

import psycopg2
import requests
import jsonpath


def test_check_roi_vision():

    class Error:
        def __init__(self, url, siteName):
            self.siteName = siteName
            self.url = url
    try:
        connection = psycopg2.connect(user="machineDBA",
                                      password="A#214Fdse!35dDC214XAzRDA12^79",
                                      host="35.233.19.13",
                                      port="5432",
                                      database="groupa")
        cursor = connection.cursor()
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        cursor.execute("SELECT roi_vision FROM groupav4.visions_tbl ORDER BY vision_id DESC, master_index DESC, album_token DESC LIMIT 1 ")
        record = cursor.fetchall()

        print(len(record))
        print("You are connected to - ", record, "\n")

        if record[0][0] == '':

            # Slack webhook URL (you need to obtain this from Slack)
            webhook_url = "YOUR_SLACK_WEBHOOK_URL"

            # Create the message payload
            message = {
                "text": "roi_vision NOT WORK!",
                "channel": "#general"
            }

            # Convert the message payload to JSON format
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



test_check_roi_vision()

