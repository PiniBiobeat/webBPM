import json

import psycopg2
import requests
import jsonpath


def test_check_errors_v3():

		connection = psycopg2.connect(user="machineDBA",
                                      password="A#214Fdse!35dDC214XAzRDA12^79",
                                      host="35.187.190.6",
                                      port="5432",
                                      database="monitor_db")
		cursor = connection.cursor()
		print("PostgreSQL server information")
		print(connection.get_dsn_parameters(), "\n")
		cursor.execute('''
                select * from error_tbl et
					inner join error_details ed on et.error_code = ed.code 
					where service_api = 'appV3' and  ed.priority_code = 4 AND et.insert_date  >= NOW() - INTERVAL '5 minutes'  
        ''')
		rows = cursor.fetchall()
		for row in rows:
				message =  {
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
										"text": "*source:*"
									},
									{
										"type": "mrkdwn",
										"text": f'{row[1]}'
									}
								]
							},
							{
								"type": "section",
								"fields": [
									{
										"type": "mrkdwn",
										"text": "*error code:*"
									},
									{
										"type": "mrkdwn",
										"text": f'{row[4]}'
									}
								]
							},
							{
								"type": "section",
								"fields": [
									{
										"type": "mrkdwn",
										"text": "*error message:*"
									},
									{
										"type": "mrkdwn",
										"text": f'{row[12]}'
									}
								]
							},
							{
								"type": "section",
								"fields": [
									{
										"type": "mrkdwn",
										"text": "*insert date:*"
									},
									{
										"type": "mrkdwn",
										"text": f'{row[7]}'
									}
								]
							}
						]
		}
				payload = json.dumps(message)

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


test_check_errors_v3()

