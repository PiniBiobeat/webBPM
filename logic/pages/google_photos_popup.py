from infra.page_base import PageBase


class GooglePhotosPopUp(PageBase):

    google_fill_email_button = "//input[@type='email']"
    google_user_name_button = "//span[text()='הבא']"
    google_fill_password_button = "//input[@type='password']"
    google_fill_allow_button = "//div[@id='passwordNext']"


    def __init__(self, page):
        super().__init__(page)

    def login_google_photos(self,text_user_name,text_password):

        self.pw_page.wait_for_load_state()
        self.pw_page.fill(self.google_fill_email_button, text_user_name)
        self.pw_page.click(self.google_user_name_button)
        self.pw_page.fill(self.google_fill_password_button, text_password)
        self.pw_page.click(self.google_fill_allow_button)

