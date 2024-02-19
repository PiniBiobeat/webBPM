import json
import time

import pytest
from tests.TestOnline.test_base_online import TestBaseOnline
#from tests.Test_Online.test_base_online import TestBaseOnline
from infra.config.config_provider import configuration
from logic.pages.online_name_book_page import NameBook
from logic.pages.connect_create_user_page import ConnectCreateUserPage
from infra.generic_helpers import generate_random_email_and_password
from infra.generic_helpers import sql_get_status_newsletter
from infra.generic_helpers import sql_get_status_master_id

list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg"]
text_user_name_instagram = "pinitesttiles"
text_password_instagram = "Pinimari2020!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"
Short_name = "B"
name_book =  "Book Automation"
firt_name = "פיני"
last_name = "mari"
rand_email = generate_random_email_and_password()
email =  rand_email["email"]
password = rand_email["password"]
num_and_pass =  password + "1"+ "!"
email1 = 'pinim@lupa.co.il'
num_phone = '0537608055'
firt_name1 = "פיני1"
last_name1 = "mari1"
email2 = "pinilupa.co.il"
pass1 = "pinimari"
pass_not_same = "pinim123"



class TestSignUpOnline(TestBaseOnline):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_User_approved_newsletter(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details(firt_name,last_name,email,num_phone,num_and_pass)
        page.click_checkbox_with_newsletter()
        page.click_button_create_user()
        token_after_login = page.take_token_online()
        newsletter = sql_get_status_newsletter(email)
        master_id = sql_get_status_master_id(email)
        assert token_after_login is not None
        assert newsletter == 1
        assert master_id == 'True'