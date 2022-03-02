import pytest

from infra.teardown import tear_down

from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.preview_screen_tiles_page import PreviewScreen

list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]

class TestUpload(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_upload_photo(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_tiles()
        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.upload_photo(list)
        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        expected_price = "39x1 "
        current_price = page.get_price()
        self.browser.stop_trace()
        assert current_price == expected_price



