from playwright.sync_api import Page, expect

from Payment_V4.Payment_site.Pages._General_function import Generalfunction

class Summary:

    coupon_field = '.MuiInputBase-input'
    coupon_confirm = ".MuiButton-text"
    coupon_error = "//div[@class='summary_page container page MuiBox-root css-0']//p"
    coupon_value_price = "(//div[@class='content_selected_coupon MuiBox-root css-0']/div[@class='box_item_l MuiBox-root css-0'])"
    loader = ".MuiBackdrop-root css-xuaqpw"

    item_count = "(//p[text()=':סה״כ פריטים']//..//p[@class='box_itemL'])[1]"
    base_price = "(//p[text()=':מחיר מחירון']//..//p[@class='box_itemL'])[1]"
    total_discount = "(//p[text()=':הנחות נוספות']//..//p[@class='box_itemL'])[1]"
    shipping_price = "(//p[text()=':משלוח']//..//p[@class='box_itemL'])[1]"
    final_price = "//h3[text()=':סה״כ לתשלום']//..//h3[@class='box_itemL']"

    checkbox = 'input[type="checkbox"][aria-label="controlled"]'
    payment_button = "//button[text()='לתשלום']"


    def __init__(self, page: Page):
        self.page = page


    def add_coupon(self, coupon):
        self.page.fill(self.coupon_field, coupon)
        self.page.click(self.coupon_confirm)
        self.page.locator(self.loader).wait_for(state="hidden")
        try:
            self.page.get_by_role("button", name="הבנתי").click(timeout=3000)
        except: pass
        try:
            check = self.page.locator(self.coupon_error).inner_text(timeout=4000)
            if check:
                raise Exception(f"Coupon error: {check}")
        except Exception as e:
            if "Coupon error" in str(e):
                raise
        return self

    def checkouts(self):
        try:
            total_discount = float(self.page.locator(self.total_discount).inner_text().replace("₪", "").replace("(", "").replace(")", ""))
        except Exception: total_discount = 0
        item_count = int(self.page.locator(self.item_count).inner_text().replace("₪", ""))
        base_price = float(self.page.locator(self.base_price).inner_text().replace("₪", ""))
        shipping_price = float(self.page.locator(self.shipping_price).inner_text().replace("₪", ""))
        final_price = float(self.page.locator(self.final_price).inner_text().replace("₪", ""))
        self.page.locator(self.checkbox).last.click()
        # self.page.screenshot(path="a_summary.png")
        self.page.click(self.payment_button)
        print(item_count, base_price, total_discount, shipping_price, final_price)
        return self, item_count, base_price, total_discount, shipping_price, final_price

















