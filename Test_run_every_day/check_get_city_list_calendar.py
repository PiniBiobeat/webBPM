import json

import requests



def check_get_city_list_calendar():
    url = "https://paymentsv4-api.lupa.co.il/api.aspx?method=get_city_list&source_type=calendars&language=&source_device=mobile&token=teHH4hWCiqzuBjza3imgD8_PX5pARAPgDVVkTDBU0_Z2Y2i3jWYILxGUzenF8G-HbeAzOLe8J320OcU02sWbIqFD4ibY6mZQEUEg_XcxYZj6IXc9zy60tT3b1Egu1KRIl6bjzDCTw1IywSz6b1ID4FYL4jIsZhKVs6uY-rwacLyi8SWm5hof0CIoaVhS4mYSbvAUmP_UAbQL4xpmxl-6-FU4WN1_g3eKwd9Ku07yyEyOtL13XANAzgWYpeJc1yltz6MUheDe9eJ9BLRhHGhIpUpbgbFfNJzb775gDNK2O74eIH7-4ZfzdDVYPXIl3On75b_rx1BBH0AgcPgZx0_XLQ2&show_header="
    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://paymentsv4-ui.lupa.co.il',
        'priority': 'u=1, i',
        'referer': 'https://paymentsv4-ui.lupa.co.il/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Cookie': 'ASP.NET_SessionId=j42jnukgapmthnzfqlmqm55l'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    json_data = json.loads(response.text)

    if  json_data["isValid"] != True:
            send_slack(json_data)


def send_slack(json_data):
    # If the assert condition is not met, send a message to Slack
        slack_webhook_url = "https://hooks.slack.com/services/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"

        error_message = f"The 'get_city_list_calendar' in calendar is return false .{json_data['errorMessage']}"

        # You can customize the message format according to your needs
        payload = {
            "text": error_message,
            "username": "Error Bot",
            "channel": "#your-error-channel"
        }

        # Send the message to Slack using requests library
        response = requests.post(slack_webhook_url, json=payload)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to send message to Slack. Status Code: {response.status_code}")


check_get_city_list_calendar()
