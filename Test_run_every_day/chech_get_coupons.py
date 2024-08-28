import json
import requests


def test_check_get_coupons_calendar():
    url = "https://paymentsv4-api.lupa.co.il/api.aspx?method=get_coupons&source_type=calendars&language=&source_device=mobile&token=Xnhtj1kGWbEm1fVOZSWLQVHjQekB2mhD1ICFcHjts0oT9h1sRJTAXU3UkJJYabaHyPLP2g-D-k3CzQMWX26vpp4nAvoJ_nDuQ-0qJmdEaA6OGQhJIMCOlYzR_3_ILK1PfrXByMZufOGXhzN8AauTN-dUwIBa1D82vCLg4rwpP47reefNuR7OuQP9obBIUfrMyBHAl2fXoAIKo12f5t4bnoVo0AKwgAODEqxe3QygGodBLkE5BmmTj9cwPIROiVexgY6icDbuPeX_Vt9Jfu5zPjmjDx4m-A44kz6FCuIzSiXP8FKGnKRL6pEJOdUPWKu1nqyLMXCbbfw2TeAjKvdoEg2&show_header=&newsletter=null"
    payload = '[{"id":4,"estimatedDate":"10/06/2024","estimatedDays":10,"productionDays":5,"name":"registered","displayName":"דואר רשום","isAvailable":true,"price":30,"priceForClubMember":26}]'
    headers = {
        'accept': '*/*',
        'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://paymentsv4-ui.lupa.co.il',
        'priority': 'u=1, i',
        'referer': 'https://paymentsv4-ui.lupa.co.il/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Cookie': 'ASP.NET_SessionId=utbwzm5cn5tmo1hgpu00r3tx'
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx and 5xx)

        json_data = response.json()  # Parse JSON response directly to dictionary

        if json_data.get("isValid") != True:
            send_slack(f"Invalid response: {json_data.get('errorMessage', 'No error message provided')}")
    except requests.exceptions.HTTPError as http_err:
        try:
            json_data = response.json()  # Attempt to parse JSON again in case of error
        except ValueError:
            json_data = {}  # Use an empty dictionary if parsing fails

        if response.status_code == 500:
            send_slack(f"Server Error (500): {json_data.get('errorMessage', 'No error message provided')}")
        else:
            send_slack(f"HTTP error occurred: {json_data.get('errorMessage', 'No error message provided')}")
    except Exception as err:
        send_slack(f"An error occurred: {str(err)}")


def send_slack(message):
    """Send a message to Slack using a webhook URL."""
    slack_webhook_url = "https://hooks.slack.com/services/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"

    payload = {
        "text": message,
        "username": "Error Bot",
        "channel": "#your-error-channel"
    }

    response = requests.post(slack_webhook_url, json=payload)

    if response.status_code != 200:
        print(f"Failed to send message to Slack. Status Code: {response.status_code}")


test_check_get_coupons_calendar()
