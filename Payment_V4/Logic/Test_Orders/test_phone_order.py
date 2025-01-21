import pytest
from playwright.sync_api import Page

from tests.TestAdmin.add_admin_coupon import AdminCoupon
from tests.TestPayment.test_add_book_V3 import AddBookV3
from tests.TestPayment.test_add_book_online import AddBookOnline
from tests.TestPayment.test_add_calendar import AddCalendar
from tests.TestPayment.test_add_tiles import AddTiles

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.assert_order import AssertOrder


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestPhoneOrder:

    def test_phone_order_app(self, page):
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).home()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
        AdminCoupon().add_admin_discount(page)
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).thank_page_status()


    def test_phone_order_online(self, page):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
        AdminCoupon().add_admin_discount(page)
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).thank_page_status()


    def test_phone_order_calendar(self, page):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
        AdminCoupon().add_admin_discount(page)
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).thank_page_status()


    def test_phone_order_tiles(self, page):
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
        AdminCoupon().add_admin_discount(page)
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).thank_page_status()


class TestChangeShippingOrder:
    pass


class TestChangeShippingPhoneOrder:

    def test_change_shipping_phone_order_app(self, page):
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).home()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
        AdminCoupon().change_shipping(page)
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).thank_page_status()
        assert AssertOrder().general_assert_orders()


    def test_change_shipping_phone_order_online(self, page):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
        AdminCoupon().change_shipping(page)
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).thank_page_status()
        assert AssertOrder().general_assert_orders()


    def test_change_shipping_phone_order_calendar(self, page):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
        AdminCoupon().change_shipping(page)
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).thank_page_status()
        assert AssertOrder().general_assert_orders()


    def test_change_shipping_phone_order_tiles(self, page):
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
        AdminCoupon().change_shipping(page)
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).thank_page_status()
        assert AssertOrder().general_assert_orders()


class TestAddCouponManual:

    def test_add_coupon_manual_app(self, page):
        AdminCoupon().add_coupon_manual(page)
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).home()
        PersonalDetails(page).filler_detail()
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


    def test_add_coupon_manual_online(self, page):
        AdminCoupon().add_coupon_manual(page)
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


    def test_add_coupon_manual_calendar(self, page):
        AdminCoupon().add_coupon_manual(page)
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


    def test_add_coupon_manual_tiles(self, page):
        AdminCoupon().add_coupon_manual(page, "33")
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()
