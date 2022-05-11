import time
import traceback
import imaplib
import email
import uuid
from email.header import decode_header
import requests
from datetime import datetime
import re

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "lupadevtest" + ORG_EMAIL
FROM_PWD = "lupadevtest!128"
SMTP_SERVER = "imap.gmail.com"
operators = ["pinim@lupa.co.il","adi@lupa.co.il"]
SMTP_PORT = 993
date_time = datetime.now()


def send_hook():

    url = 'https://files.lupa.co.il/lp/hooks.aspx?method=old_coupon&campaign_name=IncentiveBookBuyersDesktop&messageid=6547051775066112&email=lupadevtest@gmail.com&discount=40&days=3'
    response = requests.get(url).json()

    print(response)
    time.sleep(8)

def chack_if_email_exists(date_from_email_after_regex,subject,date_time_now):

    if subject == 'עפתם על הלופה? תזמינו לה עותק נוסף בהנחה שווה 😍' and date_from_email_after_regex == date_time_now:
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
              "from": "Lupa Automation ,Coupon Automation IncentiveBookBuyersDesktop  <monitor@lupa.co.il>",
              "to": operators,
              "subject": subject,
              "text": message,
              }
    )
def if_email_not_exists_send_email(result):

    send_email("The email not sent ** IncentiveBookBuyersDesktop **", result)

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
         print("Email not exists --עפתם על הלופה? תזמינו לה עותק נוסף בהנחה שווה 😍 -- ")
         if_email_not_exists_send_email("The user did not receive the email -- עפתם על הלופה? תזמינו לה עותק נוסף בהנחה שווה 😍--" + FROM_EMAIL)


def read_email():

    send_hook()

    try:
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
