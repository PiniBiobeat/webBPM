import pytest
import pytest_playwright

from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages._General_function import Generalfunction


@pytest.fixture
def page(request):
    return request.getfixturevalue('page')


class TestBasketItems:


    def root(self, page):
        self.generalfunction = Generalfunction(page)
        self.generalfunction.navigate('ofir_test')

    @pytest.mark.skip
    def test_delete_all_items(self, page):
        self.root(page)
        self.basketitems = BasketItems(page)
        self.basketitems.delete_all_items()


    def test_update_item_quantity(self, page):
        self.root(page)
        self.basket_items = BasketItems(page)
        self.basket_items.update_item_quantity(item_index=1, button="+", times=2)


