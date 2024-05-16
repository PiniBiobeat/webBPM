from infra.page_base import PageBase

class UploadStorageImagesCalendar(PageBase):

    button_click_next = "(//button[@type='button'])[3]"
    choose_A5 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[1]"
    choose_A4 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[2]"
    choose_A3 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    text_button_upload = "//input[@id='filePicker']"
    text_link_add_photos_after = "//a[@variant='contained']"
    text_choose_first_image = "(//li[@class='MuiImageListItem-root css-p8pnwm'])[1]"
    text_ok_save = '//button[contains(.,"אישור")]'
    text_save_image = '//button[contains(.,"הבא")]'
    text_save_and_next = '//button[contains(.,"בהחלט")]'
    def __init__(self, page):
        super().__init__(page)


    def click_first_image(self):

             self.pw_page.click(self.text_choose_first_image)


    def click_save_image(self):
        self.pw_page.click(self.text_ok_save)

    def click_save_image_in_storage(self):
        self.pw_page.click(self.text_save_image)