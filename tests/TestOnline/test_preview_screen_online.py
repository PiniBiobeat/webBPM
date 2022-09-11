from playwright.sync_api import  expect
import pytest
from tests.TestOnline.test_base_online import  TestBaseOnline
from infra.config.config_provider import configuration
from logic.pages.online_name_book_page import NameBook
from logic.pages.upload_photos_online_page import UploadPhotosOnline
from logic.pages.edit_screen_online_page import EditOnlinePage


list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg"]

name_book = "Book Automation"
num_images = 1
num_images1 = 27

class TestPreviewScreen(TestBaseOnline):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_online_delete_from_preview(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        page.click_upload_photos_to_check_low_quality()
        page.click_choose_one_image()
        page.click_on_edit_button()

        page: EditOnlinePage  = self.browser_online.create_page(EditOnlinePage)
        page.click_delete_button()
        page.click_yes_delete()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        sum = page.sum_all_images()
        assert sum == num_images

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_choose_image_for_cover(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        page.click_upload_photos_to_check_low_quality()
        page.click_choose_one_image()
        page.click_on_set_cover_image()
        text_button_locator_next_disabled = page.get_locator_image()
        expect(text_button_locator_next_disabled).to_contain_text(" תמונת כריכה ")

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_photos_from_local_to_preview(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        page.click_upload_photos_to_check_low_quality()
        page.click_add_images()
        page.click_add_images_from_local()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        sum = page.sum_all_images()
        assert sum == num_images1

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_text_to_photos(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        page.click_upload_Photos_for_text()
        page.click_choose_one_image()
        page.click_add_text()

        page: EditOnlinePage = self.browser_online.create_page(EditOnlinePage)
        page.input_text()
        page.click_save()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        check_text_from_image = page.get_text_from_image()
        assert check_text_from_image == " text_image "


