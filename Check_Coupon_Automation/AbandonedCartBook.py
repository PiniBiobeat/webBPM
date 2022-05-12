import time
import traceback
import imaplib
import email
import uuid
from email.header import decode_header
import requests
from datetime import datetime
import re
from playwright.sync_api import sync_playwright
import psycopg2
ORG_EMAIL = "@gmail.com"

FROM_EMAIL = "couponsaoutomat" + ORG_EMAIL
FROM_PWD = "maripini"
SMTP_SERVER = "imap.gmail.com"
operators = ["pinim@lupa.co.il","adi@lupa.co.il"]
SMTP_PORT = 993
date_time = datetime.now()
url_token = "https://payments.lupa.co.il/v1/checkout.aspx?token=223162112143086108041059072224085117055012015193017171017225063179088126115061190231207181239206167254092119250116100147141161254102026055247229&lang=he&app_version=2.10.35&device_type=android"

def send_hook():

    url = 'http://files.lupa.co.il/lp/hooks.aspx?method=coupon&messageid=4580023812030464&email=couponsaoutomat@gmail.com&campaign_name=AbandonedCartBook'
    response = requests.get(url).json()
    print(response)
    time.sleep(5)
    if response != 200:
        if_email_not_exists_send_email("פיני, מגיע לך קופון הנחה לרכישת הלופה 🎁 --" + FROM_EMAIL)

def chack_if_email_exists(date_from_email_after_regex,subject,date_time_now):

    if subject == 'פיני, מגיע לך קופון הנחה לרכישת הלופה 🎁' and date_from_email_after_regex == date_time_now:
      print('Subject : ' + subject + '\n')
      print('The date now  : ' + date_time_now + ',  The date from email : ' + date_from_email_after_regex + '\n')
      print("+++++++++++")

      return True
    else:
      return False

def send_email(subject, message):

    return requests.post(
        "https://api.mailgun.net/v3/lupa.co.il/messages",
        auth=("api", "key-d2ed6868aa56bfda882f84b173693a2a"),
        data={
              "from": "Lupa Automation ,Coupon Automation AbandonedCartBook  <monitor@lupa.co.il>",
              "to": operators,
              "subject": subject,
              "text": message,
              }
    )
def if_email_not_exists_send_email(result):

    send_email("The email not sent ** AbandonedCartBook **", result)

def check_in_payment():

        playwright = sync_playwright().start()
        pixel_2 = playwright.devices['Pixel 2']
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(**pixel_2, )
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        page.goto(url_token,wait_until="load")
        text = page.text_content("//span[@class='price-label' and contains(.,'הנחת קופון אישי')]")
        print(page.title())
        browser.close()
        if text != 'הנחת קופון אישי':
            print("Email not exists --פיני, מגיע לך קופון הנחה לרכישת הלופה 🎁-- ")
            if_email_not_exists_send_email("פיני, מגיע לך קופון הנחה לרכישת הלופה 🎁 --" + FROM_EMAIL)

def delete_coupon():

    url = 'http://service.v2.lupa.co/api/coupons.aspx?method=change_status&name=AbandonedCartBook&master_id=3502298'
    response = requests.get(url).json()
    print(response)
    if response['isValid'] != True:
        if_email_not_exists_send_email("פיני, מגיע לך קופון הנחה לרכישת הלופה 🎁 --" + FROM_EMAIL)

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

    if not isValid:
         print("פיני, מגיע לך קופון הנחה לרכישת הלופה 🎁 -- ")
         if_email_not_exists_send_email("פיני, מגיע לך קופון הנחה לרכישת הלופה 🎁 --" + FROM_EMAIL)

def read_email():

    try:

        send_hook()
        check_in_payment()
        delete_coupon()
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        check_all_emails(first_email_id,latest_email_id,mail)

    except Exception as e:
        traceback.print_exc()
        print(str(e))

read_email()
