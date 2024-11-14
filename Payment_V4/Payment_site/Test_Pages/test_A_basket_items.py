from playwright.sync_api import Page
import pytest

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestBasketItems:


    def test_root(self, page):
        self.generalfunction = Generalfunction(page)
        self.generalfunction.navigate('ofir_test')


    def test_update_item_quantity(self, page):
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=1, button="-", times=1)

    def test_next_button(self, page):
        Generalfunction(page).next_button()




class TestDeleteBasket:
    @pytest.mark.skip
    def test_delete_all_items(self, page):
        TestBasketItems().test_root(page)
        BasketItems(page).delete_all_items()


