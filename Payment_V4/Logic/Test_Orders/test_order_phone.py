from playwright.sync_api import Page
import pytest

from tests.TestPayment.test_add_book_V3 import AddBookV3
from logic.pages.connect_create_user_page import ConnectCreateUserPage

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.copuns_album import copun_albums


class TestPhoneOrder:


    def test_phone_order_app(self, page):
        AddBookV3().api_request(page, "פורמט_35_ריבועי_גדול_קשה")
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).home()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()


    def test_phone_order_online(self, page):
        Generalfunction(page).navigate("my_book_url")
        ConnectCreateUserPage(page).click_add_book_to_payment()
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("12930").checkouts()
        Thanks(page).status()
