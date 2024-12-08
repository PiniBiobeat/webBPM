import pytest
from playwright.sync_api import Page
from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Test_Pages.test_C_personalDetails import TestPersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from tests.TestPayment.test_add_book_V3 import TestAddBookV3


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestSummary:

    def test_add_coupon(self, page):
        TestPersonalDetails().test_filler_detail(page)
        Summary(page).add_coupon("AlbumTest1")

    def test_checkout(self, page):
        TestPersonalDetails().test_filler_detail(page)
        Summary(page).checkouts()