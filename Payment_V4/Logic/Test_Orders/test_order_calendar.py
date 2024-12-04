from playwright.sync_api import Page
import pytest



from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.copuns_album import copun_albums


@pytest.fixture
def page(request) -> Page:
    return request.getfixturevalue('page')


class TestCalendarCoupon:


    def test_calendar_a5(self, page):
        #wait for add calendar function from pini
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon("TestAlbum1").checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()



    @pytest.mark.parametrize("coupon_code", copun_albums.values())
    def test_order_app_f35_hard_with_all_coupon(self, page, coupon_code):
        #wait for add calendar function from pini
        Generalfunction(page).navigate("payment_url_books")
        BasketItems(page).valid_element_click_next()
        Shipping(page).asafta()
        PersonalDetails(page).filler_detail()
        Summary(page).add_coupon(coupon_code).checkouts()
        CreditGuard(page).fill_credit_card().to_pay()
        Thanks(page).status()
