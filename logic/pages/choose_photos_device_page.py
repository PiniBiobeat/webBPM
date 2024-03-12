from infra.page_base import PageBase

class ChoosePhotosDeviceCalendar(PageBase):

    button_click_next = "(//button[@type='button'])[3]"
    choose_A5 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[1]"
    choose_A4 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[2]"
    choose_A3 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    text_button_upload = "(//div[@class='font_xl color_gray position_flex_row_center mesures_full_height MuiBox-root css-0'])[1]"
    text_next_button = "//button[contains(.,'אישור')]"
    path_images = ["C:/Users/lupa/Desktop/london/IMG_2549.jpg"]

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.text_next_button, state="visible")

    def click_next_after_choose_photos(self):
        self.pw_page.click(self.text_next_button)
