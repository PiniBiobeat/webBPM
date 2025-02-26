import pytest
from tests.TestOnline.test_base_online import TestBaseOnline
from infra.config.config_provider import configuration
from logic.pages.online_v3_pages.online_v3_create_album_page import CreateAlbumsV3


list = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg","C:\\Users\\lupa\\Desktop\\london\\IMG_2668.jpg"]
psifsPhoto = ["C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg"]
text_user_name_instagram = "pinitesttiles"
text_password_instagram = "Pinimari2020!"
text_googleUserName="lupadevtest@gmail.com"
text_googlePassword="lupadevtest!128"
Short_name = "B"
name_book =  "Book Automation V3"


class TestCreateAlbumV3(TestBaseOnline):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_click_next_without_book_name(self):
        page: CreateAlbumsV3 = self.browser_online.navigate(configuration['online_v3_url_prod'], CreateAlbumsV3)
        page.click_next()
        text_err = page.get_err()
        assert text_err == " שם הספר הוא חובה "