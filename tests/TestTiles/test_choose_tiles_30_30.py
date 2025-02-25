import pytest
from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.preview_screen_tiles_page import PreviewScreen
from logic.pages.gallery_page import GalleryPage
from logic.pages.instagram_page import InstagramPage
from logic.pages.googlePhotos_page import GooglePhotosPage
from logic.pages.instagram_popup_page import InstagramPopUp
from logic.pages.google_photos_popup import GooglePhotosPopUp

list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = [".\\shutterstock_711632317.jpg"]
text_user_name_instagram = "pinitesttiles"
text_password_instagram = "Pinim2022!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"
num_images = 1
originalPrice=39
defaultQuantity=1

class TestUpload(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_upload_photo(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
        page.upload_photo(psifsPhoto)

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        expected_price = page.get_image()
        current_price = page.get_price()
        #assert current_price.replace("42x","").strip() == str(expected_price)
        assert num_images == expected_price
