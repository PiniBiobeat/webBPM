import json

import pyodbc
import requests
import psycopg2
from psycopg2 import Error


def test_check_newsletter():
		server = '104.155.49.95'
		database = 'lupa'
		username = 'MachineDBA'
		password = 'Kk28!32Zx'
		cnxn = pyodbc.connect(
			'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)
		cursor = cnxn.cursor()
		print(cursor)
		cursor.execute(
			'''  
				 SELECT *
					FROM (
						SELECT *
					FROM (
						SELECT *,
							   ROW_NUMBER() OVER (PARTITION BY [email] ORDER BY [sign_date] DESC) AS row_num
						FROM [lupa].[dbo].[newslleter]
					) AS SubQuery
					WHERE row_num = 1
					) AS n
					JOIN [lupa].[dbo].[user_master] AS m ON n.email = m.user_email
					WHERE ((n.newsletter_ststus = 1 AND m.newsletter = 'False')
					   OR (n.newsletter_ststus = 0 AND m.newsletter = 'True'))
	   ''')
		rows = cursor.fetchall()
		for row in rows:

				# Construct the message payload
				message = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":warning: *Error Alert Newsletter* :warning:"
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
					"text": "*Master ID:*"
				},
				{
					"type": "mrkdwn",
					"text": f"{row[9]}"
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
					"text": f"{row[7]}"
				}
			]
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "*Newsletter Table:*"
				},
				{
					"type": "mrkdwn",
					"text": f"{row[5]}"
				}
			]
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "*Newsletter UserMaster:*"
				},
				{
					"type": "mrkdwn",
					"text": f"{row[24]}"
				}
			]
		}
	]
}

				# Convert the message payload to JSON format
				payload = json.dumps(message)
				json_data = json.loads(payload)

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






