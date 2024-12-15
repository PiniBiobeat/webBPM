import pytest
from playwright.sync_api import Page

from playwright.sync_api import Page

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.coupon_list import *


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestTilesCouponSanity:

    def test_order_tiles_20x20(self, page):
        # wait for add tiles function from pini.
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon("TilesFormat"))
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


    @pytest.mark.parametrize("coupon_code", coupon_tiles)
    def test_order_tiles_sanity_coupon(self, page, coupon_code):
        # wait for add tiles function from pini
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestTilesCouponItems:

    @pytest.mark.parametrize("coupon_code", coupon_tiles_items)
    def test_order_tiles_items(self, page, coupon_code):
        # wait for add tiles function from pini
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestTilesCouponIsof:

    @pytest.mark.parametrize("coupon_code", coupon_tiles_isof)
    def test_order_tiles_isof(self, page, coupon_code):
        # wait for add tiles function from pini
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestTilesCouponShipping:

    @pytest.mark.parametrize("coupon_code", coupon_tiles_shipping)
    def test_order_tiles_shipping(self, page, coupon_code):
        # wait for add tiles function from pini
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).ship_by_code_name(coupon_code)
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestTilesCouponFix:

    @pytest.mark.parametrize("coupon_code", coupon_tiles_fix)
    def test_order_tiles_fix(self, page, coupon_code):
        # wait for add tiles function from pini
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
