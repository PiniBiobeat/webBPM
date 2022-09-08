import pytest
from tests.Test_Online.test_base_online import TestBaseOnline
from infra.config.config_provider import configuration
from logic.pages.online_name_book_page import NameBook
from logic.pages.upload_photos_online_page import UploadPhotosOnline
from logic.pages.edit_screen_online_page import EditOnlinePage


list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg"]

name_book = "Book Automation"
num_images = 2
num_images1 = 27

class TestEditImageOnline(TestBaseOnline):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_edit_image_and_check_result(self):
        page: NameBook = self.browser_online.navigate(configuration['online_url'], NameBook)
        page.insert_name_book(name_book)
        page.click_next()
        page.approval_regulations()
        page.click_approval()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        page.click_upload_Photos_for_text()
        page.click_choose_one_image()
        page.click_add_text()

        page: EditOnlinePage  = self.browser_online.create_page(EditOnlinePage)
        page.click_delete_button()
        page.click_yes_delete()

        page: UploadPhotosOnline = self.browser_online.create_page(UploadPhotosOnline)
        sum = page.sum_all_images()
        assert sum == num_images