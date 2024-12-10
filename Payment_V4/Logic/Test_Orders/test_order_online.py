import pytest
from playwright.sync_api import Page

from tests.TestPayment.test_add_book_online import AddBookOnline

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


class TestOnlineCoupon:

    def test_order_online_f35(self, page):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon("AlbumFormat"))
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


    coupon_albums = coupon_albums + ["AlbumFormat"]
    @pytest.mark.parametrize("coupon_code", coupon_albums)
    def test_order_online_f35_all_coupon_sanity(self, page, coupon_code):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
