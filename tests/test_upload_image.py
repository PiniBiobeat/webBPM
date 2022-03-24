import time

import pytest
import requests

from logic.pages.home_page import HomePage
from logic.pages.upload_photo_page import UploadPhotoPage
from tests.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.preview_screen_tiles_page import PreviewScreen
from logic.pages.gallery_page import GalleryPage
from logic.pages.instagram_page import InstagramPage
from logic.pages.googlePhotos_page import GooglePhotosPage
from logic.pages.Psifas_upload_photo_page import PsifasPhotosPage
from logic.pages.instagram_popup_page import InstagramPopUp
from logic.pages.google_photos_popup import GooglePhotosPopUp

list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg"]
text_user_name_instagram = "pinitesttiles"
text_password_instagram = "Pinimari2020!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"

originalPrice=39
defaultQuantity=1

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

        page: InstagramPopUp = self.browser.create_popup(page.open_instagram(),InstagramPopUp)
        page.login_instagram(text_user_name_instagram,text_password_instagram)

        page: InstagramPage = self.browser.create_page(InstagramPage)
        page.upload_photos_from_instagram()

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        expected_price = page.get_image()
        current_price = page.get_price()
        assert current_price.replace("39x", "").strip() == str(expected_price)

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_upload_photos_from_GooglePhotos(self,originalPrice="39",defaultQuantity="1"):
        page: HomePage = self.browser.navigate(configuration['url1'],HomePage)
        page.choose_tiles()

        page: UploadPhotoPage = self.browser.create_page(UploadPhotoPage)

        page: GooglePhotosPopUp = self.browser.create_popup(page.open_google_photos(),GooglePhotosPopUp)
        page.login_google_photos(text_googleUserName, text_googlePassword)

        page: GooglePhotosPage = self.browser.create_page(GooglePhotosPage)
        #upload_photos_from_google --> can get number of photos to upload
        page.upload_photos_from_google(defaultQuantity)

        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        expected_price = page.get_image()
        current_price = page.get_price()
        assert current_price.replace(f"{originalPrice}x", "").strip() == str(expected_price)

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
        page: PreviewScreen = self.browser.create_page(PreviewScreen)
        text_psifas_size = page.get_psifas_size()
        assert text_psifas_size.replace(" ריבועים  | מידות 44.3 על  44.3 ס”מ","").strip() == "2*2"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_SalePrices(self):
        SalePrice=29
        MinQuantity=10
        #אם רוצים להמשיך צריל לשנות קצת את הלוגיקה של כל שאר הפונקציות
        TestUpload.test_upload_photos_from_GooglePhotos(self, SalePrice, MinQuantity)



    @pytest.mark.tcid3
    def test_upload2(self):
        print("2222222222222222222")

    @pytest.mark.tcid4
    def test_upload3(self):
        print("333333333333333333")

    @pytest.mark.tcid5
    def test_upload3(self):
        print("4444444444444444444")






