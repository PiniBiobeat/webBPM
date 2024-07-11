from infra.page_base import PageBase
import time
class ChooseFormatCalendarPage(PageBase):

    init_indication = "(//button[@type='button'])[1]"
    A5 = "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 position_flex_row color_box_shadow_paper mesures_format_container cursor_pointer css-vuzb25'])[1]"
    A4 = "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 position_flex_row color_box_shadow_paper mesures_format_container cursor_pointer css-vuzb25'])[2]"
    A3 = "(//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 position_flex_row color_box_shadow_paper mesures_format_container cursor_pointer css-vuzb25'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.init_indication, state="visible")

    def getSelectorElement(self, format):
        if format == 92:
            time.sleep(2)
            # xpath_selector = f"//img[@src='https:////calendarv4-api.lupa.co.il//img.aspx?subject=format&size=medium&format={format}']"
            # print("xpath_selector", xpath_selector)
            xpath_selector = "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/img"
            self.pw_page.wait_for_selector(xpath_selector, state="visible")
            self.pw_page.click(xpath_selector)


        elif format == 240:
            time.sleep(2)
            self.pw_page.wait_for_selector("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=240']",state="visible")
            self.pw_page.click("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=240']")
        else:
            time.sleep(2)
            self.pw_page.wait_for_selector("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=260']",state="visible")
            self.pw_page.click("//img[@src='https:////calendarv4-api.lupa.co//img.aspx?subject=format&size=medium&format=260']")

    def click_choose_A5(self):
        self.pw_page.click(self.A5)

    def click_choose_A4(self):
        self.pw_page.click(self.A4)

    def click_choose_A3(self):
        self.pw_page.click(self.A3)

    def open_screen_login_from_menu(self):
        self.pw_page.click(self.text_open_menu)