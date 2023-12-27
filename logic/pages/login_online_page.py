from infra.page_base import PageBase
import time
import json
from playwright.sync_api import expect



class LogInOnline(PageBase):

    text_user_login =  "(//input[@class='MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd css-mnn31'])[1]"
    test_pass_login = "(//input[@class='MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd css-mnn31'])[2]"
    frame = "//iframe[@frameborder='0']"
    text_login_button = "//button[@data-testid='btn-login']"
    text_my_books = "//img[@src='/assets/img/my_books.svg']"


    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.text_my_books, state="visible")


    def insert_user_and_pass(self, text_user, text_pass):
        self.pw_page.frame_locator(self.frame).locator(self.text_user_login).fill(text_user)
        self.pw_page.frame_locator(self.frame).locator(self.test_pass_login).fill(text_pass)


    def click_login_button(self):
        self.pw_page.frame_locator(self.frame).locator(self.text_login_button).click()

    def take_token(self):
        time.sleep(5)
        token = self.pw_page.context.storage_state(path='state.json')
        # self.pw_page.wait_for_load_state(timeout=10000)
        user_token = token['origins'][0]['localStorage'][3]['value']
        return user_token