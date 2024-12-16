import requests

def get_token():
    url = "https://connect.lupa.co.il/V2/api/entry.aspx"
    params = {
        "method": "login",
        "callback": "iframe",
        "view": "gui",
        "password": "a123123",
        "email": "automation@lupa.co.il",
        "channel": "calendar",
        "temptoken": "",
        "remember": "true"
    }

    response = requests.post(url, data=params)
    if response.status_code == 200:
        response_data = response.json()
        return response_data.get("payLoad", {}).get("token", "")

    return None

# token = get_token()
# print(token)