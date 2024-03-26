import time

from infra.page_base import PageBase

class ThemesCalendarPage(PageBase):

    init_indication = "(//button[@type='button'])[1]"
    choose_theme_diamonds = "//div[@class='font_md_bold position_flex_center MuiBox-root css-1uvj8k7' and contains(.,'יהלומים')]"
    text_next_theme = "(//div[@class='MuiStack-root css-1t62lt9' and contains(.,'אישור')])[10]"
    text_add_personal_date = '(//button[@type="button"])[2]'
    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.init_indication, state="visible")



    def click_shoose_themes(self):
        self.pw_page.click(self.choose_theme_diamonds)

    def click_next_on_theme(self):
        self.pw_page.click(self.text_next_theme)

    def take_token_calendar(self):
        time.sleep(8)
        token = self.pw_page.context.storage_state(path="state.json")
        user_token = token['origins'][0]['localStorage'][4]['value']
        return user_token

    def take_token_calendar_after_login(self):
        time.sleep(8)
        token = self.pw_page.context.storage_state(path="state.json")
        user_token = token['origins'][0]['localStorage'][6]['value']
        return user_token

    def click_add_personal_date(self):
        self.pw_page.click(self.text_add_personal_date)