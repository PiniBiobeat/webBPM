import pytest
from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.edit_page import EditPage
from logic.pages.preview_screen_tiles_page import PreviewScreen




list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg", "C:\\Users\\lupa\\Desktop\\london\\IMG_2577.jpg"]





class TestEditTiles(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_edit_tiles_and_save(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.upload_photo(list[0])

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        page.click_edit_page()

        page: EditPage = self.browser.create_page(EditPage)
        page.move_image()
        page.click_save()

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        expected_price = page.get_image()
        current_price = page.get_price()
        assert current_price.replace("42x", "").strip() == str(expected_price)

