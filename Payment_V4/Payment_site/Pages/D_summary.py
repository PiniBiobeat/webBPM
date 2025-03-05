from playwright.sync_api import Page, expect
from decimal import Decimal
import allure
from Payment_V4.Logic.Logic_Orders.coupon_list import get_coupon, get_coupon_title
from Payment_V4.Payment_site.Pages.B_shipping import Shipping
from Payment_V4.Payment_site.Pages._General_function import Generalfunction

class Summary:

    coupon_field = '.MuiInputBase-input'
    coupon_confirm = ".MuiButton-text"
    coupon_error = "(//div[@class='summary_page container page MuiBox-root css-0']//p)[1]"
    coupon_value_price = "(//div[@class='content_selected_coupon MuiBox-root css-0']/div[@class='box_item_l MuiBox-root css-0'])"
    loader = '[class*="MuiCircularProgress-circle"]'


    item_count = "(//p[text()=':סה״כ פריטים']//..//p[@class='box_itemL'])[1]"
    base_price = "(//p[text()=':מחיר מחירון']//..//p[@class='box_itemL'])[1]"
    total_discount = "(//p[text()=':הנחות נוספות']//..//p[@class='box_itemL'])[1]"
    shipping_price = "(//p[text()=':משלוח']//..//p[@class='box_itemL'])[1]"
    shipping_price_discount = "(//p[text()=':הנחת משלוח']//..//p[@class='box_itemL'])[1]"
    final_prices = "//h3[text()=':סה״כ לתשלום']//..//h3[@class='box_itemL']"

    coupon_switch = "//div[@class='box_item_l bold' and text()='{coupon_title}']//following::span[contains(@class, 'MuiSwitch-switchBase') and not(contains(@class, 'Mui-checked'))][1]"

    checkbox = 'input[type="checkbox"][aria-label="controlled"]'
    payment_button = '.MuiButton-contained'
    shipping_method = "//div[contains(@class,'summary_box_item MuiBox-root')]//div[contains(text(),'איסוף ממשרדי החברה')]"
    return_checkout = None


    def __init__(self, page: Page):
        self.page = page



    def add_coupon(self, coupon_name):
        if coupon_name is None:
            return self
        coupon_fill = get_coupon(coupon_name)
        print(f"Coupon fill={coupon_fill}")
        self.page.fill(self.coupon_field, coupon_fill)
        self.page.click(self.coupon_confirm, force=True)
        self.page.locator(self.loader).wait_for(state="detached")
        try:
            self.page.get_by_role("button", name="הבנתי").click(timeout=500)
        except Exception: pass
        try:
            check = self.page.locator(self.coupon_error).inner_text(timeout=500)
            if check:
                raise Exception(f"Coupon error: {check}")
        except Exception as e:
            if "Coupon error" in str(e):
                raise
        locator = self.page.locator(self.coupon_switch.format(coupon_title=get_coupon_title(coupon_name)))
        if locator.is_visible(timeout=0):
            locator.click(timeout=0)
        return self


    def checkouts(self):
        allure.attach(body=self.page.screenshot(full_page=True), name="summary", attachment_type=allure.attachment_type.PNG)
        try:
            if self.page.locator(self.shipping_method).is_visible():
                Shipping.return_ship_method_value = 16
        except: pass
        try:
            total_discount = float(self.page.locator(self.total_discount).inner_text(timeout=1000).replace("₪", "").replace("(", "").replace(")", "").replace("-", ""))
        except: total_discount = None
        try:
            shipping_price_discount = Decimal(self.page.locator(self.shipping_price_discount).inner_text(timeout=1000).replace("₪", "").replace("(", "").replace(")", "").replace("-", ""))
        except: shipping_price_discount = Decimal(0.00)
        item_count = int(self.page.locator(self.item_count).inner_text().replace("₪", ""))
        base_price = Decimal(self.page.locator(self.base_price).inner_text().replace("₪", ""))
        shipping_price = Decimal(self.page.locator(self.shipping_price).inner_text().replace("₪", ""))
        final_price = Decimal(self.page.locator(self.final_prices).inner_text().replace("₪", ""))
        self.page.locator(self.checkbox).last.click()
        # self.page.screenshot(path="a_summary.png")
        self.page.click(self.payment_button)
        print(f"item_count={item_count}, base_price={base_price}, total_discount={total_discount}, shipping_price={shipping_price}, final_price={final_price}")
        Summary.return_checkout = [item_count, base_price, total_discount, shipping_price, shipping_price_discount, final_price]
        return self















