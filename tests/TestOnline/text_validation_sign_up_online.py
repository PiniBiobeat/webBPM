import json
import pytest
from tests.TestOnline.test_base_online import TestBaseOnline
#from tests.Test_Online.test_base_online import TestBaseOnline
from infra.config.config_provider import configuration
from logic.pages.online_name_book_page import NameBook
from logic.pages.connect_create_user_page import ConnectCreateUserPage
from infra.generic_helpers import generate_random_email_and_password
from infra.generic_helpers import sql_get_status_newsletter
from infra.generic_helpers import sql_get_status_master_id
from logic.pages.google_photos_popup import GooglePhotosPopUp


firt_name = "פיני"
last_name = "mari"
rand_email = generate_random_email_and_password()
email =  'pinim@lupa.co.il'
password = rand_email["password"]
num_and_pass =  password + "1" + "!"
email1 = 'pinim@lupa.co.il'

firt_name1 = "פיני1"
last_name1 = "mari1"
email2 = "pinilupa.co.il"
pass1 = "pinimari"
pass_not_same = "pinim123"
num_phone = '0537608055'
name_num = '1231321'
title_popup = "לא חבל?"


class TestSignUpOnline(TestBaseOnline):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_email_exists(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details(firt_name, last_name, email, num_phone, num_and_pass)
        page.click_checkbox()
        page.click_button_create_user()
        token_after_login = page.get_message_when_user_exists_text()
        assert token_after_login == "זה מייל שיש לו כבר חשבון בלופה"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_f_name_number(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details(name_num, last_name, email, num_phone, num_and_pass)
        token_after_login = page.get_text_error_f_name_with_num()
        assert token_after_login == "רק לרובוטים יש ספרות בשם"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_l_name_number(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details(firt_name, name_num, email, num_phone, num_and_pass)
        token_after_login = page.get_text_error_l_name_with_num()
        assert token_after_login == "רק לרובוטים יש ספרות בשם"


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_email_not_valid(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details(firt_name, last_name, name_num, num_phone, num_and_pass)
        token_after_login1 = page.get_text_error_email_with_num()
        assert token_after_login1 == "hopa@lupa.co.il הנה דוגמה למבנה מייל תקין"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_phone_not_valid(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details(firt_name, last_name, email, name_num, num_and_pass)
        token_after_login1 = page.get_text_error_phone_with_num()
        assert token_after_login1 == "במספר טלפון תקין יש 10 ספרות"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_password_without_num(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details(firt_name, last_name, email, num_phone, last_name)
        token_after_login1 = page.get_text_error_password_with_num()

        assert token_after_login1 == '\n                מינימום 8 תווים, \n                אות גדולה ואות קטנה,\n                מספר וסימן מיוחד'

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_password_not_same(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details_pass(firt_name, last_name, email, num_phone, last_name)
        page.click_checkbox()
        page.click_button_create_user()
        token_after_login1 = page.get_text_error_password()
        assert token_after_login1 == 'זו לא אותה סיסמה שהקלדת קודם'

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_check_terms_of_use(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details(firt_name, last_name, email, num_phone, last_name)
        page.click_button_create_user()
        token_after_login1 = page.get_text_error_approval_regulations()
        assert token_after_login1 == 'כדי להתקדם נצטרך לקבל אישור לתקנון'

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_checkbox_newslatter(self):
        page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url'], ConnectCreateUserPage)
        page.click_icon_user()
        page.click_connect_user_up()
        page.insert_user_details(firt_name, last_name, email, num_phone, num_and_pass)
        page.click_open_popup()
        page.select_date_birth()
        page.click_checkbox()
        page.click_button_create_user()
        token_after_login1 = page.get_text_title_popup()

        assert title_popup == token_after_login1
















