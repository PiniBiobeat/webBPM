from infra.page_base import PageBase

class SettingsCalendarPage(PageBase):

    init_indication = "(//button[@type='button'])[1]"
    choose_A5 = "//div[@class='position_direction_rtl MuiBox-root css-ktwy7h']"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    text_calendar_name = "//input[@id='filled-basic']"
    text_click_next = "//button[@type='button' and contains(.,'הבא')]"

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.init_indication, state="visible")

    def click_choose_A5(self):
        self.pw_page.click(self.choose_A5)

    def insert_name_calendar(self,calendar_name):
        self.pw_page.locator(self.text_calendar_name).fill(calendar_name)

    def click_button_next(self):
        self.pw_page.click(self.text_click_next)

