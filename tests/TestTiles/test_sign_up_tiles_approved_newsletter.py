import os
import time
from logic.pages.home_page import HomePage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.sign_up_page import SignUpPage
from infra.generic_helpers import generate_random_email_and_password
from infra.generic_helpers import sql_get_status_newsletter
from infra.generic_helpers import sql_get_status_master_id
import pytest


firt_name = "פיני"
last_name = "mari"
rand_email = generate_random_email_and_password()
email =  rand_email["email"]
password = rand_email["password"]
num_and_pass =  password + "1"
email1 = 'pinim@lupa.co.il'

firt_name1 = "פיני1"
last_name1 = "mari1"
email2 = "pinilupa.co.il"
pass1 = "pinimari"
pass_not_same = "pinim123"




class TestSignUpApproved(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_User_approved_newsletter(self):

        page: HomePage = self.browser.navigate(configuration['url_tiles_'+os.getenv('env')],HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details(firt_name,last_name,email,num_and_pass)
        page.approval_regulations()
        page.click_checkbox()
        page.click_next()
        page.Sign_me_up_without_mailing()
        page.click_next()
        token_after_login = page.take_token()
        newsletter = sql_get_status_newsletter(email)
        master_id = sql_get_status_master_id(email)
        assert token_after_login is not None
        assert  newsletter == 1
        assert master_id == 'True'