

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
    text_plus_to_add_images = "//button[@type='button' and img[@class='mesures_icon_lg MuiBox-root css-0']]"
    text_plus_to_add_image = "//img[@class='mesures_icon_lg MuiBox-root css-0']"
    text_choose_month = "//div[@id='month_number_0']"
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

    def click_plus_to_add_images(self):

        if self.pw_page.wait_for_selector(self.text_plus_to_add_images, state="visible", timeout=0):
            self.pw_page.click(self.text_plus_to_add_images)
        else:
            self.pw_page.wait_for_url("/preview", timeout=60000)

    def do_reload(self):
        self.pw_page.reload()


    def get_locator_plus(self):
        return self.pw_page.locator(self.text_plus_to_add_image).count()

    def click_checkbox_accsept(self):
        self.pw_page.click(self.text_checkbox_ok)

    def click_ok_accsept(self):
        self.pw_page.click(self.text_next_after_checkout)

    def click_choose_month_(self, month):
        self.pw_page.click(f"(//div[@name='month_name'])[{month}]")


        # list_element  = self.pw_page.wait_for_selector(self.text_button_edit_page, state="visible")
        # list_items = list_element.select_option(self.text_select_change)
        # for item in list_items:
        #     item.click()


