from infra.page_base import PageBase
import time

class GooglePhotosPopUp(PageBase):

    google_fill_email_button = "//input[@type='email']"
    google_user_name_button = "//span[text()='הבא']"
    google_fill_password_button = "//input[@type='password']"
    google_fill_allow_button = "//div[@id='passwordNext']"
    title_button = "//h4[@class='intro-title' and contains(.,'לופה בריבוע')]"
    tiles_button = '(//span[@class="lupa-btn-content"])[1]'


    def __init__(self, page):
        super().__init__(page)

    def login_google_photos(self,text_user_name,text_password):

        self.pw_page.wait_for_load_state()
        self.pw_page.fill(self.google_fill_email_button, text_user_name)
        self.pw_page.click(self.google_user_name_button)
        self.pw_page.fill(self.google_fill_password_button, text_password)
        self.pw_page.click(self.google_fill_allow_button)


    def take_token(self):
        time.sleep(7)
        #self.pw_page.wait_for_selector(self.tiles_button, state="attached")
        token = self.pw_page.context.storage_state(path="['origins'][0]['localStorage'][5]['value']")
        user_token = token['origins'][0]['localStorage'][5]['value']
        return user_token


