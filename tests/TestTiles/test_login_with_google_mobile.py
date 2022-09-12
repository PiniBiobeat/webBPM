import pytest
from logic.pages.home_page import HomePage
from tests.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.google_photos_popup import GooglePhotosPopUp
from logic.pages.choose_login_or_sign_up_page import ChooseLoginOrSignUpPage
from logic.pages.login_page import LoginPage

text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"
text_error = "lupa@lup.co.il דוגמא לכתובת מייל נכונה"

class TestLoginGoogle(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_login_google(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_tiles()
        page.open_menu()
        page.open_screen_login_from_menu()

        page: ChooseLoginOrSignUpPage = self.browser.create_page(ChooseLoginOrSignUpPage)
        page.click_login_button()

        page: LoginPage = self.browser.create_page(LoginPage)

        page: GooglePhotosPopUp = self.browser.create_popup(page.login_with_google(), GooglePhotosPopUp)
        page.login_google_photos(text_googleUserName, text_googlePassword)

        page: LoginPage = self.browser.create_page(LoginPage)
        token_after_login = page.take_token()
        assert token_after_login is not None