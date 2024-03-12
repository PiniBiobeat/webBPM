from infra.page_base import PageBase

class PersonalDates(PageBase):

    button_click_next = "(//button[@type='button'])[3]"
    choose_A5 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[1]"
    choose_A4 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[2]"
    choose_A3 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.button_click_next, state="visible")

    def click_next(self):
        self.pw_page.click(self.button_click_next)