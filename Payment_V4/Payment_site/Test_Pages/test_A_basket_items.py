from playwright.sync_api import Page
import pytest

from Payment_V4.Logic.Logic_Orders.data_order import ClearBasketApi
from tests.TestPayment.test_add_book_V3 import AddBookV3
from tests.TestPayment.test_add_book_online import AddBookOnline
from tests.TestPayment.test_add_calendar import AddCalendar
from tests.TestPayment.test_add_tiles import AddTiles

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems


@pytest.fixture
def page(request) -> Page:
    ClearBasketApi().clear_basket_before_tests()
    ClearBasketApi().clear_coupons_before_tests()
    return request.getfixturevalue('page')


class TestBasketItemsBooks:

    def root_books(self, page, item="פורמט_35_ריבועי_גדול_קשה"):
        AddBookV3().requestV3(page, item)
        Generalfunction(page).navigate('payment_url_books')


    def test_update_item_quantity_books(self, page):
        self.root_books(page)
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=1, button="-", times=1)


    def test_first_page_books(self, page):
        self.root_books(page)
        Generalfunction(page).next_button()


    def test_valid_element_books(self, page):
        self.root_books(page)
        BasketItems(page).valid_element_click_next()


    def test_change_format_books(self, page):
        self.root_books(page, item="ספר_27_מסלול_מקוצר")
        BasketItems(page).change_format(1, "ריבועי גדול")


    def test_change_cover_books(self, page):
        self.root_books(page, item="פורמט_27_ריבועי_קטן_קשה")
        BasketItems(page).change_cover(1, "רכה")


    def test_delete_all_items_book(self, page):
        add_item_app = AddBookV3()
        for item_app in add_item_app.token.keys():
            add_item_app.requestV3(page, item_app)

        add_item_online = AddBookOnline()
        for item_online in add_item_online.token.keys():
            add_item_online.request_online(page, item_online)

        add_item_calendar = AddCalendar()
        for item_calendar in add_item_calendar.items.keys():
            add_item_calendar.request_calendar(page, item_calendar)

        Generalfunction(page).navigate('payment_url_books')
        BasketItems(page).delete_all_items()


class TestBasketItemsTiles:

    def root_tiles(self, page, item="tiles20X20"):
        AddTiles().request_tiles(page, item)
        Generalfunction(page).navigate('payment_url_tiles')


    def test_update_item_quantity_tiles(self, page):
        self.root_tiles(page)
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=1, button="-", times=1)


    def test_first_page_tiles(self, page):
        self.root_tiles(page)
        Generalfunction(page).next_button()


    def test_valid_element_tiles(self, page):
        self.root_tiles(page)
        BasketItems(page).valid_element_click_next()


    def test_change_format_tiles(self, page):
        self.root_tiles(page)
        BasketItems(page).change_format(1, "קאפה")


    def test_change_cover_tiles(self, page):
        self.root_tiles(page)
        BasketItems(page).change_cover(1, "30x30")


    def test_delete_all_items_tiles(self, page):
        add_tiles_items = AddTiles()
        for item_tiles in add_tiles_items.tiles_format.keys():
            add_tiles_items.request_tiles(page, item_tiles)
        Generalfunction(page).navigate('payment_url_tiles')
        BasketItems(page).delete_all_items()
