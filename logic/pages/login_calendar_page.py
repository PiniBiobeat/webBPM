from infra.page_base import PageBase
import time
import json
from playwright.sync_api import expect
import  pytest
import os
from infra.config.config_provider import configuration


class LoginCalendarPage(PageBase):

    click_open_menu =  "(//*[@type='button']//*[name()='svg'])[5]"
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    iframe_calendar = configuration['iframe_login_' + os.getenv('MY_KEY')]# os.environ.get('iframe_login_' +"env", "//iframe[@src='https://connect-v2-ui.lupa.co.il/loginregister?channel=calendar']")

    #test = 'https://connect-ui-v2.lupa.co/loginregister?channel=calendar'
    #https://connect-v2-ui.lupa.co.il/loginregister?channel=calendar
    text_first_name = "//input[@id=':r4:']"
    text_last_name = "//input[@id=':r5:']"
    text_email = "//input[@id=':r6:']"
    text_num_phone = "//input[@id=':r9:']"
    text_password1 = "//input[@id=':ra:']"
    text_password2 = "//input[@id=':rb:']"
    text_checkbox_newswetter = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[1]"
    text_checkbox = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[2]"
    text_button_create_user = '//button[contains(.,"יצירת חשבון")]//..//..//div[@class="MuiStack-root css-ax63s"]'
    text_user_login =  "//input[@class='MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd css-jnx2aw']"
    test_pass_login = "//input[@class='MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd css-1knobvl']"
    text_login_button = "//button[@data-testid='btn-login']"

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.iframe_calendar, state="visible")

    def shoose_sign_up(self):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_choose_create_user).click()

    def click_checkbox_with_newsletter(self):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_checkbox_newswetter).click()
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_checkbox).click()

    def insert_user_and_pass(self, text_user, text_pass):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_user_login).fill(text_user)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.test_pass_login).fill(text_pass)

    def click_login_button(self):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_login_button).click()

    def click_button_create_user(self):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_button_create_user).click()

    def take_token_online(self):
        time.sleep(8)
        token = self.pw_page.context.storage_state(path="state.json")
        user_token = token['origins'][0]['localStorage'][3]['value']
        return user_token

    def take_token_after(self):
        time.sleep(8)
        token = self.pw_page.context.storage_state(path="state.json")
        user_token =  token['origins'][0]['localStorage'][6]['value']
        return user_token

    def insert_user_details(self, firt_name, last_name, emailEx,num_phone, password):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_first_name).fill(firt_name)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_last_name).fill(last_name)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_email).fill(emailEx)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_num_phone).fill(num_phone)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_password1).fill(password)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_password2).fill(password)