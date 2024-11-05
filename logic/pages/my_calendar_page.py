from infra.page_base import PageBase
import time
class MyCalendarPage(PageBase):

    init_indication = "(//button[@type='button'])[1]"
    test_click_change_format = '//button[contains(.,"לשינוי הפורמט")]'
    text_add_to_basket = '//button[contains(.,"הוספה לסל")'

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.text_add_to_basket, state="visible")

    def click_add_calendar_to_basket(self):
        self.pw_page.click(self.text_add_to_basket)
        print("")
