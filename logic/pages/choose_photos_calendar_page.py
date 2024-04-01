from infra.page_base import PageBase

class ChoosePhotosCalendar(PageBase):

    button_click_next = "(//button[@type='button'])[3]"
    choose_A5 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[1]"
    choose_A4 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[2]"
    choose_A3 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    text_button_upload = "//input[@id='filePicker']"
    text_link_add_photos_after = "//a[@variant='contained']"



    def __init__(self, page):
        super().__init__(page)


    def add_photos_from_local(self, path):
        self.pw_page.set_input_files(self.text_button_upload, path)

    def click_link_add_images_after(self):
        self.pw_page.click(self.text_link_add_photos_after)

    def do_reload(self):
        self.pw_page.reload()