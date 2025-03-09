import json
from logic.pages.upload_photo_page import UploadPhotoPage
import pytest
from logic.pages.home_page import HomePage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.choose_login_or_sign_up_page import ChooseLoginOrSignUpPage
from logic.pages.login_page import LoginPage
from logic.pages.gallery_page import GalleryPage
from urllib.parse import urlparse, urlunparse
psifsPhoto = [".\\shutterstock_711632317.jpg"]
text_login_user = 'pinim@lupa.co.il'
text_login_pass = 'Pinimari!1'
text_user_not_valid = "NOT"
text_error = "lupa@lup.co.il דוגמא לכתובת מייל נכונה"


class TestUrlPayment(TestBase):



    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_url_payment(self) -> None:
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_tiles()
        page.open_menu()
        page.open_screen_login_from_menu()

        page: ChooseLoginOrSignUpPage = self.browser.create_page(ChooseLoginOrSignUpPage)
        page.click_login_button()

        page: LoginPage = self.browser.create_page(LoginPage)
        page.input_user_and_pass(text_login_user,text_login_pass)
        page.click_login_button()

        page: HomePage = self.browser.create_page(HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.upload_photo_gallery()

        page: GalleryPage = self.browser.create_page(GalleryPage)
        # page.select_group_images()
        # page.select_image()
        page.click_button_next()
        page.click_button_next()

        self.browser.page.wait_for_selector("text=בואו נמשיך", state="visible")
        current_url = self.browser.page.url
        parsed_url = urlparse(current_url)
        url_without_params = urlunparse(parsed_url._replace(query=''))
        expected_url = 'https://paymentsv4-ui.lupa.co.il/basketItems'
        assert url_without_params == expected_url, f"Expected URL: {expected_url}, Actual URL: {url_without_params}"
