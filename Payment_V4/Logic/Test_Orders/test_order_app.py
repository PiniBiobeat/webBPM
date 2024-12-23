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

from Payment_V4.Logic.Logic_Orders.coupon_list import *
from Payment_V4.Logic.Logic_Orders.assert_order import AssertOrder


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestAppCouponSanity:

    def test_order_app_f35(self, page):
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        # Summary(page).add_coupon(get_coupon("AlbumFormat"))
        Summary(page).checkouts()
        page.pause()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().assert_order_details()


    @pytest.mark.parametrize("coupon_code", coupon_albums)
    def test_order_app_sanity_coupon(self, page, coupon_code):
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestAppCouponItems:

    @pytest.mark.parametrize("coupon_code", coupon_albums_items)
    def test_order_app_items(self, page, coupon_code):
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_הולנדי")
        AddBookV3().requestV3(page, "פורמט_38_מיני_לופה_קשה_רכה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=2, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=3, button="+", times=1)
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestAppCouponIsof:

    @pytest.mark.parametrize("coupon_code", coupon_albums_isof)
    def test_order_app_isof(self, page, coupon_code):
        AddBookV3().requestV3(page, "פורמט_6_קלאסי_פלוס_הולנדי")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()

    @pytest.mark.parametrize("coupon_code", coupon_albums_isof)
    def test_order_app_isof_short(self, page, coupon_code):
        AddBookV3().requestV3(page, "פורמט_6_קלאסי_פלוס_הולנדי")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).add_isof_code(get_coupon(coupon_code))
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestAppCouponShipping:

    @pytest.mark.parametrize("coupon_code", coupon_albums_shipping)
    def test_order_app_free_shipping(self, page, coupon_code):
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).ship_coupon_name(coupon_code)
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestAppCouponFix:

    @pytest.mark.parametrize("coupon_code", coupon_albums_fix)
    def test_order_app_fix_price(self, page, coupon_code):
        AddBookV3().requestV3(page, "פורמט_26_פנורמי_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestAppCouponPay40:

    @pytest.mark.parametrize("coupon_code", coupon_pay_for_40)
    def test_order_app_pay_40_pages(self, page, coupon_code):
        AddBookV3().requestV3(page, "אלבום_לבדיקת_144_עמודים")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_code)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
