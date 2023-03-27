import time

import pytest
from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.preview_screen_tiles_page import PreviewScreen
from logic.pages.login_page import LoginPage
from logic.pages.choose_login_or_sign_up_page import ChooseLoginOrSignUpPage
from logic.pages.terms_pages import TermsPages


num_images = 1
login_to_lupa_account = "כניסה לחשבון לופה"
title_text_in_terms_page = "תקנון ומדיניות פרטיות"

class TestChechManuTiles(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_check_login_link(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        page.click_log_in()

        page: ChooseLoginOrSignUpPage = self.browser.create_page(ChooseLoginOrSignUpPage)
        text_login =  page.get_log_in_text()
        assert text_login == login_to_lupa_account

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_link_lupa_site(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        url_lupa_site = page.click_lupa_site()
        assert url_lupa_site == "https://www.lupa.co.il/"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_link_lupa_tariff(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.open_menu()
        url_lupa_tariff = page.click_lupa_tariff()
        assert url_lupa_tariff == "https://www.lupa.co.il/tariff/tiles/"

    # @pytest.mark.smoke
    # @pytest.mark.usefixtures("before_after_test")
    # def test_link_lupa_terms_of_use(self):
    #     page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
    #     page.open_menu()
    #     url_lupa_terms_of_use = page.click_terms_of_use()
    #     assert url_lupa_terms_of_use == "https://localhost:3000/terms-of-use"







