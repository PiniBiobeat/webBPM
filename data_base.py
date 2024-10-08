import json
import pyodbc


import pyodbc
import requests


def mysql(mysql_execute):
    server = '104.155.49.95'
    database = 'lupa'
    username = 'MachineDBA'
    password = 'Kk28!32Zx'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Encrypt = Optional;UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()
    query1 = mysql_execute
    cursor.execute(query1)
    result1 = cursor.fetchall()
    cursor.close()
    return result1






# def send_slack(message):
#     """Send a message to Slack using a webhook URL."""
#     slack_webhook_url = "https://hooks.slack.com/services/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"
#
#     payload = {
#         "text": message,
#         "username": "Error Bot",
#         "channel": "#מוניטור-הזמנות",
#         "icon_emoji": ":camera:"
#     }


orders = "https://hooks.slack.com/services/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"
demoapp = "https://hooks.slack.com/services/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"
def send_slack(block):
    """Send a message to Slack using a webhook URL."""
    paymentv4 = demoapp

    payload = {
        "blocks": block,

    }

    try:
        response = requests.post(paymentv4, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")