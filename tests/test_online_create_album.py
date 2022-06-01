import pytest
from tests.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.online_name_book_page import NameBook



list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg"]
text_user_name_instagram = "pinitesttiles"
text_password_instagram = "Pinimari2020!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"
Short_name = "B"
name_book =  "Book Automation"





class TestCreateAlbum(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_online_click_next_without_name_book(self):
        page: NameBook = self.browser.navigate(configuration['online_url'], NameBook)
        page.click_next()
        text_err = page.get_err()
        assert text_err == " שם הספר הוא חובה "

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_online_click_next_with_one_letter(self):
        page: NameBook = self.browser.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(Short_name)
        page.click_next()
        text_err1 = page.get_err_short()
        assert text_err1 == " שם הספר קצר מידי "

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_online_insert_name_book_and_check_get_event_token(self):
        page: NameBook = self.browser.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()
        token_after_login = page.take_token()
        assert token_after_login is not None





