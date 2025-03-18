import pytest
from playwright.sync_api import Page
from Payment_V4.Logic.Logic_Orders.data_order import ClearBasketApi
from tests.TestAdmin.admin_function import AdminCoupon, AdminShipping
from tests.TestPayment.test_add_book_V3 import AddBookV3
from tests.TestPayment.test_add_book_online import AddBookOnline
from tests.TestPayment.test_add_calendar import AddCalendar
from tests.TestPayment.test_add_tiles import AddTiles

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.assert_order import AssertOrder



@pytest.fixture
def page(request) -> Page:
    ClearBasketApi().clear_basket_before_tests()
    ClearBasketApi().clear_coupons_before_tests()
    return request.getfixturevalue('page')








