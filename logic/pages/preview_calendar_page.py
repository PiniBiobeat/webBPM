from infra.page_base import PageBase

class PreviewCalendar(PageBase):

    button_click_next = "(//button[@type='button'])[3]"
    choose_A5 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[1]"
    choose_A4 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[2]"
    choose_A3 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    text_button_edit_page = "//*[@id='root']/div/div[1]/div[2]/div[2]/div[2]/button"
    text_select_change = "//*[@id='SpeedDial-action-3']"
    text_select_theme = "//*[@id='SpeedDial-action-4']"


    def __init__(self, page):
        super().__init__(page)


    def click_edit_page(self):
        self.pw_page.click(self.text_button_edit_page)
        self.pw_page.click(self.text_select_change)

    def click_select_theme(self):
        self.pw_page.click(self.text_select_theme)



        # list_element  = self.pw_page.wait_for_selector(self.text_button_edit_page, state="visible")
        # list_items = list_element.select_option(self.text_select_change)
        # for item in list_items:
        #     item.click()


