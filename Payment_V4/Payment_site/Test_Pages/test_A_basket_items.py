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


class TestUIChangeFormatAndCovers:
    # app
    def test_books_app_ui_change_cover_format_27_and_38_to_soft(self, page):
        AddBookV3().requestV3(page, "פורמט_27_ריבועי_קטן_קשה")
        AddBookV3().requestV3(page, "פורמט_38_מיני_לופה_קשה")
        Generalfunction(page).navigate('payment_url_books')
        BasketItems(page).change_cover(1, "רכה")
        BasketItems(page).change_cover(2, "רכה")
        BasketItems(page).valid_element_click_next()


    # online
    @pytest.mark.parametrize("request_format, change_format_to, change_cover_to", [
        ("פורמט_35_ריבועי_גדול_קשה", "ריבועי קטן", None),
        ("פורמט_27_ריבועי_קטן_קשה", "ריבועי גדול", None),
        ("פורמט_35_ריבועי_גדול_הולנדי", "ריבועי קטן", None),
        ("פורמט_27_ריבועי_קטן_הולנדי", "ריבועי גדול", None),
        ("פורמט_35_ריבועי_גדול_קשה", None, "הולנדי"),
        ("פורמט_35_ריבועי_גדול_הולנדי", None, "קשה"),
        ("פורמט_27_ריבועי_קטן_קשה", None, "הולנדי"),
        ("פורמט_27_ריבועי_קטן_הולנדי", None, "קשה"),
        ("פורמט_35_ריבועי_גדול_קשה", "ריבועי קטן", "הולנדי"),
        ("פורמט_35_ריבועי_גדול_הולנדי", "ריבועי קטן", "קשה"),
        ("פורמט_27_ריבועי_קטן_קשה", "ריבועי גדול", "הולנדי"),
        ("פורמט_27_ריבועי_קטן_הולנדי", "ריבועי גדול", "קשה"),
        ("פורמט_27_ריבועי_קטן_קשה", "ריבועי גדול", "קשה"),
        ("פורמט_27_ריבועי_קטן_הולנדי", "ריבועי גדול", "הולנדי"),
        ("פורמט_35_ריבועי_גדול_קשה", "ריבועי קטן", "קשה"),
        ("פורמט_35_ריבועי_גדול_הולנדי", "ריבועי קטן", "הולנדי"),
        ("פורמט_35_ריבועי_גדול_קשה", "ריבועי קטן", "רכה"),
        ("פורמט_35_ריבועי_גדול_הולנדי", "ריבועי קטן", "רכה"),
        ("פורמט_27_ריבועי_קטן_קשה", None, "רכה"),
        ("פורמט_27_ריבועי_קטן_הולנדי", None, "רכה"),
    ])
    def test_books_online_ui_change_format_and_cover(self, page, request_format, change_format_to, change_cover_to):
        AddBookOnline().request_online(page, request_format)
        Generalfunction(page).navigate('payment_url_books')
        if change_format_to:
            BasketItems(page).change_format(1, change_format_to)
        if change_cover_to:
            BasketItems(page).change_cover(1, change_cover_to)
        BasketItems(page).valid_element_click_next()


    # tiles
    @pytest.mark.parametrize("request_tiles, cover_change_to, format_change_to", [
        ("tiles20X20", "30x30", None),
        ("tiles20X20kapa", "30x30", None),
        ("tiles30X30", "20x20", None),
        ("tiles30X30kapa", "20x20", None),
        ("tiles20X20", None, "מסגרת לבנה"),
        ("tiles20X20", None, "קאפה"),
        ("tiles20X20white", None, "מסגרת שחורה"),
        ("tiles20X20white", None, "קאפה"),
        ("tiles20X20kapa", None, "מסגרת שחורה"),
        ("tiles20X20kapa", None, "מסגרת לבנה"),
        ("tiles30X30", None, "קאפה"),
        ("tiles30X30kapa", None, "מסגרת שחורה"),
        ("tiles20X20", "30x30", "קאפה"),
        ("tiles30X30", "20x20", "מסגרת לבנה"),
        ("tiles30X30kapa", "20x20", "מסגרת שחורה"),
        ("tiles20X20kapa", "30x30", "מסגרת שחורה"),
        ("tiles30X30", "20x20", "קאפה"),
    ])
    def test_tiles_ui_changes(self, page, request_tiles, cover_change_to, format_change_to):
        AddTiles().request_tiles(page, request_tiles)
        Generalfunction(page).navigate('payment_url_tiles')
        if cover_change_to:
            BasketItems(page).change_cover(1, cover_change_to)
        if format_change_to:
            BasketItems(page).change_format(1, format_change_to)
        BasketItems(page).valid_element_click_next()
