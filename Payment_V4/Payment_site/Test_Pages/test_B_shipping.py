import pytest
from playwright.sync_api import Page

from Payment_V4.Logic.Logic_Orders.data_order import ClearBasketApi, DataValidationMSG, DataPriceList
from tests.TestPayment.test_add_book_V3 import AddBookV3
from tests.TestPayment.test_add_book_online import AddBookOnline
from tests.TestPayment.test_add_calendar import AddCalendar
from tests.TestPayment.test_add_tiles import AddTiles
from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.D_summary import Summary


@pytest.fixture
def page(request) -> Page:
    ClearBasketApi().clear_basket_before_tests()
    ClearBasketApi().clear_coupons_before_tests()
    return request.getfixturevalue('page')


def root_books(page, product, item="פורמט_35_ריבועי_גדול_קשה"):
    if product == "app":
        AddBookV3().requestV3(page, item)
    elif product == "online":
        AddBookOnline().request_online(page, item)
    elif product == "calendar":
        AddCalendar().request_calendar(page, item)
    Generalfunction(page).navigate("payment_url_books")
    BasketItems(page).valid_element_click_next()


def root_books_marketing(page, product, item="פורמט_35_ריבועי_גדול_קשה"):
    if product == "app":
        AddBookV3().requestV3(page, item)
    elif product == "online":
        AddBookOnline().request_online(page, item)
    elif product == "calendar":
        AddCalendar().request_calendar(page, item)
    Generalfunction(page).navigate("payment_url_books")
    Generalfunction(page).next_button()
    BasketItems(page).valid_element_click_next()


class TestShippingBooks:

    def test_asafta_select(self, page):
        root_books("app", page)
        Shipping(page).asafta()


    def test_shops_select(self, page):
        root_books("app", page)
        Shipping(page).shops("פתח תקוה", "ברזיל הקטנה")


    def test_post_select(self, page):
        root_books("app", page)
        Shipping(page).post()


    def test_home_select(self, page):
        root_books("app", page)
        Shipping(page).home()


    @pytest.mark.xfail
    def test_add_isof_code(self, page):
        root_books("app", page)
        Shipping(page).add_isof_code("Album-isof-Code")


class TestShippingErrorValidationBooks:

    def test_no_shops_selection(self, page):
        root_books("app", page)
        Shipping(page).no_shops_selection_validation()


    def test_no_shops_validation(self, page):
        root_books("app", page)
        Shipping(page).no_shops_validation()


    def test_no_shops_after_clear_validation(self, page):
        root_books("app", page)
        Shipping(page).no_shops_deleting_validation()


    def test_no_shipping_selection_back_and_forward(self, page):
        root_books("app", page)
        Shipping(page).no_shipping_selection_back_and_forward_validation()


class TestShippingPriceBooks:

    @pytest.mark.parametrize("item", AddBookV3.token)
    @pytest.mark.parametrize("newsletter", ['True', 'False'])
    def test_shipping_price_app(self, page, item, newsletter):
        DataPriceList().sign_newsletter(newsletter)
        if newsletter == "True":
            root_books(page, "app", item)
            row = "shipPriceOnlineSpl"
        else:
            root_books_marketing(page, "app", item)
            row = "shipPriceOnline"
        shipping_methods = [Shipping(page).asafta, Shipping(page).shops, Shipping(page).post, Shipping(page).home]
        errors = []
        for method in shipping_methods:
            try:
                method()
                a_num = Shipping.a_num
                if item == "ספר_27_מסלול_מקוצר":
                    a_num = 5
                assert Shipping.return_ship_price_value == DataPriceList().get_shippint_pricelist(row, a_num)
            except AssertionError as e:
                errors.append(str(e))
            page.go_back()
        DataPriceList().sign_newsletter("True")
        if errors:
            raise AssertionError("\n".join(errors))


    @pytest.mark.parametrize("item", AddBookOnline.token)
    @pytest.mark.parametrize("newsletter", ['True', 'False'])
    def test_shipping_price_online(self, page, item, newsletter):
        DataPriceList().sign_newsletter(newsletter)
        if newsletter == "True":
            root_books(page, "online", item)
            row = "shipPriceOnlineSpl"
        else:
            root_books_marketing(page, "online", item)
            row = "shipPriceOnline"
        shipping_methods = [Shipping(page).asafta, Shipping(page).shops, Shipping(page).post, Shipping(page).home]
        errors = []
        for method in shipping_methods:
            try:
                method()
                assert Shipping.return_ship_price_value == DataPriceList().get_shippint_pricelist(row, Shipping.a_num)
            except AssertionError as e:
                errors.append(str(e))
            page.go_back()
        DataPriceList().sign_newsletter("True")
        if errors:
            raise AssertionError("\n".join(errors))


    @pytest.mark.parametrize("item", AddCalendar.items)
    @pytest.mark.parametrize("newsletter", ['True', 'False'])
    def test_shipping_price_calendar(self, page, item, newsletter):
        DataPriceList().sign_newsletter(newsletter)
        if newsletter == "True":
            root_books(page, "calendar", item)
            row = "shipPriceCalendarSpl"
        else:
            root_books_marketing(page, "calendar", item)
            row = "shipPriceCalendar"
        shipping_methods = [Shipping(page).asafta, Shipping(page).shops, Shipping(page).post, Shipping(page).home]
        errors = []
        for method in shipping_methods:
            try:
                method()
                assert Shipping.return_ship_price_value == DataPriceList().get_shippint_pricelist(row, Shipping.a_num)
            except AssertionError as e:
                errors.append(str(e))
            page.go_back()
        DataPriceList().sign_newsletter("True")
        if errors:
            raise AssertionError("\n".join(errors))


class TestIsofCodeValidationBooks:

    def test_error_isof_code_Expired(self, page):
        with pytest.raises(Exception) as p:
            root_books("app", page)
            Shipping(page).add_isof_code("CouponExpired")  # 'עבר זמנו של הקופון שהקלדת, זהו נגמר :('
        assert str(p.value) == DataValidationMSG().validate_msg("CouponExpired")


    def test_error_isof_code_item(self, page):
        with pytest.raises(Exception) as p:
            root_books("app", page)
            Shipping(page).add_isof_code(
                "Tiles-isof-Code")  # 'יש פה אי הבנה, הקופון שהקלדת בכלל שייך למוצר אחר (נמליץ לעבור על תנאי הקופון'
        assert str(p.value) == DataValidationMSG().validate_msg("CouponIrrelevant")


    def test_error_isof_code_exist(self, page):
        root_books("app", page)
        with pytest.raises(Exception) as p:
            Shipping(page).add_isof_code("dfdfgdf")  # 'הקופון שהקלדת לא קיים, כדאי לבדוק שהאותיות והמספרים מדויקים'
        assert str(p.value) == DataValidationMSG().validate_msg("CouponNotFound")


    @pytest.mark.xfail
    def test_error_isof_code_Benefit(self, page):
        with pytest.raises(Exception) as p:
            root_books("app", page)
            Shipping(page).add_isof_code(
                "Test_Sal_item_isof")  # 'יש פה אי הבנה, הקופון אינו מקנה הטבה בהזמנה זו (נמליץ לעבור על תנאי הקופון)'
        assert str(p.value) == DataValidationMSG().validate_msg("CouponHasNoValue")


    def test_error_isof_code_none(self, page):
        root_books("app", page)
        with pytest.raises(Exception) as p:
            Shipping(page).add_isof_code("")
        assert str(p.value) == "לא הוכנס קוד קופון"


##################  tiles  ##################

def root_tiles(page, item="tiles20X20"):
    AddTiles().request_tiles(page, item)
    Generalfunction(page).navigate("payment_url_tiles")
    BasketItems(page).valid_element_click_next()


def root_tiles_marketing(page, item="tiles20X20"):
    AddTiles().request_tiles(page, item)
    Generalfunction(page).navigate("payment_url_tiles")
    Generalfunction(page).next_button()
    BasketItems(page).valid_element_click_next()


class TestShippingTiles:

    def test_asafta_select_tiles(self, page):
        root_tiles(page)
        Shipping(page).asafta()


    def test_shops_select_tiles(self, page):
        root_tiles(page)
        Shipping(page).shops("פתח תקוה", "ברזיל הקטנה")


    def test_post_select_tiles(self, page):
        root_tiles(page)
        Shipping(page).post()


    def test_home_select_tiles(self, page):
        root_tiles(page)
        Shipping(page).home()


    @pytest.mark.xfail
    def test_add_isof_code_tiles(self, page):
        root_tiles(page)
        Shipping(page).add_isof_code("Tiles-isof-Code")


class TestShippingPriceTiles:

    @pytest.mark.parametrize("item", AddTiles.tiles_format)
    @pytest.mark.parametrize("newsletter", ['True', 'False'])
    def test_shipping_price_app(self, page, item, newsletter):
        DataPriceList().sign_newsletter(newsletter)
        if newsletter == "True":
            root_tiles(page, item)
            row = "shipPriceTilesSpl"
        else:
            root_tiles_marketing(page, item)
            row = "shipPriceTiles"
        shipping_methods = [Shipping(page).asafta, Shipping(page).shops, Shipping(page).post, Shipping(page).home]
        errors = []
        for method in shipping_methods:
            try:
                method()
                assert Shipping.return_ship_price_value == DataPriceList().get_shippint_pricelist(row, Shipping.a_num)
            except AssertionError as e:
                errors.append(str(e))
            page.go_back()
        DataPriceList().sign_newsletter("True")
        if errors:
            raise AssertionError("\n".join(errors))


class TestShippingErrorValidationTiles:

    def test_no_shops_selection_tiles(self, page):
        root_tiles(page)
        Shipping(page).no_shops_selection_validation()


    def test_no_shops_validation_tiles(self, page):
        root_tiles(page)
        Shipping(page).no_shops_validation()


    def test_no_shops_after_clear_validation_tiles(self, page):
        root_tiles(page)
        Shipping(page).no_shops_deleting_validation()


    def test_no_shipping_selection_back_and_forward_tiles(self, page):
        root_tiles(page)
        Shipping(page).no_shipping_selection_back_and_forward_validation()


class TestIsofCodeValidationTiles:

    def test_error_isof_code_Expired_tiles(self, page):
        with pytest.raises(Exception) as p:
            root_tiles(page)
            Shipping(page).add_isof_code("CouponExpired")  # 'עבר זמנו של הקופון שהקלדת, זהו נגמר :('
        assert str(p.value) == DataValidationMSG().validate_msg("CouponExpired")


    def test_error_isof_code_item_tiles(self, page):
        with pytest.raises(Exception) as p:
            root_tiles(page)
            Shipping(page).add_isof_code(
                "Album-isof-Code")  # 'יש פה אי הבנה, הקופון שהקלדת בכלל שייך למוצר אחר (נמליץ לעבור על תנאי הקופון'
        assert str(p.value) == DataValidationMSG().validate_msg("CouponIrrelevant")


    def test_error_isof_code_exist_tiles(self, page):
        root_tiles(page)
        with pytest.raises(Exception) as p:
            Shipping(page).add_isof_code("dfdfgdf")  # 'הקופון שהקלדת לא קיים, כדאי לבדוק שהאותיות והמספרים מדויקים'
        assert str(p.value) == DataValidationMSG().validate_msg("CouponNotFound")


    @pytest.mark.xfail
    def test_error_isof_code_Benefit_tiles(self, page):
        with pytest.raises(Exception) as p:
            root_tiles(page)
            Shipping(page).add_isof_code(
                "Test_Sal_item_isof")  # 'יש פה אי הבנה, הקופון אינו מקנה הטבה בהזמנה זו (נמליץ לעבור על תנאי הקופון)'
        assert str(p.value) == DataValidationMSG().validate_msg("CouponHasNoValue")


    def test_error_isof_code_none_tiles(self, page):
        root_tiles(page)
        with pytest.raises(Exception) as p:
            Shipping(page).add_isof_code("")
        assert str(p.value) == "לא הוכנס קוד קופון"
