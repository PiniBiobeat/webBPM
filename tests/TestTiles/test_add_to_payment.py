import re

import pytest
from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.preview_screen_tiles_page import PreviewScreen
from logic.pages.login_page import LoginPage


list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = [".\\shutterstock_711632317.jpg"]
text_user_name_instagram = "pinitesttiles"
text_password_instagram = "Pinim2022!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"
text_login_user = "pinim4@lupa.co.il"
text_login_pass = "pinim1"
num_images = 1
originalPrice=39
defaultQuantity=1

class TestTilesToPayment(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_tiles_to_payment(self):

        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.upload_photo_gallery()

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        page.button_click_to_buy()
        page.click_with_same_user()

        page: LoginPage = self.browser.create_page(LoginPage)
        page.input_user_and_pass(text_login_user, text_login_pass)
        page.click_login_button()

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        page.button_click_to_payment()

        expected_url_pattern = r"https://paymentsv4-ui\.lupa\.co\.il/.*"


        url = page.get_url()


        # Assert that the actual URL matches the expected pattern
        assert re.match(expected_url_pattern, url), f"Expected URL pattern: {expected_url_pattern}, but got {url}"
