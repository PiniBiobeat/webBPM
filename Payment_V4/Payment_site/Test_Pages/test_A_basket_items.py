from playwright.sync_api import Page
import pytest
from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestBasketItems:

    def test_root(self, page):
        Generalfunction(page).navigate('payment_url_books')


    def test_update_item_quantity(self, page):
        Generalfunction(page).navigate('payment_url_books')
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=1, button="-", times=1)


    def test_first_page(self, page):
        Generalfunction(page).navigate('payment_url_books')
        Generalfunction(page).next_button()


    def test_valid_element(self, page):
        Generalfunction(page).navigate('payment_url_books')
        BasketItems(page).valid_element_click_next()


class TestDeleteBasket:
    @pytest.mark.skip
    def test_delete_all_items(self, page):
        Generalfunction(page).navigate('payment_url_books')
        BasketItems(page).delete_all_items()
