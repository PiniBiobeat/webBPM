from infra.page_base import PageBase
import time

class FacebookPopup(PageBase):

    title_button = "//h4[@class='intro-title' and contains(.,'לופה בריבוע')]"
    tiles_button = '(//span[@class="lupa-btn-content"])[1]'
    facebook_user = "//input[@id='m_login_email']"
    facebook_pass = "//input[@id='m_login_password']"
    button_login = "//button[@type='button']"



    def __init__(self, page):
        super().__init__(page)



    def login_facebook(self,text_user_name,text_password):

        self.pw_page.wait_for_load_state()
        self.pw_page.fill(self.facebook_user, text_user_name)
        self.pw_page.fill(self.facebook_pass, text_password)
        self.pw_page.click(self.button_login)

