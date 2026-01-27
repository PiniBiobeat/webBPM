from playwright.sync_api import expect
from infra.page_base import PageBase

class BPMLoginPage(PageBase):
    username = "input[type='text']"
    password = "input[type='password']"
    submit = "button[type='submit']"

    def login(self, username: str, password: str):
        expect(self.pw_page.locator(self.username)).to_be_visible(timeout=60000)
        self.pw_page.locator(self.username).fill(username)
        self.pw_page.locator(self.password).fill(password)
        self.pw_page.locator(self.submit).click()