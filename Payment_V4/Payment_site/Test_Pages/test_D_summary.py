import pytest
from playwright.sync_api import Page
from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Test_Pages.test_C_personalDetails import TestPersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary

@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestSummary:

    def test_add_coupon(self, page):
        TestPersonalDetails().test_filler_detail(page)
        Summary(page).add_coupon("AlbumTest1")
