import pytest
from playwright.sync_api import Page

from Payment_V4.Logic.Logic_Orders.data_order import ClearBasketApi
from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from tests.TestPayment.test_add_book_V3 import AddBookV3


@pytest.fixture
def page(request) -> Page:
    ClearBasketApi().clear_basket_before_tests()
    ClearBasketApi().clear_coupons_before_tests()
    return request.getfixturevalue('page')


def root_books(page, book="פורמט_35_ריבועי_גדול_קשה"):
    AddBookV3().requestV3(page, book)
    Generalfunction(page).navigate("payment_url_books")
    BasketItems(page).valid_element_click_next()


class TestShipping:

    def test_asafta_select(self, page):
        root_books(page)
        Shipping(page).asafta()


    def test_shops_select(self, page):
        root_books(page)
        Shipping(page).shops("פתח תקוה", "ברזיל הקטנה")


    def test_post_select(self, page):
        root_books(page)
        Shipping(page).post()


    def test_home_select(self, page):
        root_books(page)
        Shipping(page).home()


class TestShipping_Error_Validation:

    def test_no_shops_selection(self, page):
        root_books(page)
        Shipping(page).no_shops_selection_validation()


    def test_no_shops_validation(self, page):
        root_books(page)
        Shipping(page).no_shops_validation()


    def test_no_shops_deleting(self, page):
        root_books(page)
        Shipping(page).no_shops_deleting_validation()


    def test_no_shipping_selection_back_and_forward(self, page):
        root_books(page)
        Shipping(page).no_shipping_selection_back_and_forward_validation()


class TestIsofCode:

    def test_add_isof_code(self, page):
        root_books(page)
        Shipping(page).add_isof_code("A35M9W1D")


    def test_error_isof_code_Expired(self, page):
        root_books(page)
        result = Shipping(page).add_isof_code("LUPALIVE99")
        assert result == 'עבר זמנו של הקופון שהקלדת, זהו נגמר :('


    def test_error_isof_code_item(self, page):
        root_books(page)
        result = Shipping(page).add_isof_code("Testisof")
        assert result == 'יש פה אי הבנה, הקופון שהקלדת בכלל שייך למוצר אחר (נמליץ לעבור על תנאי הקופון)'


    def test_error_isof_code_exist(self, page):
        root_books(page)
        result = Shipping(page).add_isof_code("dfdfgdf")
        assert result == 'הקופון שהקלדת לא קיים, כדאי לבדוק שהאותיות והמספרים מדויקים'


    def test_error_isof_code_none(self, page):
        root_books(page)
        result = Shipping(page).add_isof_code("")
        assert result == 'לא הוכנס קוד קופון'
