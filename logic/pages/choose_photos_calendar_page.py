from infra.page_base import PageBase
import time
class ChoosePhotosCalendar(PageBase):

    button_click_next = "(//button[@type='button'])[3]"
    choose_A5 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[1]"
    choose_A4 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[2]"
    choose_A3 = "(//div[@class='position_direction_rtl MuiBox-root css-ktwy7h'])[3]"
    text_open_menu = '//span[contains(.,"להתחברות לחשבון")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    text_button_upload = "//input[@id='filePicker']"
    text_link_add_photos_after = "//a[@variant='contained']"
    text_next_button = "//button[contains(.,'הבא')]"
    text_checkbox_approval_regulations = "//input[@type='checkbox']"
    text_click_next_after_checkbox = "//button[contains(.,'להמשך')]"

    def __init__(self, page):
        super().__init__(page)


    def add_photos_from_local(self, path):
        self.pw_page.set_input_files(self.text_button_upload, path)


        # link = self.pw_page.wait_for_selector('#link-textbox', state='visible').inner_text()
        # print(f'file link: {link}')

        # with page.expect_response(
        #         lambda response: response.url == \"https://example.com\" and response.status == 200) as response_info:
        # page.click(\"input\")
        # response = response_info.value
        # return response.ok


    def click_next_after_choose_photos(self):
        self.pw_page.click(self.text_next_button)

    def checkbox_approval_regulations(self):
        self.pw_page.click(self.text_checkbox_approval_regulations)

    def click_next_after_checkbox(self):
        self.pw_page.click(self.text_click_next_after_checkbox)


    def click_link_add_images_after(self):
        self.pw_page.click(self.text_link_add_photos_after)

    def do_reload(self):
        self.pw_page.reload()