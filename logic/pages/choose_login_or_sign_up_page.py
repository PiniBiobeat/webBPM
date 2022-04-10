from infra.page_base import PageBase



class ChooseLoginOrSignUpPage(PageBase):

    login_button = "//span[@class='lupa-btn-content' and contains(.,'כניסה')]"

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.login_button,state="visible")

    def click_login_button(self):
        self.pw_page.click(self.login_button)

