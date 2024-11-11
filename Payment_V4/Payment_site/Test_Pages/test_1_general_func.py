import pytest
from Payment_V4.Payment_site.Test_Pages.test_A_basket_items import TestBasketItems


@pytest.fixture
def page(request):
    return request.getfixturevalue('page')




class TestGeneralFunc:

    def test_other_page_basket(self, page):
        basket_test = TestBasketItems()
        basket_test.test_delete_all_items(page)