from playwright.sync_api import Page, expect
from Payment_V4.Payment_site.Pages._General_function import Generalfunction


class BasketItems:
    count_item_conatiner = "//div[@class='basket_item_container MuiBox-root css-0']"
    plus_items_button = "(//button[contains(text(), '+')])"
    minus_items_button = "(//button[contains(text(), '-')])"
    select_item_button = "//input[@class='PrivateSwitchBase-input css-1m9pwf3']"
    delete_button = "//div[@class='count_selected_items_and_icon MuiBox-root css-0']/img"
    image_src = "(//button/img)"

    sale_price = "(//div[@class='color_green MuiBox-root css-gg4vpm'])/div[2]"


    def __init__(self, page: Page):
        self.page = page


    def valid_element_click_next(self):
        self.page.locator("text=מחיר מחירון").first.wait_for(state="visible")
        try:
            prices = self.page.locator(self.sale_price)
            total_sum = 0
            price_count = prices.count()
            for i in range(price_count):
                price_text = prices.nth(i).inner_text()
                price_text = price_text.replace("₪", "").replace("(", "").replace(")", "").replace("-", "").strip()
                price = float(price_text)
                total_sum += price
            print(f"Total Sale sum: {total_sum} ₪")
            print(f"Total Sale item: {prices.count()}")
        except Exception: pass
        Generalfunction(self.page).next_button()


    def update_item_quantity(self, item_index: int, button: str, times: int):
        button_selector = self.plus_items_button if button == "+" else self.minus_items_button
        item_button = f"{button_selector}[{item_index}]"
        for _ in range(times):
            self.page.click(item_button)


    def delete_all_items(self):
        self.page.locator(self.select_item_button).nth(0).click()
        self.page.locator(self.select_item_button).first.check()
        self.page.locator(self.delete_button).click()
        self.page.get_by_role("button", name="כן").click()
        expect(self.page.get_by_role("heading")).to_contain_text("הסל שלך ריק בינתיים")
