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


def send_slack(block):
    """Send a message to Slack using a webhook URL."""
    # slack_webhook_url = "https://hooks.slack.com/services/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"
    paymentv4 = "https://hooks.slack.com/services/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"

    payload = {
        "blocks": block,

    }

    try:
        response = requests.post(paymentv4, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")