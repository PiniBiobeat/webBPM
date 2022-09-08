import pytest
from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.googlePhotos_page import GooglePhotosPage
from logic.pages.google_photos_popup import GooglePhotosPopUp
from logic.pages.preview_mosaic_page import PreviewMosaicScreen

list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg"]
text_user_name_instagram = "pinitesttiles"
text_password_instagram = "Pinimari2020!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"

class TestMosaicDimensions(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_upload_image_3631_width_3026_height_make_sure_respons_2X2(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_pesipas()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)

        page: GooglePhotosPopUp = self.browser.create_popup(page.open_google_photos(), GooglePhotosPopUp)
        page.login_google_photos(text_googleUserName, text_googlePassword)

        page: GooglePhotosPage = self.browser.create_page(GooglePhotosPage)
        page.upload_image_for_mosaic()

        page: PreviewMosaicScreen = self.browser.create_page(PreviewMosaicScreen)
        all_size_for_image = page.get_psifas_size_1()
        assert all_size_for_image == 12

    # @pytest.mark.smoke
    # @pytest.mark.usefixtures("before_after_test")
    # def test_edit_mosaic(self):
    #     page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
    #     page.choose_pesipas()
    #
    #     page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)
    #
    #     page: GooglePhotosPopUp = self.browser.create_popup(page.open_google_photos(), GooglePhotosPopUp)
    #     page.login_google_photos(text_googleUserName, text_googlePassword)
    #
    #     page: GooglePhotosPage = self.browser.create_page(GooglePhotosPage)
    #     page.upload_image_for_mosaic()
    #
    #     page: PreviewMosaicScreen = self.browser.create_page(PreviewMosaicScreen)
    #     page.move_the_image()