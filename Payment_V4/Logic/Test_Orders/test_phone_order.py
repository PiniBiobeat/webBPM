import pytest
from playwright.sync_api import Page

from tests.TestPayment.test_add_book_V3 import AddBookV3
from tests.TestPayment.test_add_book_online import AddBookOnline
from tests.TestPayment.test_add_calendar import AddCalendar

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
# from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks


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


    def test_phone_order_online(self, page):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()


    def test_phone_order_calendar(self, page):
        AddCalendar().request_calendar(page, "לוח_A5")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()


    def test_phone_order_tiles(self, page):
        # wait for add tiles function from pini
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
