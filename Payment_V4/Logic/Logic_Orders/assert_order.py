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

    def __init__(self, db="lupa_online"):
        try:
            # Elements From Pages
            self.sale_price, self.sale_items = BasketItems.valid_element_click_next  #wait
            self.ship_selected_price = Shipping.return_ship_price #wait
            self.item_count, self.base_price, self.total_discount, self.shipping_price, self.shipping_price_discount, self.final_price, = Summary.checkouts
            self.credit_card = CreditGuard.to_pay  #wait
            self.order_number = Thanks.status


            # DABA BASE SQL: Orders.tbl
            self.order_id, self.master_id, self.in_status, self.total_items_quantity, self.total_items_price, self.total_order_price, self.shipping_value, self.shipping_method, self.invoice_number = DataConnection().orders_tbl(self.order_number, db)
            # DABA BASE PG14: coupon.tbl
            self.discount_actual_value = DataConnection().total_discount_sum(self.order_number)

        except Exception as e:
            print(f"Element Not Return, Error{e}")


    def general_assert_orders(self):
        assert self.item_count == self.total_items_quantity, f"Element item count: {self.item_count}, not match signed db: {self.total_items_quantity}."
        assert self.base_price == self.total_items_price, f"Element Base price: {self.base_price}, not match signed db: {self.total_items_price}."
        assert self.total_discount == self.discount_actual_value, f"Element discount: {self.total_discount}, not match signed db: {self.discount_actual_value}."
        assert self.shipping_price - self.shipping_price_discount == self.shipping_value, f"Element ship {self.shipping_price_discount} and summary ship {self.shipping_price} not match signed db: {self.shipping_value}."
        assert self.final_price == self.total_order_price, f"Element final price: {self.final_price}, not match signed db: {self.total_order_price}."
        assert self.invoice_number.isdigit(), f"invoice not created"
        return self






















# AssertOrder().general_assert_orders()               #תמיד להשאיר ממורקר

# assert self.delivery_method == self.shipping_method, f"delivery selected method is: {self.delivery_method}, not match signed db: {self.shipping_method}."