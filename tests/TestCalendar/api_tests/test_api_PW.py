from typing import Generator
import pytest
import os
import requests

users = [
    {"email": "pinim@lupa.co.il", "password": "Pinimari!1", "numOfBooks": 1, "index": 0},
    {"email": "test159487s@gmail.com", "password": "2z835yf", "numOfBooks": 1, "index": 3},
    {"email": "testbdika123456@gmail.com", "password": "ttttggg", "numOfBooks": 1, "index": 5},
    {"email": "testbdikot1122@gmail.com", "password": "A123456", "numOfBooks": 1, "index": 6},
    {"email": "connect1@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 7},
    {"email": "connect2@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 8},
    {"email": "connect3@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 9},
    {"email": "connect@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 10},
    {"email": "rwyr6407@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 12},
    {"email": "royroyh2@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 13},
    {"email": "testtcheck123@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 14},
    {"email": "royh8@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 15},
    {"email": "royhh89@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 16},
    {"email": "check458@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 18},
    {"email": "testbdikot1122@gmail.com", "password": "A123456", "numOfBooks": 1, "index": 22},
    {"email": "connect1@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 23},
    {"email": "connect2@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 24},
    {"email": "connect3@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 25},
    {"email": "connect@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 26},
    {"email": "rwyr6407@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 28},
    {"email": "royroyh2@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 29},
    {"email": "testtcheck123@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 30},
    {"email": "royh8@lupa.co.il", "password": "Aa123456", "numOfBooks": 1, "index": 31},
    {"email": "royhh89@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 32},
    {"email": "check458@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 34},
    {"email": "check789@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 36},
    {"email": "testbdikot112233@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 37},
    {"email": "roylupa1234@gmail.com", "password": "Aa123456", "numOfBooks": 1, "index": 38},
    {"email": "pinim12@lupa.co.il", "password": "pinimari1", "numOfBooks": 1, "index": 39},
    {"email": "pinim14@lupa.co.il", "password": "pinim1", "numOfBooks": 1, "index": 40},
    {"email": "pinim16@lupa.co.il", "password": "pinim1", "numOfBooks": 1, "index": 41},
    {"email": "pinimn31@lupa.co.il", "password": "22507624", "numOfBooks": 1, "index": 43},
    {"email": "pinimn30@lupa.co.il", "password": "06700023", "numOfBooks": 1, "index": 44},
    {"email": "pinimn50@lupa.co.il", "password": "pinim1", "numOfBooks": 1, "index": 45},
    {"email": "pinimmmp@gmail.com", "password": "noym2018", "numOfBooks": 1, "index": 46},
    {"email": "pinimmiry@gmail.com", "password": "pinim2", "numOfBooks": 1, "index": 47},
    {"email": "pinimaryy@gmail.com", "password": "noym2018", "numOfBooks": 1, "index": 48},
    {"email": "pinimary@gmail.com", "password": "pinim2018", "numOfBooks": 1, "index": 49},
    {"email": "pinimt@lupa.co.il", "password": "ppp111", "numOfBooks": 1, "index": 50},
    {"email": "pinimari@gmail.com", "password": "xxxx123", "numOfBooks": 1, "index": 51},
    {"email": "pinimar1@gmail.com", "password": "pinim2", "numOfBooks": 1, "index": 52},
    {"email": "pinim053@gmail.com", "password": "pinim053", "numOfBooks": 1, "index": 53},
    {"email": "pinimpinim@lupa.co.il", "password": "pinimpinim", "numOfBooks": 1, "index": 54},
    {"email": "ppppinim@lupa.co.il", "password": "pinim1", "numOfBooks": 1, "index": 55},
    {"email": "pinim55@gmail.com", "password": "pinimlupa55", "numOfBooks": 1, "index": 57},
    {"email": "pinimtobe@lupa.co.il", "password": "pinim1", "numOfBooks": 1, "index": 58},
    {"email": "pinimn56@lupa.co.il", "password": "18203910", "numOfBooks": 1, "index": 59},
    {"email": "pinimtest5@gmail.com", "password": "pinim20", "numOfBooks": 1, "index": 60},
    {"email": "pinimn20@lupa.co.il", "password": "qinsos-1vywhU-xydzes", "numOfBooks": 1, "index": 61}
]

def test_upload_image(filePath, album_token, token) -> None:
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://calendarv4-ui.lupa.co.il',
        'priority': 'u=1, i',
        'referer': 'https://calendarv4-ui.lupa.co.il/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    # Prepare the file data
    with open(filePath, "rb") as f:
        files = {
            "file": ("test.jpg", f, "image/jpeg")
        }
        payload = {}
        response = requests.post(
            "https://calendarv4-api.lupa.co.il/upload-browser.aspx",
            headers=headers,
            files=files,
            data=payload,
            params={
                "token": token,
                "event_token": album_token
            }
        )

    assert response.status_code == 200
    print("Upload response:", response.json())


def test_upload_file(event_token, token) -> None:
    for i in range(1, 50):
        file_path = f'C:\\Users\\tester\\Desktop\\repositories\\pytest-lupa\\tests\\TestCalendar\\image_london\\test{i}.jpg'
        test_upload_image(file_path, event_token, token)



def test_Get_login(user,password):

    url = f"https://connect.lupa.co.il/V2/api/entry.aspx?method=login&callback=iframe&view=gui&password={password}&email={user}&channel=calendar&temptoken="
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://connect-v2-ui.lupa.co.il',
        'priority': 'u=1, i',
        'referer': 'https://connect-v2-ui.lupa.co.il/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Cookie': 'ASP.NET_SessionId=jv3aetexns221evw42vad3iw'
    }
    payload = {}
    response = requests.get(url, headers=headers, data=payload)
    response_data = response.json()
    print("Login response:", response_data)
    test_Post_album_token(response_data['payLoad']['token'])


def test_Post_album_token(token):
    url = f"https://calendarv4-api.lupa.co.il/api.aspx?method=initcalendar&token={token}"
    payload = 'calendarSettings={"CalendarName":"sdf","Format":92,"ThemeName":"Black","DateSettings":{"StartYear":"2024","StartMonth":7,"IsHebrewDates":false,"IsHoliday":false,"HolidayCity":""},"calendarToken":""}'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://calendarv4-ui.lupa.co.il',
        'priority': 'u=1, i',
        'referer': 'https://calendarv4-ui.lupa.co.il/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()
    print("Album token response:", response_data)
    event_token = response_data['Response']['CalendarToken']
    test_upload_file(event_token, token)

def test_login_all_users():
    for user in users:
        email = user['email']
        password = user['password']
        test_Get_login(email, password)

