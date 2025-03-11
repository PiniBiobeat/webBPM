import os

import pytest
from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.preview_screen_tiles_page import PreviewScreen
from logic.pages.gallery_page import GalleryPage

num_images = 1

class TestDeleteTiles(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_delete_image_preview(self):
        page: HomePage = self.browser.navigate(configuration['url_tiles_'+os.getenv('env')], HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.upload_photo_gallery()

        page: GalleryPage = self.browser.create_page(GalleryPage)
        page.select_image_2()
        page.click_button_next()

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        page.delete_image()
        page.yes_delete()
        expected_price = page.get_image()
        current_price = page.get_price()
        #assert current_price.replace("42x", "").strip() == str(expected_price)
        assert num_images == expected_price
