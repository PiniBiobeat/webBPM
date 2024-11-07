from infra.page_base import PageBase
import time
class MyCalendarPage(PageBase):

    init_indication = "(//button[@type='button'])[1]"
    test_click_change_format = '//button[contains(.,"לשינוי הפורמט")]'
    text_add_to_basketA3 = '//div[@class="font_md_bold MuiBox-root css-0" and contains(.,"לוח A3")]//..//..//..//..//button[contains(.,"הוספה לסל")]'
    text_add_to_basketA4 = '//div[@class="font_md_bold MuiBox-root css-0" and contains(.,"לוח A4")]//..//..//..//..//button[contains(.,"הוספה לסל")]'
    text_add_to_basketA5 = '//div[@class="font_md_bold MuiBox-root css-0" and contains(.,"לוח A5")]//..//..//..//..//button[contains(.,"הוספה לסל")]'
    text_checkbox = "//input[@class='PrivateSwitchBase-input muirtl-1m9pwf3']"
    text_add = '//button[contains(.,"בהחלט")]'



    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.text_add_to_basketA3, state="visible")

    def click_add_calendar_to_basket(self):
        self.pw_page.click(self.text_add_to_basketA3)
        self.pw_page.click(self.text_checkbox)
        self.pw_page.click(self.text_add)
        print("")
