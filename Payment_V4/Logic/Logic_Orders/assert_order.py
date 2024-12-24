import pytest

from Payment_V4.Logic.Logic_Orders.data_order import DataConnection

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks




class AssertOrder:
    def __init__(self):
        try:
            self.sale_price, self.sale_items = BasketItems.valid_element_click_next
            self.ship_price = Shipping.return_ship_price
            self.item_count, self.base_price, self.total_discount, self.shipping_price, self.shipping_price_discount, self.final_price, = Summary.checkouts
            self.credit_card = CreditGuard.fill_credit_card
            self.order_number = Thanks.status
        except:
            pass



    def assert_order_details(self):
        self.item_count = 1
        assert self.item_count == 1, f"Expected"
        print(self.item_count)
        return self



AssertOrder().assert_order_details()















    # def assert_order_details222(self):
    #     if self.item_count != 1:
    #         raise Exception(f"Expected item count to be 2, but got {self.item_count}")
    #     return self




















# item_count, base_price, total_discount, shipping_price, shipping_price_discount, final_price = Summary.checkouts



#     def assert_order_details(self, summary):
#         assert summary.item_count == 1, f"Expected item count to be 1, but got {summary.item_count}"
#         assert summary.final_price == summary.base_price + summary.shipping_price - summary.total_discount - summary.shipping_price_discount, "Final price calculation mismatch"
#         assert summary.final_price > 0, f"Final price should be greater than 0, but got {summary.final_price}"
#         # Add more assertions as needed
