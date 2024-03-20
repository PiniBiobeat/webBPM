import json
import psycopg2
import requests
import jsonpath



def test_check_all_site_ver3_is_valid():
    global connection
    global cursor
    try:
        connection = psycopg2.connect(user="machineDBA",
                                      password="A#214Fdse!35dDC214XAzRDA12^79",
                                      host="35.187.190.6",
                                      port="5432",
                                      database="monitor_db")
        cursor = connection.cursor()

        # Retrieve records from the error_tbl table
        cursor.execute('''SELECT * FROM public.error_tbl
                        WHERE error_code = 30
                        ORDER BY id DESC LIMIT 100''')
        records = cursor.fetchall()

        # Print the number of records
        print(len(records))
        print("You are connected to - ", records, "\n")

        # Check if there are records
        if records != []:
            send_to_slack(len(records))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def json_to_slack_message(value_list):
    """
            Converts a JSON object to a formatted Slack message.

            Args:
                json_data (dict): The JSON data to convert to a Slack message.

            Returns:
                str: The formatted Slack message string.
            """
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"There are {value_list} orders with status 30 :wave:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": str(value_list)
            }
        }
    ]

    # Build the Slack message payload
    payload = {
        "blocks": blocks
    }

    # Convert the payload to JSON and return it
    return json.dumps(payload)


def send_to_slack(my_dict_lupa):
    payload = json_to_slack_message(my_dict_lupa)
    requests.post("https://hooks.slack.com/services/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",
                  data=payload)

test_check_all_site_ver3_is_valid()