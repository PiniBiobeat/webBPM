import pytest
from playwright.sync_api import Page
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


    def test_shops(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).shops("פתח תקוה", "ברזיל הקטנה")


    def test_post(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).post()


    @pytest.mark.xfail
    def test_home(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).home()


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


class Testisofcode:

    def test_add_isof_code(self, page):
        TestBasketItems().test_first_page(page)
        Shipping(page).add_isof_code("A35M9W1D")


    def test_error_isof_code_Expired(self, page):
        TestBasketItems().test_first_page(page)
        result = Shipping(page).add_isof_code("LUPALIVE99")
        assert result == 'עבר זמנו של הקופון שהקלדת, זהו נגמר :('


    def test_error_isof_code_item(self, page):
        TestBasketItems().test_first_page(page)
        result = Shipping(page).add_isof_code("Testisof")
        assert result == 'יש פה אי הבנה, הקופון שהקלדת בכלל שייך למוצר אחר (נמליץ לעבור על תנאי הקופון)'


    def test_error_isof_code_exist(self, page):
        TestBasketItems().test_first_page(page)
        result = Shipping(page).add_isof_code("dfdfgdf")
        assert result == 'הקופון שהקלדת לא קיים, כדאי לבדוק שהאותיות והמספרים מדויקים'


    def test_error_isof_code_none(self, page):
        TestBasketItems().test_first_page(page)
        result = Shipping(page).add_isof_code("")
        assert result == 'לא הוכנס קוד קופון'



