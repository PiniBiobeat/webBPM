from playwright.sync_api import Page
import pytest



from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.coupon_list import get_coupon, coupon_tiles


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestTilesCoupon:

    def test_tiles_20x20(self, page):
        # wait for add tiles function from pini.
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon("Testofir"))
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


    @pytest.mark.parametrize("coupon_code", coupon_tiles)
    def test_order_tiles_20x20_with_all_coupon(self, page, coupon_code):
        # wait for add tiles function from pini
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_tiles).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
