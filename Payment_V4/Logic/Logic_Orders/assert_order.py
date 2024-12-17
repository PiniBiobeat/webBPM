
from Payment_V4.Payment_site.Pages.D_summary import Summary



class AssertOrder:

    def assert_order_details(self):
        item_count, base_price, total_discount, shipping_price, shipping_price_discount, final_price = Summary.checkouts
        assert item_count == 1



















# class TestAppCouponSanity:
#     def assert_order_details(self, summary):
#         assert summary.item_count == 1, f"Expected item count to be 1, but got {summary.item_count}"
#         assert summary.final_price == summary.base_price + summary.shipping_price - summary.total_discount - summary.shipping_price_discount, "Final price calculation mismatch"
#         assert summary.final_price > 0, f"Final price should be greater than 0, but got {summary.final_price}"
#         # Add more assertions as needed
