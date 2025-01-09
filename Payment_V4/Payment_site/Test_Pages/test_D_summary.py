import pytest
from playwright.sync_api import Page

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestSummary:

    def test_add_coupon(self, page):
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        Summary(page).add_coupon("AlbumTest1")

    def test_checkout(self, page):
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).checkouts()