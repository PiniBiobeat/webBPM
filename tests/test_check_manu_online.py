import pytest
from tests.test_base_online import TestBaseOnline
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



class TestCreateAlbum(TestBaseOnline):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_click_create_album_with_anonymous(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()
        page.click_on_manu()
        page.click_create_album()
        text_login = page.get_text_from_login()
        assert text_login == 'כניסה לחשבון לופה'
        #expect(page.pw_page.locator("text=כניסה לחשבון לופה")).to_be_visible()

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_click_open_my_book(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.click_on_manu()
        page.click_open_my_albums()
        text_login = page.get_text_from_login()
        assert text_login == 'כניסה לחשבון לופה'

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_click_open_lupa_site(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.click_on_manu()
        text_err = page.click_open_web_side()
        assert text_err == "https://www.lupa.co.il/"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_click_open_chat(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.click_on_manu()
        text_err = page.get_url_chat()
        assert text_err == "https://www.lupa.co.il/customer-service/"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_click_connect_to_account(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.click_on_manu()
        page.clock_login()
        text_login = page.get_text_from_login()
        assert text_login == 'כניסה לחשבון לופה'