import json

import requests



def check_get_all_cities_calendar():
    import requests

    url = "https://paymentsv4-api.lupa.co.il/api.aspx?method=get_all_cities&source_type=calendars&language=&source_device=mobile&token=rNJDeHiC9b20Vv7BY2L-3OCKE8AMUXk1dGM6lAP4MKzrl6uQqVqGeQJ8drgVU72xdjAXim6rfzxHSUZyD4Vl5vo3oJNFhYtrb6m5yOIkCk31JGjVFrK8UWntaq52TiH_jWJCFgf1QlccE_oY5d0OLnhUJ37mnD_s6dgH9IKZuDyDz3l8di-1bNfByljTbkimR67bNSJJOI71sK5Q_-_gSozX8Kbvnh8jI8_B11_VRzxHxjJEWLVvvmeiHsG2ESHUobNawd9vWEOLM3XdgYY5ylft5nylFwgr5bzLUuEIzJGcJdNUk913-X7Hyktt8BlhLucdq3FI09uTeaqusH-cjA2&show_header="

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://paymentsv4-ui.lupa.co.il',
        'priority': 'u=1, i',
        'referer': 'https://paymentsv4-ui.lupa.co.il/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'Cookie': 'ASP.NET_SessionId=uvtjgi2ikbcnkidbrgtsc3cb'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    json_data = json.loads(response.text)
    if  json_data["isValid"] != True:
            send_slack(json_data)


def send_slack(json_data):
    # If the assert condition is not met, send a message to Slack
        slack_webhook_url = "https://hooks.slack.com/services/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"

        error_message = f"The 'check_get_all_cities_calendar' in calendar is return false .{json_data['errorMessage']}"

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


check_get_all_cities_calendar()
