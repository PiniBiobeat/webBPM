from playwright.sync_api import Page
import pytest

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Test_Pages.test_A_basket_items import TestBasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestShipping:


    def test_asafta(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).asafta()
        Generalfunction(page).next_button()


    def test_shops(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).shops("פתח תקוה", "ברזיל הקטנה")
        Generalfunction(page).next_button()

    def test_post(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).post()
        Generalfunction(page).next_button()


    def test_home(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).home()
        Generalfunction(page).next_button()



class TestShippingError:

    def test_no_shops_selection(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).no_shops_selection()


    def test_no_shops_validation(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).no_shops_validation()


    def test_no_shops_deleting(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).no_shops_deleting()


    def test_no_shipping_selection_back_and_forward(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).no_shipping_selection_back_and_forward()
