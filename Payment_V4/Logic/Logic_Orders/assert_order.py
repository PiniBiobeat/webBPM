import pytest

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks


item_count, base_price, total_discount, shipping_price, shipping_price_discount, final_price = Summary.checkouts

class AssertOrders:

    def assert_order_details(self):
        assert item_count == 2




















# class TestAppCouponSanity:
#     def assert_order_details(self, summary):
#         assert summary.item_count == 1, f"Expected item count to be 1, but got {summary.item_count}"
#         assert summary.final_price == summary.base_price + summary.shipping_price - summary.total_discount - summary.shipping_price_discount, "Final price calculation mismatch"
#         assert summary.final_price > 0, f"Final price should be greater than 0, but got {summary.final_price}"
#         # Add more assertions as needed
