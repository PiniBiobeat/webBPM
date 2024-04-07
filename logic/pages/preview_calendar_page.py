from infra.page_base import PageBase
import time
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
    text_open_select_laout = '//*[@id="root"]/div/div[1]/div[1]/div[1]/div[1]/button'
    text_laout_1 = "(//li[@class='MuiListItem-root MuiListItem-gutters layout color_gray font_md mesures_padding_drawer_list position_flex_row muirtl-1tpp0wj'])[1]"
    text_laout_2 = "(//li[@class='MuiListItem-root MuiListItem-gutters layout color_gray font_md mesures_padding_drawer_list position_flex_row muirtl-1tpp0wj'])[2]"
    text_plus_to_add_images = "//button[@type='button' and img[@class='mesures_icon_md MuiBox-root css-0']]"
    text_plus_to_add_image = "//img[@class='mesures_icon_md MuiBox-root css-0']"
    text_choose_month = "//div[@id='month_number_0']"
    text_choose_month1 = "//div[@id='month_number_1']"
    text_choose_month2 = "//div[@id='month_number_2']"
    text_choose_month3 = "//div[@id='month_number_3']"
    text_choose_month4 = "//div[@id='month_number_4']"
    text_choose_month5 = "//div[@id='month_number_5']"
    text_choose_month6 = "//div[@id='month_number_6']"
    text_choose_month7 = "//div[@id='month_number_7']"
    text_choose_month8 = "//div[@id='month_number_8']"
    text_choose_month9 = "//div[@id='month_number_9']"
    text_choose_month10 = "//div[@id='month_number_10']"
    text_choose_month11 = "//div[@id='month_number_11']"
    text_choose_month12 = "//div[@id='month_number_12']"
    text_next_to_checkout = '//button[contains(.,"לקנייה")]'
    text_checkbox_ok = "//input[@class='PrivateSwitchBase-input muirtl-1m9pwf3']"
    text_next_after_checkout = '//button[contains(.,"בהחלט")]'
    def __init__(self, page):
        super().__init__(page)


    def click_edit_page(self):
        self.pw_page.click(self.text_button_edit_page)
        self.pw_page.click(self.text_select_change)

    def next_to_checkout(self):
        self.pw_page.click(self.text_next_to_checkout)
    def click_select_theme(self):
        self.pw_page.click(self.text_select_theme)

    def click_open_laout(self, number):
        self.pw_page.click(self.text_open_select_laout)
        self.pw_page.click(f"(//li[@class='MuiListItem-root MuiListItem-gutters layout color_gray font_md mesures_padding_drawer_list position_flex_row muirtl-1tpp0wj'])[{number}]")

    def click_open_laout_1(self):
        self.pw_page.click(self.text_open_select_laout)
        self.pw_page.click(self.text_laout_1)

    def click_open_laout_2(self):
        self.pw_page.click(self.text_open_select_laout)
        self.pw_page.click(self.text_laout_2)

    def click_plus_to_add_images(self):
        time.sleep(5)
        self.pw_page.click(self.text_plus_to_add_images)


    def do_reload(self):
        self.pw_page.reload()

    def click_choose_month1(self):
        self.pw_page.click(self.text_choose_month1)

    def click_choose_month(self):
        self.pw_page.click(self.text_choose_month)

    def click_choose_month2(self):
        self.pw_page.click(self.text_choose_month2)

    def click_choose_month3(self):
        self.pw_page.click(self.text_choose_month3)

    def click_choose_month4(self):
        self.pw_page.click(self.text_choose_month4)

    def click_choose_month5(self):
        self.pw_page.click(self.text_choose_month5)

    def click_choose_month6(self):
            self.pw_page.click(self.text_choose_month6)

    def click_choose_month7(self):
            self.pw_page.click(self.text_choose_month7)

    def click_choose_month8(self):
            self.pw_page.click(self.text_choose_month8)

    def click_choose_month9(self):
            self.pw_page.click(self.text_choose_month9)
    def click_choose_month10(self):
            self.pw_page.click(self.text_choose_month10)
    def click_choose_month11(self):
            self.pw_page.click(self.text_choose_month11)

    def click_choose_month12(self):
            self.pw_page.click(self.text_choose_month12)

    def get_locator_plus(self):
        return self.pw_page.locator(self.text_plus_to_add_image).count()

    def click_checkbox_accsept(self):
        self.pw_page.click(self.text_checkbox_ok)

    def click_ok_accsept(self):
        self.pw_page.click(self.text_next_after_checkout)

    def click_choose_month_(self, month):
        self.pw_page.click(f"//div[@id='month_number_{month}']")


        # list_element  = self.pw_page.wait_for_selector(self.text_button_edit_page, state="visible")
        # list_items = list_element.select_option(self.text_select_change)
        # for item in list_items:
        #     item.click()


