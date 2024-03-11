from infra.page_base import PageBase

class ChooseFormatCalendarPage(PageBase):

    init_indication = "(//button[@type='button'])[1]"
    choose_A5 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[1]"
    choose_A4 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[2]"
    choose_A3 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.init_indication, state="visible")

    def click_choose_A5(self):
        self.pw_page.click(self.choose_A5)

    def click_choose_A4(self):
        self.pw_page.click(self.choose_A4)

    def click_choose_A3(self):
        self.pw_page.click(self.choose_A3)

    def open_screen_login_from_menu(self):
        self.pw_page.click(self.text_open_menu)