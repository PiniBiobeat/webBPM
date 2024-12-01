from playwright.sync_api import Page
import pytest
from tests.TestPayment.test_add_book_V3 import AddBookV3
from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary

from Payment_V4.Logic.Logic_Orders.copuns_album import copun_albums


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestAppCoupon:


    def test_order_app_f35_hard(self, page):
        AddBookV3().api_request(page, "פורמט 35 ריבועי גדול קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_image_item()
        Shipping(page).home()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930")
        page.pause()


    @pytest.mark.parametrize("coupon_code", copun_albums.values())
    def test_order_app_f35_hard_with_all_coupon(self, page, coupon_code):
        AddBookV3().api_request(page, "פורמט 35 ריבועי גדול קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_image_item()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("AlbumTest1")





