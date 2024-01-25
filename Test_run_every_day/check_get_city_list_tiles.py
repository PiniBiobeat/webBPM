import json

import requests



def check_get_city_list_tiles():
    url = "https://paymentsv4-api.lupa.co.il/api.aspx?method=get_city_list&source_type=tiles&language=&source_device=desktop&token=075006004198174051194069114000059171223190201022241114097118246017106021141252132008248100179032200057179068154106101200050007232010073061230171&show_header="

    payload = {}
    headers = {
      'authority': 'paymentsv4-api.lupa.co.il',
      'accept': '*/*',
      'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
      'origin': 'https://paymentsv4-ui.lupa.co.il',
      'referer': 'https://paymentsv4-ui.lupa.co.il/',
      'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      'Cookie': 'ASP.NET_SessionId=xp2vl01tytfwykjvut525jd2'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    json_data = json.loads(response.text)

    if  json_data["isValid"] != True:
            send_slack(json_data)


def send_slack(json_data):
    # If the assert condition is not met, send a message to Slack
        slack_webhook_url = "https://hooks.slack.com/services/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"

        error_message = f"The 'get_city_list_tiles' in tiles is return false .{json_data['errorMessage']}"

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


check_get_city_list_tiles()
