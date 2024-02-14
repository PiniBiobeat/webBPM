import json
import requests


def check_update_item():

    url = "https://paymentsv4-api.lupa.co.il/api.aspx?method=update_item&format=0&item_id=938190&quantity=2&item_color=2&item_material=2&is_basket_callback=false&source_type=tiles&language=&source_device=desktop&token=tIKxzLq2DpXhfKaojAiq64JPBL7rMbrlZCVq9nzONBd2V4pkHlsc1T7a_DKxxMRk_FtOVH0Br8tM4htwMzEqmE4uD52yYfzGVoC-WrFkEVkrSLsi7XkRTf2KuMh1YjP9BhY22BFeqEHhBbFiMAmL-XwX_SmfvR02dzdD732LdYcwr0yWbnN6pTnYcVb2vAxXpO30SbjgulGG5Is2YqgyQOWqP_bupDMKJX708AyhIGqimdMM3BHgg4zKlqECP-x3qJwuqqYILU2fCk3sPCWXhTHs_lQkrIvGbKcNw1i8g4BvlHX4K87sHUzAErdsY3xqix_9qZcPbIEL3QbXC8A96Q2&show_header="
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
        'Cookie': 'ASP.NET_SessionId=ob3av0ohfvtvrg4vwl5a3w3k'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    json_data = json.loads(response.text)

    if  json_data["isValid"] != True:
        send_slack(json_data)


def send_slack(json_data):
    # If the assert condition is not met, send a message to Slack
        slack_webhook_url = "https://hooks.slack.com/services/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"

        error_message = f"The 'update_item' in tiles is return false .{json_data['errorMessage']}"

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


check_update_item()