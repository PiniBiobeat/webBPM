from infra.page_base import PageBase

class EditPersonalDates(PageBase):

    button_click_next = "(//button[@type='button'])[3]"
    choose_A5 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[1]"
    choose_A4 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[2]"
    choose_A3 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    text_select_event_type = '//li[@name="יום הולדת"]'
    text_event_type = '(//div[@class="MuiFormControl-root  mesures_full_width position_margin_drop_down position_input_label muirtl-13sljp9"])[2]'
    text_birthday_selection =  '//li[@name="אמא"]'
    text_attribution_selection = '(//div[@class="MuiFormControl-root  mesures_full_width position_margin_drop_down position_input_label muirtl-13sljp9"])[1]'
    text_event_name = '//input[@id="filled-basic"]'
    text_save_button = "//button[@type='button' and contains(.,'שמירה')]"
    text_add_image = '(//div[@class="position_flex_row_start_center MuiBox-root muirtl-0"])[1]'
    text_add_image_from_local = "//input[@id='filePicker']"
    text_save_image = '//button[contains(.,"Done")]'
    text_popap_save = '//button[contains(.,"ככה התמונה תראה")]'
    text_checkbox = "//input[@class='PrivateSwitchBase-input muirtl-1m9pwf3']"
    text_checkbox_next = "//button[@type='button' and contains(.,'להמשך')]"


    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.text_event_type, state="visible")

    def select_event_eype(self):
        self.pw_page.click(self.text_event_type)
        self.pw_page.click(self.text_select_event_type)

    def select_attribution_selection(self):
        self.pw_page.click(self.text_attribution_selection)
        self.pw_page.click(self.text_birthday_selection)

    def input_name_event(self,a):
        self.pw_page.locator(self.text_event_name).fill(a)

    def click_save_event(self):
        self.pw_page.click(self.text_save_button)
        print("222")
    def click_save_image(self):
        self.pw_page.click(self.text_save_image)
        self.pw_page.click(self.text_popap_save)

    def click_save_image_in_storage(self):
        self.pw_page.click(self.text_save_image)


    def click_add_photos(self):
        self.pw_page.click(self.text_add_image)

    def add_photos_from_local(self, path):self.pw_page.set_input_files(self.text_add_image_from_local, path)

    def click_checkbox(self):
        self.pw_page.click(self.text_checkbox)

    def click_checkbox_next(self):
        self.pw_page.click(self.text_checkbox_next)

