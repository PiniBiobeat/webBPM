import json

import requests



def test_check_get_delivery_calendar():
    url = "https://paymentsv4-api.lupa.co.il/api.aspx?method=get_delivery&source=tiles&source_type=tiles&language=&source_device=desktop&token=tIKxzLq2DpXhfKaojAiq64JPBL7rMbrlZCVq9nzONBd2V4pkHlsc1T7a_DKxxMRk_FtOVH0Br8tM4htwMzEqmE4uD52yYfzGVoC-WrFkEVkrSLsi7XkRTf2KuMh1YjP9BhY22BFeqEHhBbFiMAmL-XwX_SmfvR02dzdD732LdYcwr0yWbnN6pTnYcVb2vAxXpO30SbjgulGG5Is2YqgyQOWqP_bupDMKJX708AyhIGqimdMM3BHgg4zKlqECP-x3qJwuqqYILU2fCk3sPCWXhTHs_lQkrIvGbKcNw1i8g4BvlHX4K87sHUzAErdsY3xqix_9qZcPbIEL3QbXC8A96Q2&show_header=&newsletter=null"
    payload = {
  "items": [
    {
      "item_id": 929448,
      "item_guid": "00000000-0000-0000-0000-000000000000",
      "project_guid": "00000000-0000-0000-0000-000000000000",
      "url": "http://paymentsv4-api.lupa.co.il/ImageBasket.aspx?order_id=7764572&token=teHH4hWCiqzuBjza3imgD8_PX5pARAPgDVVkTDBU0_Z2Y2i3jWYILxGUzenF8G-HbeAzOLe8J320OcU02sWbIqFD4ibY6mZQEUEg_XcxYZj6IXc9zy60tT3b1Egu1KRIl6bjzDCTw1IywSz6b1ID4FYL4jIsZhKVs6uY-rwacLyi8SWm5hof0CIoaVhS4mYSbvAUmP_UAbQL4xpmxl-6-FU4WN1_g3eKwd9Ku07yyEyOtL13XANAzgWYpeJc1yltz6MUheDe9eJ9BLRhHGhIpUpbgbFfNJzb775gDNK2O74eIH7-4ZfzdDVYPXIl3On75b_rx1BBH0AgcPgZx0_XLQ2&project_tick=240516092213099-2",
      "itemImageUrl": "http://paymentsv4-api.lupa.co.il/ImageBasket.aspx?order_id=7764572&token=teHH4hWCiqzuBjza3imgD8_PX5pARAPgDVVkTDBU0_Z2Y2i3jWYILxGUzenF8G-HbeAzOLe8J320OcU02sWbIqFD4ibY6mZQEUEg_XcxYZj6IXc9zy60tT3b1Egu1KRIl6bjzDCTw1IywSz6b1ID4FYL4jIsZhKVs6uY-rwacLyi8SWm5hof0CIoaVhS4mYSbvAUmP_UAbQL4xpmxl-6-FU4WN1_g3eKwd9Ku07yyEyOtL13XANAzgWYpeJc1yltz6MUheDe9eJ9BLRhHGhIpUpbgbFfNJzb775gDNK2O74eIH7-4ZfzdDVYPXIl3On75b_rx1BBH0AgcPgZx0_XLQ2&project_tick=240516092213099-2",
      "parent_item_id": None,
      "product_type": 3,
      "format": 92,
      "material": None,
      "cover": -1,
      "theme": None,
      "pages": 0,
      "feature": None,
      "catalogue_code": "3_92_n_n_n_n_n_n",
      "title": "test me",
      "price_group": 0,
      "is_paspartu": None,
      "item_filter": None,
      "is_black_white": None,
      "frame_color": None,
      "quantity": 1,
      "item_q1_price": 0,
      "item_qx_price": 0,
      "item_final_price": 0,
      "item_total_price": 0,
      "discounts": None,
      "isChecked": False,
      "unit_price": 85,
      "price_list": 85,
      "base_price": 85,
      "quantity_discount": 0,
      "additional_discount": 0
    }
  ]
}
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
        'Cookie': 'ASP.NET_SessionId=j42jnukgapmthnzfqlmqm55l'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    json_data = json.loads(response.text)

    if  json_data["isValid"] != True:
            send_slack(json_data)


def send_slack(json_data):
    # If the assert condition is not met, send a message to Slack
        slack_webhook_url = "https://hooks.slack.com/services/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"

        error_message = f"The 'check_get_delivery_calendar' in calendar is return false .{json_data['errorMessage']}"

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


test_check_get_delivery_calendar()
