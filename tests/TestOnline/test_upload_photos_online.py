from playwright.sync_api import  expect
import pytest
from tests.Test_Online.test_base_online import TestBaseOnline
from infra.config.config_provider import configuration
from logic.pages.online_name_book_page import NameBook
from logic.pages.upload_photos_online_page import UploadPhotosOnline


list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg"]
text_user_name_instagram = "pinitesttiles"
text_password_instagram = "Pinimari2020!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"
Short_name = "B"
name_book = "Book Automation"
num_images = 25
text_low = ' איכות נמוכה '
text_unprintable_quality = ' איכות לא ניתנת להדפסה '

class TestUploadPhotos(TestBaseOnline):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_online_upload_from_local_num_of_images_uploaded_equal_num_images_in_preview(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        page.click_upload_photos()
        sum = page.sum_all_images()
        assert sum == num_images

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_online_upload_from_local_check_photo_with_low_quality(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        page.click_upload_photos_to_check_low_quality()
        image_with_text = page.get_text_low_quality()
        assert text_low == image_with_text

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_online_upload_from_local_check_photo_with_unprintable_quality(self):

        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        page.click_upload_photos_to_check_low_quality()
        image_with_text = page.get_unprintable_quality()
        assert text_unprintable_quality == image_with_text
        text_button_locator_next_disabled = page.get_locator_button()
        expect(text_button_locator_next_disabled).to_be_disabled()




