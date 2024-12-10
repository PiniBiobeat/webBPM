import pytest
from playwright.sync_api import Page

from tests.TestPayment.test_add_book_V3 import AddBookV3

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.coupon_list import get_coupon, coupon_albums


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestAppCoupon:

    def test_order_app_f35(self, page):
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon("AlbumTest")).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


    coupon_albums = coupon_albums + ["AlbumFormat"]
    @pytest.mark.parametrize("coupon_code", coupon_albums)
    def test_order_app_f35_hard_with_all_coupon(self, page, coupon_code):
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
