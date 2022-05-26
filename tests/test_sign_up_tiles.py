
from logic.pages.home_page import HomePage
from tests.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.sign_up_page import SignUpPage
from infra.generic_helpers import generate_random_email_and_password
import pytest

firt_name = "פיני"
last_name = "mari"
rand_email = generate_random_email_and_password()
email =  rand_email["email"]
password = rand_email["password"]
num_and_pass =  password + "1"




class TestSignUp(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up(self):
        page: HomePage = self.browser.navigate(configuration['url1'],HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details(firt_name,last_name,email,num_and_pass)
        page.approval_regulations()
        page.click_checkbox()
        page.click_next()

        token_after_login = page.take_token()
        assert token_after_login is not None








