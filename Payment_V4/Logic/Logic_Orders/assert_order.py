import pytest

from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Payment_site.Pages.A_basket_items import BasketItems
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages.C_personalDetails import PersonalDetails
from Payment_V4.Payment_site.Pages.D_summary import Summary
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from Payment_V4.Payment_site.Pages.F_thanks import Thanks

from Payment_V4.Logic.Logic_Orders.data_order import DataConnection


class AssertOrder:

    def __init__(self):
        try:
            #lements From Pages
            self.sale_price, self.sale_items = BasketItems.valid_element_click_next
            self.ship_price = Shipping.return_ship_price
            self.item_count, self.base_price, self.total_discount, self.shipping_price, self.shipping_price_discount, self.final_price, = Summary.checkouts
            self.credit_card = CreditGuard.fill_credit_card
            self.order_number = Thanks.status


            # DABA BASE SQL: Orders.tbl
            self.order_id, self.master_id, self.in_status, self.total_items_quantity, self.total_items_price, self.total_order_price, self.discount_admin_value, self.discount_checkout_value, self.shipping_value, self.shipping_method, self.invoice_number = DataConnection().orders_tbl(self.order_number)


        except Exception as e:
            print(f"Element Not Return, Error{e}")


    def general_assert_orders(self):
        assert self.item_count == self.total_items_quantity
        assert self.base_price == self.total_items_price
        assert self.total_discount == self.total_items_quantity
        assert self.item_count == self.total_items_quantity
        assert self.final_price == self.total_order_price
        return self















# AssertOrder().assert_order_details()               #תמיד להשאיר ממורקר





#     def assert_order_details(self, summary):
#         assert summary.item_count == 1, f"Expected item count to be 1, but got {summary.item_count}"
#         assert summary.final_price == summary.base_price + summary.shipping_price - summary.total_discount - summary.shipping_price_discount, "Final price calculation mismatch"
#         assert summary.final_price > 0, f"Final price should be greater than 0, but got {summary.final_price}"
#         # Add more assertions as needed
