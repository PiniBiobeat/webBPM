import pytest

from infra.teardown import tear_down

from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.preview_screen_tiles_page import PreviewScreen
from logic.pages.gallery_page import GalleryPage


list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
text_user_name = "pinitesttiles"
text_password = "Pinimari2020!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"

class TestUpload(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_upload_photo(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.upload_photo(list)

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        expected_price = page.get_image()
        current_price = page.get_price()
        assert current_price.replace("39x","").strip() == str(expected_price)

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_upload_photos_from_gallery(self):
        page: HomePage = self.browser.navigate(configuration['url1'],HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.upload_photo_gallery()

        page: GalleryPage = self.browser.create_page(GalleryPage)
        page.select_group_images()
        page.select_image()
        page.click_button_next()

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        expected_price = page.get_image()
        current_price = page.get_price()
        assert current_price.replace("39x", "").strip() == str(expected_price)

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_upload_photos_from_instagram(self):
        page: HomePage = self.browser.navigate(configuration['url1'],HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.login_to_instagram(text_user_name,text_password)
        page.upload_photos_from_instagram()

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        expected_price = page.get_image()
        current_price = page.get_price()
        assert current_price.replace("39x", "").strip() == str(expected_price)

     #   page.login_imstagram(text_user_name)
        print("ddddd")

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_upload_photos_from_GooglePhotos(self):
        page: HomePage = self.browser.navigate(configuration['url1'],HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.upload_photo_googlePhotos(text_googleUserName,text_googlePassword)

     #   page.login_imstagram(text_user_name)
        print("ddddd")
        print("pini")







    @pytest.mark.tcid3
    def test_upload2(self):
        print("2222222222222222222")

    @pytest.mark.tcid4
    def test_upload3(self):
        print("333333333333333333")

    @pytest.mark.tcid5
    def test_upload3(self):
        print("4444444444444444444")






