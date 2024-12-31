import pytest
from playwright.sync_api import Page

from tests.TestPayment.test_add_calendar import AddCalendar

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


class TestCalendarCouponSanity:

    def test_order_calendar_a5(self, page):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("CalendarFormat")
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


    @pytest.mark.parametrize("coupon_code", coupon_calendar)
    def test_order_online_sanity_coupon(self, page, coupon_code):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestCalendarCouponItems:

    @pytest.mark.parametrize("coupon_code", coupon_calendars_items)
    def test_order_calendar_items(self, page, coupon_code):
        AddCalendar().request_calendar(page, "לוח_A5")
        AddCalendar().request_calendar(page, "לוח_A4")
        AddCalendar().request_calendar(page, "לוח_A3")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=2, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=3, button="+", times=1)
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestCalendarCouponIsof:

    @pytest.mark.parametrize("coupon_code", coupon_calendar_isof)
    def test_order_calendar_isof(self, page, coupon_code):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


    @pytest.mark.parametrize("coupon_code", coupon_calendar_isof)
    def test_order_calendar_isof_short(self, page, coupon_code):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).add_isof_code(get_coupon(coupon_code))
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestCalendarCouponShipping:

    @pytest.mark.parametrize("coupon_code", coupon_calendar_shipping)
    def test_order_calendar_shipping(self, page, coupon_code):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).ship_coupon_name(coupon_code)
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


class TestCalendarCouponFix:

    @pytest.mark.parametrize("coupon_code", coupon_calendar_fix)
    def test_order_calendar_fix(self, page, coupon_code):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
