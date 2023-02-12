import pytest
from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.googlePhotos_page import GooglePhotosPage
from logic.pages.Psifas_upload_photo_page import PsifasPhotosPage
from logic.pages.google_photos_popup import GooglePhotosPopUp
from logic.pages.preview_mosaic_page import PreviewMosaicScreen

list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = ["./shutterstock_711632317.jpg"]
text_user_name_instagram = "pinitesttiles"
text_password_instagram = "Pinimari2020!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"

originalPrice=39
defaultQuantity=1





class TestUploadMosaic(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_psifas_upload_photo_from_local_gallery(self):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_pesipas()

        page: PsifasPhotosPage = self.browser.create_page(PsifasPhotosPage)
        page.Psifas_upload_photos(psifsPhoto)
        # use API
        # url = f"https://tiles.lupa.co.il/api.aspx?method=get_mosaic_options&width=4898&height=3265"
        # response = requests.get(url).json()
        # a =  response["payload"][0]['Price']
        page: PreviewMosaicScreen = self.browser.create_page(PreviewMosaicScreen)
        text_psifas_size = page.get_psifas_size()
        assert text_psifas_size.replace(" ריבועים  | מידות 44.3 על  44.3 ס”מ" ,"").strip() == "2*2"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_psifas_upload_photos_from_google_photos(self ,originalPrice="39" ,defaultQuantity="1"):
        page: HomePage = self.browser.navigate(configuration['url1'], HomePage)
        page.choose_pesipas()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)

        page: GooglePhotosPopUp = self.browser.create_popup(page.open_google_photos(), GooglePhotosPopUp)
        page.login_google_photos(text_googleUserName, text_googlePassword)

        page: GooglePhotosPage = self.browser.create_page(GooglePhotosPage)
        # upload_photos_from_google --> can get number of photos to upload
        page.upload_photos_from_google()

        page: PreviewMosaicScreen = self.browser.create_page(PreviewMosaicScreen)
        text_psifas_size = page.get_psifas_size()
        assert text_psifas_size.replace(" ריבועים  | מידות 44.3 על  44.3 ס”מ", "").strip() == "2*2"