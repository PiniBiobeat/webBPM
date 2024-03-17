from infra.page_base import PageBase

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
            self.pw_page.click(f"(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[{1}]")
        elif format == 240:
            self.pw_page.click(f"(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[{2}]")
        else:
            self.pw_page.click(f"(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[{3}]")

    def click_choose_A5(self,a):
        self.pw_page.click(f"(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[{a}]")

    def click_choose_A4(self,b):
        self.pw_page.click(f"(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[{b+1}]")

    def click_choose_A3(self,b):
        self.pw_page.click(f"(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[{b}]")

    def open_screen_login_from_menu(self):
        self.pw_page.click(self.text_open_menu)