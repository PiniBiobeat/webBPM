import json
import requests
import psycopg2

# def test_check_errors_calendar():
#     try:
#         # PostgreSQL connection setup
#         connection = psycopg2.connect(user="machineDBA",
#                                       password="A#214Fdse!35dDC214XAzRDA12^79",
#                                       host="35.187.190.6",
#                                       port="5432",
#                                       database="monitor_db")
#         cursor = connection.cursor()
#
#         # Display PostgreSQL server information
#         print("PostgreSQL server information")
#         print(connection.get_dsn_parameters(), "\n")
#
#         # Query execution to fetch relevant records
#         cursor.execute('''
# SELECT distinct error_message,count(*) FROM public.reporting_log_tbl x
# WHERE "source" ='2_paymentv4' and error_message  <>'' and api_method not in ('writelog') and error_code not in (-15,-102)
# and created >='2024-10-06'
# group by error_message
#
#         ''')
#
#         # Fetch all records
#         records = cursor.fetchall()
#
#         # Display number of records fetched
#         print(len(records))
#         print("You are connected to - ", records, "\n")
#
#         # If records are found, send an error alert to Slack
#         if len(records) != 0:
#             # Prepare the message payload in Slack Block Kit format
#             if len(records) != 0:
#                 # Prepare the table-like message for Slack
#                 table_rows = "\n".join([f"*{record[0]}:* {record[1]}" for record in records])
#
#                 message = {
#                     "blocks": [
#                         {
#                             "type": "section",
#                             "text": {
#                                 "type": "mrkdwn",
#                                 "text": ":warning: *Error Alert* :warning:\nThe following errors occurred:"
#                             }
#                         },
#                         {
#                             "type": "divider"
#                         },
#                         {
#                             "type": "section",
#                             "text": {
#                                 "type": "mrkdwn",
#                                 "text": table_rows
#                             }
#                         }
#                     ]
#                 }
#
#                 # Convert the message payload to JSON format
#                 payload = json.dumps(message)
#
#             try:
#                 # Send the message to Slack
#                 response = requests.post("https://hooks.slack.com/services/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", data=payload)
#
#                 # Check the response status code
#                 if response.status_code == 200:
#                     print("Message sent to Slack successfully.")
#                 else:
#                     print("Failed to send the message to Slack. Status code:", response.status_code)
#
#             except requests.RequestException as error:
#                 print("Error:", error)
#
#     except (Exception, psycopg2.Error) as error:
#         print("Error while connecting to PostgreSQL:", error)
#
#     finally:
#         # Close cursor and connection
#         if connection:
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")
#
# # Run the test function
# test_check_errors_calendar()
