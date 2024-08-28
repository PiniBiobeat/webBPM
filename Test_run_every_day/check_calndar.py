import json
import requests

def check_calendar_exsist():
    url ="https://calendarv4-api.lupa.co.il/api.aspx?method=getcalendar&calendar_token=7cdf03f725314174ae7df740e3246f0d&token=GkQpPolB6-5iLGhWB2dELatbnyidv6FkKkC-CymN23S4AmLrl9YiHKPX2FWvVGRJ2J4D2jj-HDaclNBxYPJMxSCDblmM9zglECn3udNIRgU8DO93hpafbtcUwiH7du6WD8RnL7zejaF_Vi7gQwNJ7-NCIWuW0w-Yyo4cc2Qo2zJtZuW9ZEmUptD5z1suULxXFsRz_nR7QHvHn026d9hFUjpsF5ER-TlRDeagij0CkD3jM-d9RVyrvjxy2Kpn9ID3seCdQFtSPHIQxUkXkvIU3uYPGcp9JhUe3_Fts3q88cMO6DVN2t5OxLntk2Mn_VgAO9TXbcpX1Qcz3n7bhwKsvw2"
    try:
        response = requests.request("GET", url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx and 5xx)

        json_data = json.loads(response.text)

        if json_data.get("isValid") != True:
            send_slack(f"Invalid response: {json_data}")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 500:
            send_slack(f"Server Error (500): {http_err}")
        else:
            send_slack(f"HTTP error occurred: {http_err}")
    except Exception as err:
        send_slack(f"An error occurred: {err}")

def send_slack(error_message):
    slack_webhook_url = "https://hooks.slack.com/services/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"

    # Send the error message to Slack
    payload = {
        "text": error_message
    }

    # Send the message to Slack using requests library
    response = requests.post(slack_webhook_url, json=payload)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to send message to Slack. Status Code: {response.status_code}")

# Run the test
check_calendar_exsist()
