from playwright.sync_api import Page, expect

from Payment_V4.Payment_site.Pages._General_function import Generalfunction

class Summary:

    coupon_field = '.MuiInputBase-input'
    coupon_confirm = ".MuiButton-text"
    coupon_error = "//div[@class='summary_page container page MuiBox-root css-0']/div//p"
    coupon_value_price = "(//div[@class='content_selected_coupon MuiBox-root css-0']/div[@class='box_item_l MuiBox-root css-0'])"

    loader = ".MuiBackdrop-root css-xuaqpw"


    def __init__(self, page: Page):
        self.page = page





    def add_coupon(self, coupon):
        self.page.fill(self.coupon_field, coupon)
        self.page.click(self.coupon_confirm)

        self.page.locator(self.loader).wait_for(state="hidden")
        try:
            check = self.page.locator(self.coupon_error).inner_text(timeout=1000)
            if check:
                raise Exception(f"Coupon error: {check}")
        except Exception as e:
            if "Coupon error" in str(e):
                raise





















