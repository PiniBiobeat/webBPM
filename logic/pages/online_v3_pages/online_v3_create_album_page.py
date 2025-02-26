from infra.page_base import PageBase
import time
import json


class CreateAlbumsV3(PageBase):

    init_indication = "//div[@class=' large intro-box']/h4[@class='intro-title']"
    locator_book_name = "//input[@id='mat-input-1']"
    click_button_next = "//button[@data-testid='continue-button']"


    def __init__(self, page):
        super().__init__(page)
        #self.pw_page.wait_for_selector(self.locator_book_name, state="visible")

    def click_next(self):
        self.pw_page.click(self.click_button_next)