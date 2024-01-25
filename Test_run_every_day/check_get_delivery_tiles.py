import json

import requests



def check_get_delivery_tiles():
    url = "https://paymentsv4-api.lupa.co.il/api.aspx?method=get_delivery&source=tiles&source_type=tiles&language=&source_device=desktop&token=075006004198174051194069114000059171223190201022241114097118246017106021141252132008248100179032200057179068154106101200050007232010073061230171&show_header=&newsletter=null"

    payload = {"items":[{"item_id":938190,"item_guid":"00000000-0000-0000-0000-000000000000","project_guid":"00000000-0000-0000-0000-000000000000","url":"https://tiles-api.lupa.co.il/img.aspx?token=075006004198174051194069114000059171223190201022241114097118246017106021141252132008248100179032200057179068154106101200050007232010073061230171&image=B44c1094f7e644a6b8ac414ed3e08dffd.jpg&projectguid=52722f90274949beb61e95c28aedff0f&type=no","itemImageUrl":"https://paymentsv4-api.lupa.co.il//img/black_frame.svg","parent_item_id":None,"product_type":7,"format":0,"material":2,"cover":None,"theme":None,"pages":None,"feature":None,"catalogue_code":"7_0_n_2_2_n_n_n","title":None,"price_group":0,"is_paspartu":False,"item_filter":"no","is_black_white":False,"frame_color":2,"quantity":1,"item_q1_price":0,"item_qx_price":0,"item_final_price":0,"item_total_price":0,"discounts":None,"isChecked":False,"unit_price":42,"price_list":42,"base_price":42,"quantity_discount":0,"additional_discount":0}]}
    headers = {
        'authority': 'paymentsv4-api.lupa.co.il',
        'accept': '*/*',
        'accept-language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'text/plain;charset=UTF-8',
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

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    json_data = json.loads(response.text)

    if  json_data["isValid"] != True:
            send_slack(json_data)


def send_slack(json_data):
    # If the assert condition is not met, send a message to Slack
        slack_webhook_url = "https://hooks.slack.com/services/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"

        error_message = f"The 'check_get_delivery_tiles' in tiles is return false .{json_data['errorMessage']}"

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


check_get_delivery_tiles()
