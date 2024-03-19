from infra.page_base import PageBase
import time
class ChooseFormatCalendarPage(PageBase):

    init_indication = "(//button[@type='button'])[1]"
    A5 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[1]"
    A4 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[2]"
    A3 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.init_indication, state="visible")

    def getSelectorElement(self, format):
        if format == 92:
            time.sleep(5)
            self.pw_page.wait_for_selector("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=92']", state="visible")
            self.pw_page.click("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=92']")

        elif format == 240:
            time.sleep(5)
            self.pw_page.wait_for_selector("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=240']",state="visible")
            self.pw_page.click("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=240']")
        else:
            time.sleep(5)
            self.pw_page.wait_for_selector("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=260']",state="visible")
            self.pw_page.click("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=260']")

    def click_choose_A5(self,a):
        self.pw_page.click(f"(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[{a}]")

    def click_choose_A4(self,b):
        self.pw_page.click(f"(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[{b+1}]")

    def click_choose_A3(self,b):
        self.pw_page.click(f"(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[{b}]")

    def open_screen_login_from_menu(self):
        self.pw_page.click(self.text_open_menu)