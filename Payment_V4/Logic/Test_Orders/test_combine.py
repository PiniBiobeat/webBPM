import pytest
from playwright.sync_api import Page

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

from Payment_V4.Logic.Logic_Orders.coupon_list import *
from Payment_V4.Logic.Logic_Orders.assert_order import AssertOrder


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestCombineCouponSanity:

    def test_order_combine(self, page):
        AddCalendar().request_calendar(page, "לוח_A5")
        AddBookV3().requestV3(page, "פורמט_35_ריבועי_גדול_קשה")
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_הולנדי")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("CombineFormat")
        page.pause()
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


    @pytest.mark.parametrize("coupon_code, coupon_code2", zip(coupon_albums, coupon_calendar))
    def test_order_combine_sanity_coupon(self, page, coupon_code, coupon_code2):
        AddCalendar().request_calendar(page, "לוח_A3")
        AddBookV3().requestV3(page, "פורמט_6_קלאסי_פלוס_קשה")
        AddBookOnline().request_online(page, "פורמט_27_ריבועי_קטן_הולנדי")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).shops()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code)
        Summary(page).add_coupon(coupon_code2).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()









