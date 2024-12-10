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

from Payment_V4.Logic.Logic_Orders.coupon_list import get_coupon, coupon_calendar


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestCalendarCoupon:

    def test_calendar_a5(self, page):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon("CalendarFormat"))
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


    @pytest.mark.parametrize("coupon_code", coupon_calendar)
    def test_test_calendar_a5_with_all_coupon(self, page, coupon_code):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(get_coupon(coupon_calendar)).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
