from playwright.sync_api import Page
import pytest

from logic.pages.connect_create_user_page import ConnectCreateUserPage

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.coupon_list import coupon_albums


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestOnlineCoupon:

    def test_order_online_f35(self, page):
        Generalfunction(page).navigate("my_book_url")
        ConnectCreateUserPage(page).click_add_book_to_payment()
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("AlbumTest1").checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()


    @pytest.mark.parametrize("coupon_code", coupon_albums.values())
    def test_order_online_f35_all_coupon_sanity(self, page, coupon_code):
        Generalfunction(page).navigate("my_book_url")
        ConnectCreateUserPage(page).click_add_book_to_payment()
        Generalfunction(page).navigate("payment_url_books_test")
        BasketItems(page).update_item_quantity(item_index=1, button="+", times=1)
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
