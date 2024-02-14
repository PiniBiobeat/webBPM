from infra.page_base import PageBase
import time

class GooglePhotosPopUp(PageBase):

    google_fill_email_button = "//input[@type='email']"
    google_user_name_button = "//span[text()='Next']"
    google_fill_password_button = "//input[@type='password']"
    google_fill_allow_button = "//div[@id='passwordNext']"
    title_button = "//h4[@class='intro-title' and contains(.,'לופה בריבוע')]"
    tiles_button = '(//span[@class="lupa-btn-content"])[1]'


    def __init__(self, page):
        super().__init__(page)

    def login_google_photos(self,text_user_name,text_password):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.wait_for_load_state()
            self.pw_page.fill(self.google_fill_email_button, text_user_name)
            self.pw_page.click(self.google_user_name_button)
            self.pw_page.fill(self.google_fill_password_button, text_password)
            self.pw_page.click(self.google_fill_allow_button)

        popup = popup_info.value

        popup.wait_for_load_state()







