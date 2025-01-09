import pytest
from playwright.sync_api import Page

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestPersonalDetails:

    def test_filler_detail(self, page):
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()


    def test_fill_personal_details(self, page):
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        personal_details = PersonalDetails(page)
        personal_details.fill_personal_details(
            "אופיר",
            "בדיקות",
            "פתח תקוה",
            "תוצרת הארץ",
            "3",
            "15",
            "10005",
            "6746933",
            "054"
        )



