from infra.page_base import PageBase
import time
import json
from playwright.sync_api import expect



class ChooseFormatCoverPage(PageBase):

    text_choose_format =  'img[alt="ריבועי גדול"]'
    text_choose_cover = 'img[alt="כריכה קשה"]'

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.text_choose_format, state="visible")


    def choose_format(self):
        self.pw_page.click(self.text_choose_format)

    def choose_cover(self):
        self.pw_page.click(self.text_choose_cover)