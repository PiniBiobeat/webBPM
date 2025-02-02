import pytest
from playwright.sync_api import Page

from tests.TestPayment.test_add_tiles import AddTiles

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.coupon_list import *
from Payment_V4.Logic.Logic_Orders.assert_order import AssertOrder


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestTilesCouponSanity:

    def test_order_tiles_20x20(self, page):
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("TilesFormat")
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()


    @pytest.mark.parametrize("coupon_code", coupon_tiles)
    def test_order_tiles_sanity_coupon(self, page, coupon_code):
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()


class TestTilesCouponItems:

    @pytest.mark.parametrize("coupon_code", coupon_tiles_items)
    def test_order_tiles_items(self, page, coupon_code):
        AddTiles().request_tiles(page, "tiles20X20")
        AddTiles().request_tiles(page, "tiles20X20kapa")
        AddTiles().request_tiles(page, "tiles30X30")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=2, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=3, button="+", times=1)
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()


class TestTilesCouponIsof:

    @pytest.mark.parametrize("coupon_code", coupon_tiles_isof)
    def test_order_tiles_isof(self, page, coupon_code):
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()


    @pytest.mark.parametrize("coupon_code", coupon_tiles_isof)
    def test_order_tiles_isof(self, page, coupon_code):
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).add_isof_code(get_coupon(coupon_code))
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()


class TestTilesCouponShipping:

    @pytest.mark.parametrize("coupon_code", coupon_tiles_shipping)
    def test_order_tiles_shipping(self, page, coupon_code):
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).ship_coupon_name(coupon_code)
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()


class TestTilesCouponFix:

    @pytest.mark.parametrize("coupon_code", coupon_tiles_fix)
    def test_order_tiles_fix(self, page, coupon_code):
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()


class TestTilesCouponType:

    @pytest.mark.parametrize("coupon_code", coupon_tiles_type_name)
    def test_order_tiles_type_name(self, page, coupon_code):
        AddTiles().request_tiles(page, "tiles20X20")
        AddTiles().request_tiles(page, "tiles20X20white")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=2, button="+", times=1)
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()


    @pytest.mark.parametrize("coupon_code", coupon_tiles_type_code)
    def test_order_tiles_type_name(self, page, coupon_code):
        AddTiles().request_tiles(page, "tiles20X20")
        AddTiles().request_tiles(page, "tiles30X30")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code)
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder(db="lupa_square").general_assert_orders()


# special cases for tiles
class TestTilesQuantityDiscount:

    def test_order_tiles_20x20_with_quantity_10(self, page, ):
        AddTiles().request_tiles(page, "tiles20X20")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=9)
        BasketItems(page).get_quantity_discount().valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert BasketItems.return_quantity_discount == 90
        assert AssertOrder(db="lupa_square").general_assert_orders()


    def test_order_tiles_30x30_with_quantity_10(self, page, ):
        AddTiles().request_tiles(page, "tiles30X30")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=9)
        BasketItems(page).get_quantity_discount().valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert BasketItems.return_quantity_discount == 90
        assert AssertOrder(db="lupa_square").general_assert_orders()


    def test_order_tiles_20x20_and_30x30_with_quantity_20(self, page, ):
        AddTiles().request_tiles(page, "tiles20X20")
        AddTiles().request_tiles(page, "tiles30X30")
        Generalfunction(page).navigate("payment_url_tiles")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=9)
        BasketItems(page).update_item_quantity(item_index=2, button="+", times=9)
        BasketItems(page).get_quantity_discount().valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert BasketItems.return_quantity_discount == 180
        assert AssertOrder(db="lupa_square").general_assert_orders()