from infra.page_base import PageBase



class TermsPages(PageBase):

    login_button = "//span[@class='lupa-btn-content' and contains(.,'כניסה')]"
    get_text_title_log_in = '//h2[contains(.,"תקנון ומדיניות פרטיות")]'

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.login_button,state="visible")

    def click_login_button(self):
        self.pw_page.click(self.login_button)


    def get_title_terms(self):
        text_error = self.pw_page.text_content(self.get_text_title_log_in)
        return text_error