import json
import time
import traceback
import imaplib
import email
import uuid
from email.header import decode_header
import requests
from datetime import datetime
import re

import urllib3
from playwright.sync_api import sync_playwright


ORG_EMAIL = "@gmail.com"

FROM_EMAIL = "couponsaoutomat" + ORG_EMAIL
FROM_PWD = "maripini"
SMTP_SERVER = "smtp.gmail.com"
operators = ["pinim@lupa.co.il"]
SMTP_PORT = 993
date_time = datetime.now()
url_token = "https://payments.lupa.co.il/v1/checkout.aspx?token=223162112143086108041059072224085117055012015193017171017225063179088126115061190231207181239206167254092119250116100147141161254102026055247229&lang=he&app_version=2.10.35&device_type=android"
URL = 'http://files.lupa.co.il/lp/hooks.aspx?method=coupon&messageid=4580023812030464&email=couponsaoutomat@gmail.com&campaign_name=AbandonedCartBook'
webhook_url = "https://hooks.slack.com/services/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"
url_delete_coupon = 'http://service.v2.lupa.co/api/coupons.aspx?method=change_status&name=AbandonedCartBook&master_id=3502298'

def maks_hook():
    URL_1 = URL
    response = requests.get(URL_1)
    print(response)
    if response.status_code == 200:
        check_in_payment()
        #check_gmail()
    else:
        send_email("not send hook", FROM_EMAIL)
        slack_notification("not send hook" + "  -> " + FROM_EMAIL)

def check_gmail():

    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')
        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        check_all_emails(first_email_id, latest_email_id, mail)

    except Exception as e:
        traceback.print_exc()
        print(str(e))
        check_in_payment()
        #send_email("not send hook", FROM_EMAIL)

def check_all_emails(first_email_id, latest_email_id,mail):

    isValid = True
    for i in range(latest_email_id, first_email_id, -1):
        data = mail.fetch(str(i), '(RFC822)')
        for response_part in data:
            arr = response_part[0]
            if isinstance(arr, tuple):
                msg = email.message_from_string(str(arr[1], 'utf-8'))
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding)
                    date_time_now = date_time.strftime("%d %b %Y")
                    date_from_email = msg["date"]
                    result = re.search(r"(\d{2}) (\w+) (\d{4})", date_from_email)
                    date_from_email_after_regex = result.group()
                    isValid = chack_if_email_exists(date_from_email_after_regex, subject, date_time_now)
                    if isValid:
                        break
        if isValid:
            break
    check_in_payment()
    if not isValid:
         print("עוד לא הספקת להגיד לופה וכבר הגענו עם ההטבה 😍 -- ")
         send_email("the coupon email not found ",FROM_EMAIL)
         slack_notification("the coupon email not found " + "  -> " + FROM_EMAIL)

def chack_if_email_exists(date_from_email_after_regex,subject,date_time_now):

    if subject == 'עוד לא הספקת להגיד לופה וכבר הגענו עם ההטבה 😍' and date_from_email_after_regex == date_time_now:
      print('Subject : ' + subject + '\n')
      print('The date now  : ' + date_time_now + ',  The date from email : ' + date_from_email_after_regex + '\n')
      print("+++++++++++")

      return True
    else:
      return False

def check_in_payment():
    playwright = sync_playwright().start()
    pixel_2 = playwright.devices['Pixel 2']
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(**pixel_2, )
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()
    page.goto(url_token, wait_until="load")
    text = page.text_content("//span[@class='price-label' and contains(.,'הנחת קופון אישי')]")
    print(page.title())
    time.sleep(5)
    browser.close()
    if text != 'הנחת קופון אישי':
        print("coupon not in payment")
        send_email("coupon not in payment",FROM_EMAIL)
        slack_notification("coupon not in payment" + "  -> " + FROM_EMAIL)
    else:
        print("the coupon apper in payment")
        delete_coupon()

def delete_coupon():
    url_delete = url_delete_coupon
    response = requests.get(url_delete).json()
    print(response)
    if response['isValid'] != True:
        send_email("the coupon not deleted",FROM_EMAIL)
        slack_notification("the coupon not deleted" + "  -> " + FROM_EMAIL)

def send_email(subject, message):
    return requests.post(
        "https://api.mailgun.net/v3/lupa.co.il/messages",
        auth=("api", "key-d2ed6868aa56bfda882f84b173693a2a"),
        data={
            "from": "Lupa Automation ,Coupon Automation WelcomePopupApp  <monitor@lupa.co.il>",
            "to": operators,
            "subject": subject,
            "text": message,
        }
    )

def slack_notification(message):
        try:
            slack_message = {'text': message}

            http = urllib3.PoolManager()
            response = http.request('POST',
                                    webhook_url,
                                    body=json.dumps(slack_message),
                                    headers={'Content-Type': 'application/json'},
                                    retries=False)
        except:
            traceback.print_exc()

        return True

maks_hook()