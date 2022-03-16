from infra.page_base import PageBase


class UploadPhotoPage(PageBase):

    input_photo = "//input[@id= 'f']"
    title_button = "//span[@id= 'header_title']"
    gallery_button = "//img[@src='/static/media/icon_gallery_old.e4c596ba.svg']"
    instagram_button = "//img[@src='/static/media/icon_instagram.ae47004e.svg']"
    user_name = "//span[@class='_9nyy2']"
    user_password = "//input[@aria-label='Password']"
    login_button = "//button[@type='submit']"
    button_login_save_1 = "//button[@type='button' and contains(., 'Save Info')]"
    button_login_save_2 = "//button[@class='sqdOP  L3NKy   y3zKF   cB_4K  ' and contains(., 'Allow')]"

    googlePhotos_button = "//img[@src='/static/media/icon_google_photos.776cf4ac.svg']"
    googleFillEmail_button = "//input[@type='email']"
    googleUserName_button = "//span[text()='הבא']"
    googleFillPassword_button = "//input[@type='password']"
    googleFillAllow_button = "//div[@id='passwordNext']"

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.title_button, state="visible")

    def upload_photo(self, path):
        self.pw_page.set_input_files(self.input_photo, path)

    def upload_photo_gallery(self):
        self.pw_page.click(self.gallery_button)

    def open_instagram_and_login(self,text_user_name,text_password):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.instagram_button)
        popup = popup_info.value
        popup.wait_for_load_state()
        popup.fill(self.user_name,text_user_name)
        popup.fill(self.user_password,text_password)
        popup.click(self.login_button)
        popup.click(self.button_login_save_1)
        popup.click(self.button_login_save_2)
#    def open_googlePhotos_and_login(self,text_user_name,text_password):

    def open_googlePhotos_and_login(self, text_user_name,text_password):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.googlePhotos_button)
        popup = popup_info.value
        popup.wait_for_load_state()
        popup.fill(self.googleFillEmail_button,text_user_name)
        popup.click(self.googleUserName_button)
        popup.fill(self.googleFillPassword_button,text_password)
        popup.click(self.googleUserName_button)






