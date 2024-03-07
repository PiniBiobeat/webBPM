from infra.page_base import PageBase
import time
import json
from playwright.sync_api import expect



class LoginCalendarPage(PageBase):

    click_open_menu =  "(//*[@type='button']//*[name()='svg'])[5]"
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    iframe_calendar = "//iframe[@src='https://connect-v2-ui.lupa.co.il/loginregister?channel=calendar']"
    text_first_name = "//input[@id=':r4:']"
    text_last_name = "//input[@id=':r5:']"
    text_email = "//input[@id=':r6:']"
    text_num_phone = "//input[@id=':r9:']"
    text_password1 = "//input[@id=':ra:']"
    text_password2 = "//input[@id=':rb:']"
    text_checkbox_newswetter = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[1]"
    text_checkbox = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[2]"
    text_button_create_user = '//button[contains(.,"יצירת חשבון")]//..//..//div[@class="MuiStack-root css-ax63s"]'

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.iframe_calendar, state="visible")

    def shoose_sign_up(self):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_choose_create_user).click()

    def click_checkbox_with_newsletter(self):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_checkbox_newswetter).click()
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_checkbox).click()

    def click_button_create_user(self):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_button_create_user).click()

    def take_token_online(self):
        time.sleep(8)
        token = self.pw_page.context.storage_state(path="state.json")
        user_token = token['origins'][0]['localStorage'][3]['value']
        return user_token

    def click_my_book(self):
        self.pw_page.click(self.img_user)

    def click_icon_user(self):
        self.pw_page.click(self.img_user)

    def click_connect_user(self):
        self.pw_page.click(self.text_connect_user)
        self.pw_page.wait_for_selector(self.frame, state="visible")
       # self.pw_page.frame_locator(self.frame).locator("//button[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-1r09c7j']").click()

    def click_connect_user_up(self):
        self.pw_page.click(self.text_connect_user)
        #self.pw_page.wait_for_selector(self.frame, state="visible")
        self.pw_page.frame_locator(self.frame_connect).locator("//button[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-1r09c7j']").click()

    def click_create_account(self):
        #time.sleep(60)
        self.pw_page.click("//u[text()='למידע נוסף']")
        self.pw_page.go_back()
        #self.pw_page.click(self.text_connect_user)
        # self.pw_page.wait_for_selector(self.frame, state="visible")
        self.pw_page.frame_locator(self.frame).locator("//button[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-1r09c7j']").click()


    def insert_user_details(self, firt_name, last_name, emailEx,num_phone, password):
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_first_name).fill(firt_name)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_last_name).fill(last_name)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_email).fill(emailEx)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_num_phone).fill(num_phone)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_password1).fill(password)
        self.pw_page.frame_locator(self.iframe_calendar).locator(self.text_password2).fill(password)