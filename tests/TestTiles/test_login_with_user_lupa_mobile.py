import json

import pytest
from logic.pages.home_page import HomePage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.choose_login_or_sign_up_page import ChooseLoginOrSignUpPage
from logic.pages.login_page import LoginPage

text_login_user = 'pinim@lupa.co.il'
text_login_pass = 'Pinimari1!'
text_user_not_valid = "NOT"
text_error = "lupa@lup.co.il דוגמא לכתובת מייל נכונה"



class TestLogin(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_login_with_user_invalid(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_tiles()
        page.open_menu()
        page.open_screen_login_from_menu()

        page: ChooseLoginOrSignUpPage = self.browser.create_page(ChooseLoginOrSignUpPage)
        page.click_login_button()

        page: LoginPage = self.browser.create_page(LoginPage)
        page.input_user_and_pass(text_user_not_valid, text_login_pass)
        page.click_login_button()
        get_err_dialogue = page.get_error()
        assert get_err_dialogue  == text_error

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_login_local(self) -> None:
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_tiles()
        page.open_menu()
        page.open_screen_login_from_menu()

        page: ChooseLoginOrSignUpPage = self.browser.create_page(ChooseLoginOrSignUpPage)
        page.click_login_button()

        page: LoginPage = self.browser.create_page(LoginPage)
        page.input_user_and_pass(text_login_user,text_login_pass)
        page.click_login_button()
        token_after_login  = page.take_token()
        #a        = json.loads(token_after_login)
        assert token_after_login is not None










