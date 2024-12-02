import re
import pytest
import requests

from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.preview_screen_tiles_page import PreviewScreen
from logic.pages.login_page import LoginPage
from logic.pages.calender_payment_page import CalenderPaymentPage


# Global test data
text_login_user = "pinim4@lupa.co.il"
text_login_pass = "pinim1"


class TilesToPayment(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def add_tiles_to_payment(self):
        try:
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
            url = page.get_url()

            page: CalenderPaymentPage = self.browser.create_page(CalenderPaymentPage)
            page.delete_from_basket()

            expected_url_pattern = r"https://paymentsv4-ui\.lupa\.co\.il/.*"
            assert re.match(expected_url_pattern, url), f"Expected URL pattern: {expected_url_pattern}, but got {url}"

        except Exception as e:
            error_message = f"Test 'add_tiles_to_payment' failed: {str(e)}"
            self.send_slack_message(error_message)
            pytest.fail(error_message)

    def send_slack_message(self, message):
        webhook_url = "https://hooks.slack.com/services/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"  # Replace with your actual webhook URL

        payload = {
            "text": message,
            "channel": "#general"
        }

        try:
            response = requests.post(webhook_url, json=payload, headers={'Content-Type': 'application/json'})

            if response.status_code == 200:
                print("Message sent to Slack successfully.")
            else:
                print(f"Failed to send message to Slack: Status code {response.status_code}, response: {response.text}")

        except requests.RequestException as error:
            print("Error sending message to Slack:", error)
