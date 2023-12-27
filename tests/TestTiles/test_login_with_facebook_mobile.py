import pytest
from logic.pages.home_page import HomePage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.choose_login_or_sign_up_page import ChooseLoginOrSignUpPage
from logic.pages.login_page import LoginPage
from logic.pages.facebook_popup import FacebookPopup

text_facebook_user = "couponsaoutomat@gmail.com"
text_facebook_pass = "Pinim2022!"


# class TestLoginFacebook(TestBase):
#
#     @pytest.mark.smoke
#     @pytest.mark.usefixtures("before_after_test")
#     def test_login_facebook(self):
#         page: HomePage = self.browser.navigate(configuration['url1'],HomePage)
#         page.choose_tiles()
#         page.open_menu()
#         page.open_screen_login_from_menu()
#
#         page: ChooseLoginOrSignUpPage = self.browser.create_page(ChooseLoginOrSignUpPage)
#         page.click_login_button()
#
#         page: LoginPage = self.browser.create_page(LoginPage)
#
#         page: FacebookPopup = self.browser.create_popup(page.login_with_facebook(), FacebookPopup)
#         page.login_facebook(text_facebook_user, text_facebook_pass)
#
#         page: LoginPage = self.browser.create_page(LoginPage)
#         token_after_login = page.take_token()
#         assert token_after_login is not None























