from infra.page_base import PageBase
import time
import json
from playwright.sync_api import expect



class EditOnlinePage(PageBase):


    text_button_delete = "(//a[@class='delete'])[2]"
    text_yes_delete = "//a[@class='cancel' and contains(text(),'כן, למחוק')]"


    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.text_button_delete, state="visible")

    def click_delete_button(self):
        self.pw_page.click(self.text_button_delete)

    def click_yes_delete(self):
        self.pw_page.click(self.text_yes_delete)