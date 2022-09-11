import time

from infra.page_base import PageBase

class LoginPage(PageBase):

    text_user_login = "//input[@type='text']"
    test_pass_login = "//input[@type='password']"
    button_login = "//span[@class='lupa-btn-content']"
    google_button = "//button[@class='google_sign_in']"
    tiles_button = '(//span[@class="lupa-btn-content"])[1]'
    facebook_button = "//button[@class='facebook_sign_in']"
    get_text_err = "//div[@class='error']"
    menu_button = '//img[@class="burger_menu"]'
    button_out = '//div[@class="menu-item" and contains(., "יציאה מהחשבון")]'

    def __init__(self,page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.text_user_login,state="visible")

    def input_user_and_pass(self,text_user,text_pass):
        self.pw_page.fill(self.text_user_login,text_user)
        self.pw_page.fill(self.test_pass_login,text_pass)

    def click_login_button(self):
        self.pw_page.click(self.button_login)


    def take_token(self):
        time.sleep(5)
        token = self.pw_page.context.storage_state(path='state.json')
        #self.pw_page.wait_for_load_state(timeout=10000)
        user_token = token['origins'][0]['localStorage'][1]['value']
        return user_token

    def login_with_google(self):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.google_button)
        return popup_info.value

    def login_with_facebook(self):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.facebook_button)
        return popup_info.value

    def get_error(self):
        text_error = self.pw_page.text_content(self.get_text_err)
       # self.pw_page.close()
        return text_error

    def open_menu(self):
        self.pw_page.click(self.menu_button)

    def click_out(self):
        self.pw_page.click(self.button_out)









