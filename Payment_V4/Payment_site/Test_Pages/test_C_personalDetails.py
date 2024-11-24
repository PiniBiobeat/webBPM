import pytest
from playwright.sync_api import Page

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Test_Pages.test_B_shipping import TestShipping


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestPersonalDetails:

    def test_fill_personal_details(self, page: Page):
        TestShipping().test_asafta(page)
        personal_details = PersonalDetails(page)
        personal_details.fill_personal_details("אופיר1", "בדיקות1", "פתח תקוה", "תוצרת הארץ", "3", "15", "10005", "6746933", "054")



