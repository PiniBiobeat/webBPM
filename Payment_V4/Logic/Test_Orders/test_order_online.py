import pytest
from playwright.sync_api import Page
from Payment_V4.Logic.Logic_Orders.data_order import ClearBasketApi
from tests.TestPayment.test_add_book_online import AddBookOnline

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
    ClearBasketApi().clear_basket_before_tests()
    ClearBasketApi().clear_coupons_before_tests()
    return request.getfixturevalue('page')


class TestOnlineCouponSanity:

    def test_order_online_f35(self, page):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        # BasketItems(page).valid_element_click_next()
        # Shipping(page).asafta()
        # PersonalDetails(page).filler_detail()
        # Summary(page).add_coupon("AlbumFormat")
        # Summary(page).checkouts()
        # CreditGuard(page).fill_credit_card().to_pay()
        # Thanks(page).status()
        assert AssertOrder().general_assert_orders()


    @pytest.mark.parametrize("coupon_code", coupon_albums)
    def test_order_online_sanity_coupon(self, page, coupon_code):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


class TestOnlineCouponItems:

    @pytest.mark.parametrize("coupon_code", coupon_albums_items)
    def test_order_online_items(self, page, coupon_code):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_הולנדי")
        AddBookOnline().request_online(page, "פורמט_27_ריבועי_קטן_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=2, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=3, button="+", times=1)
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


class TestOnlineCouponIsof:

    @pytest.mark.parametrize("coupon_code", coupon_albums_isof)
    def test_order_online_isof(self, page, coupon_code):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


    @pytest.mark.parametrize("coupon_code", coupon_albums_isof)
    def test_order_online_isof_short(self, page, coupon_code):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).add_isof_code(get_coupon(coupon_code))
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


class TestOnlineCouponShipping:

    @pytest.mark.parametrize("coupon_code", coupon_albums_shipping)
    def test_order_online_free_shipping(self, page, coupon_code):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).ship_coupon_name(coupon_code)
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


class TestOnlineCouponFix:

    @pytest.mark.parametrize("coupon_code", coupon_albums_fix)
    def test_order_online_fix_price(self, page, coupon_code):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


class TestOnlineCouponType:

    @pytest.mark.parametrize("coupon_code", coupon_albums_type_name)
    def test_order_online_type_name(self, page, coupon_code):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        AddBookOnline().request_online(page, "פורמט_27_ריבועי_קטן_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


    @pytest.mark.parametrize("coupon_code", coupon_albums_type_code)
    def test_order_online_type_code(self, page, coupon_code):
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_קשה")
        AddBookOnline().request_online(page, "פורמט_35_ריבועי_גדול_הולנדי")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code)
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


# special cases for online
class TestOnlineCouponPay40:

    @pytest.mark.parametrize("coupon_code", coupon_pay_for_40)
    def test_order_online_pay_40_pages(self, page, coupon_code):
        AddBookOnline().request_online(page, "אלבום_לבדיקת_144_עמודים")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()


class TestOnlineHaggadah:

    @pytest.mark.parametrize("coupon_code", coupon_haggadah)
    def test_order_online_haggadah(self, page, coupon_code):
        AddBookOnline().request_online(page, "הגדה_פורמט_35_ריבועי_גדול")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
        assert AssertOrder().general_assert_orders()

# class TestOnlineShortWay:
#
#     @pytest.mark.parametrize("coupon_code", coupon_short_way)
#     def test_order_online_short_way(self, page, coupon_code):
#         AddBookOnline().request_online(page, "עתידי")
#         Generalfunction(page).navigate("payment_url_books")
#         BasketItems(page).valid_element_click_next()
#         Shipping(page).home()
#         PersonalDetails(page).filler_detail()
#         Summary(page).checkouts()
#         CreditGuard(page).fill_credit_card().to_pay()
#         Thanks(page).status()
#         assert AssertOrder().general_assert_orders()


# class TestOnlineMiniLupa:
#
#         @pytest.mark.parametrize("coupon_code", coupon_mini_lupa)
#         def test_order_online_mini_lupa(self, page, coupon_code):
#             AddBookOnline().request_online(page, "מיני_לופה עתידי")
#             Generalfunction(page).navigate("payment_url_books")
#             BasketItems(page).valid_element_click_next()
#             Shipping(page).asafta()
#             PersonalDetails(page).filler_detail()
#             Summary(page).add_coupon(coupon_code).checkouts()
#             CreditGuard(page).fill_credit_card().to_pay()
#             Thanks(page).status()
#             assert AssertOrder().general_assert_orders()
