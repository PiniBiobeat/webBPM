from datetime import datetime
from playwright.sync_api import sync_playwright
#import pytest
import ast
import urllib3
import json
import traceback


ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "couponsaoutomat" + ORG_EMAIL
FROM_PWD = "maripini"
SMTP_SERVER = "imap.gmail.com"
operators = ["pinim@lupa.co.il","adi@lupa.co.il"]
SMTP_PORT = 993
date_time = datetime.now()
url_token = "https://tiles-tiny.lupa.co.il/"
list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
tiles_button = '(//span[@class="lupa-btn-content"])[1]'
input_photo = "//input[@id= 'f']"
button_click_to_buy = "//button[@class='lupa-btn']"
login_to_existing_account = "//span[@class='lupa-btn-content' and contains(.,'כניסה')]"
text_user = "pinim4@lupa.co.il"
text_pass = "pinim1"
locators_user_name  = "//input[@type='text']"
locators_pass = "//input[@type='password']"
click_login = "//span[@class='lupa-btn-content']"
approve_image = "//button[@class='lupa-btn']//..//..//div[@class='center-btn']"
click_sum_order = "//button[@class='lupa-btn' and contains(.,'לסיכום הזמנה')]"
add_coupon = "//button[@class='add_code']"
imput_code = "//input[@autocomplete='new-password']"
code_coupon = "12930"
save_coupons = "//button[@class='lupa-btn' and contains(.,'למימוש קופון')]"
button_ok = "//button[@class='lupa-btn' and contains(.,'הבנתי')]"
go_to_shipping = "//button[@class='lupa-btn' and contains(.,'לבחירת משלוח')]"
choose_shipping = "//input[@type='checkbox']//..//..//..//div[@class='details' and contains(.,'אספתא')]"
next_payment = "//button[@class='lupa-btn' and contains(.,'לתשלום')]"
checkbox_approve = "//input[@type='checkbox']//..//..//..//div[@class='checkbox']"
webhook_url = "https://hooks.slack.com/services/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"

def send_event():

    playwright = sync_playwright().start()
    pixel_2 = playwright.devices['Pixel 2']
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(**pixel_2, )
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()
    page.goto(url_token, wait_until="load")
    page.click(tiles_button)
    page.set_input_files(input_photo,list[0])
    page.click(button_click_to_buy)
    page.click(approve_image)
    page.click(button_click_to_buy)
    page.click(login_to_existing_account)
    page.fill(locators_user_name,text_user)
    page.fill(locators_pass,text_pass)
    page.click(click_login)
    page.click(click_sum_order)
    page.click(add_coupon)
    page.fill(imput_code,code_coupon)
    page.click(save_coupons)
    page.click(button_ok)
    page.click(go_to_shipping)
    page.click(choose_shipping)
    page.click(next_payment)
    page.click(next_payment)
    page.click(checkbox_approve)
    page.click(next_payment)
    page.click(next_payment)
    text_title_login1 = page.frame_locator("//iframe[@class='credit_guard_frame']").locator("//input[@id='tmpHelper']").input_value()
    result = ast.literal_eval(text_title_login1)
    if result['event'] !=  'eec.transaction':
        slack_notification('The event sent correct '+ "  -> " + result['event'])

        print(result['event'])
    else:
        print("The event sent correct")
        print(page.title())
        browser.close()

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

send_event()





