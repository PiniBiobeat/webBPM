import time
from logic.pages.calendar_home_page import CalendarPage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.sign_up_page import SignUpPage
from logic.pages.login_calendar_page import LoginCalendarPage
from infra.generic_helpers import generate_random_email_and_password
from infra.generic_helpers import sql_get_status_newsletter
from infra.generic_helpers import sql_get_status_master_id
import pytest


firt_name = "פיני"
last_name = "mari"
rand_email = generate_random_email_and_password()
email =  rand_email["email"]
password = rand_email["password"] + "!"
num_and_pass =  password + "1"
email1 = 'pinim@lupa.co.il'

firt_name1 = "פיני1"
last_name1 = "mari1"
email2 = "pinilupa.co.il"
pass1 = "pinimari"
pass_not_same = "pinim123"
num_phone = '0537608055'




class TestSignUpCalendarApproved(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_User_approved_newsletter(self):

        page: CalendarPage = self.browser.navigate(configuration['calendar_url'],CalendarPage)
        page.open_menu()
        page.open_screen_login_from_menu()

        page: LoginCalendarPage = self.browser.create_page(LoginCalendarPage)
        page.shoose_sign_up()

        page.insert_user_details(firt_name,last_name,email,num_phone,num_and_pass)
        page.click_checkbox_with_newsletter()
        page.click_button_create_user()
        newsletter = sql_get_status_newsletter(email)
        master_id = sql_get_status_master_id(email)

        #assert newsletter == 1
        assert master_id == 'True'