
from logic.pages.home_page import HomePage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.sign_up_page import SignUpPage
from infra.generic_helpers import generate_random_email_and_password
from infra.generic_helpers import sql_get_status_newsletter

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




class TestSignUp(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_User_approved_newsletter(self):

        page: HomePage = self.browser.navigate(configuration['url1'],HomePage)
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
        aa = sql_get_status_newsletter(email)
        assert token_after_login is not None
        assert  aa == 1

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_User_not_approved_newsletter(self):

        page: HomePage = self.browser.navigate(configuration['url1'],HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details(firt_name,last_name,email,num_and_pass)
        page.approval_regulations()

        page.click_next()
        page.click_checknox_not_newslatter()
        #page.Sign_me_up_without_mailing()
        page.click_next()
        token_after_login = page.take_token()
        aa = sql_get_status_newsletter(email)
        assert token_after_login is not None
        assert  aa == 0

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_email_exists(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details_exists(firt_name, last_name, email1, num_and_pass,None)
        page.approval_regulations()
        page.click_checkbox()
        page.click_next()
        page.Sign_me_up_without_mailing()
        page.click_next()
        token_after_login = page.get_message_when_user_exists_text()
        assert token_after_login == "למייל הזה כבר יש חשבון בלופה, להזכיר לך את הסיסמה?"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_f_name_number(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details_exists(firt_name1, last_name1, email1, num_and_pass,None)
        page.approval_regulations()
        page.click_checkbox()
        page.click_next()
        page.Sign_me_up_without_mailing()
        page.click_next()
        token_after_login = page.get_text_error_f_name_with_num()
        assert token_after_login == "שם פרטי לא יכול להכיל ספרות"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_l_name_number(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details_exists(firt_name1, last_name1, email1, num_and_pass,None)
        page.approval_regulations()
        page.click_checkbox()
        page.click_next()
        page.Sign_me_up_without_mailing()
        page.click_next()
        token_after_login1 = page.get_text_error_l_name_with_num()
        token_after_login2 = page.get_text_error_f_name_with_num()

        assert token_after_login1 == "רק לרובוט יש ספרות בשם"
        assert token_after_login2 == "שם פרטי לא יכול להכיל ספרות"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_email_not_valid(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details_exists(firt_name1, last_name1, email2, num_and_pass,None)
        page.approval_regulations()
        page.click_checkbox()
        page.click_next()
        page.Sign_me_up_without_mailing()
        page.click_next()
        token_after_login1 = page.get_text_error_email_with_num()

        assert token_after_login1 == "lupa@lup.co.il דוגמא לכתובת מייל נכונה"


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_password_without_num(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details_exists(firt_name1, last_name1, email2, pass1,None)
        page.approval_regulations()
        page.click_checkbox()
        page.click_next()
        page.Sign_me_up_without_mailing()
        page.click_next()
        token_after_login1 = page.get_text_error_password_without_num()

        assert token_after_login1 == "המינימום שלנו, הוא שילוב של 6 אותיות וספרות"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_password_not_same(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details_exists(firt_name, last_name, email1, num_and_pass,pass_not_same)
        page.approval_regulations()
        page.click_checkbox()
        page.click_next()
        page.Sign_me_up_without_mailing()
        page.click_next()
        token_after_login1 = page.get_text_error_same_password()

        assert token_after_login1 == "זה לא אותה הסיסמה שהקלדת מקודם"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_check_terms_of_use(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        token_after_login1 = page.click_terms_of_use()
        assert token_after_login1 == "https://www.lupa.co.il/license/"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_with_user_not_newsletter(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details_exists(firt_name, last_name, email1, num_and_pass,None)
        page.approval_regulations()
        page.click_next()
        token_after_login = page.get_text_error_newsletter()
        assert token_after_login == "רק באישור דואר פרסומי נוכל לפרגן בהטבת יום הולדת והטבות נוספות"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_sign_up_user_not_approved(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.open_screen_login_from_menu()
        page.shoose_sign_up()

        page: SignUpPage = self.browser.create_page(SignUpPage)
        page.input_user_details_exists(firt_name, last_name, email1, num_and_pass,None)
        page.click_checkbox()
        page.click_next()
        page.Sign_me_up_without_mailing()
        page.click_next()
        token_after_login = page.get_message_user_not_approved()
        assert token_after_login == "כדי להתקדם נשמח לקבל ממך אישור"












