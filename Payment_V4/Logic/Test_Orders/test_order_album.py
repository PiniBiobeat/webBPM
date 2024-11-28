from playwright.sync_api import Page
import pytest

from Payment_V4.Logic.Logic_Orders.copuns_album import copun_albums


from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary



from logic.pages.connect_create_user_page import ConnectCreateUserPage


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestAlbumCopuns:

    def test_order_album_v3_f35n(self, page):
        Generalfunction(page).navigate("my_book_url")
        ConnectCreateUserPage(page).click_add_book_to_payment()
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_image_item()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("AlbumTest1")



    @pytest.mark.parametrize("coupon_code", copun_albums.values())
    def test_order_album_v3_f35_with_all_coupon(self, page, coupon_code):
        Generalfunction(page).navigate("my_book_url")
        ConnectCreateUserPage(page).click_add_book_to_payment()
        Generalfunction(page).navigate("payment_url_books_test")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).valid_image_item()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code)
