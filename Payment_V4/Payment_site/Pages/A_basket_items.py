import time
import allure
from decimal import Decimal
from playwright.sync_api import Page, expect
from Payment_V4.Payment_site.Pages._General_function import Generalfunction
from Payment_V4.Logic.Logic_Orders.data_order import DataPriceList


class BasketItems:
    count_item_conatiner = "(//div[@class='basket_item_container MuiBox-root css-0'])"
    plus_items_button = "(//button[contains(text(), '+')])"
    minus_items_button = "(//button[contains(text(), '-')])"
    select_item_button = "//input[@class='PrivateSwitchBase-input css-1m9pwf3']"
    delete_button = "//div[@class='count_selected_items_and_icon MuiBox-root css-0']/img"
    image_src = "(//button/img)"

    replacements = str.maketrans({"₪": "", "(": "", ")": "", "-": "", ",": ""})
    sale_price = "(//div[@class='color_green MuiBox-root css-gg4vpm'])/div[2]"
    quantity_discount_price = "(//p[text()=':הנחת כמות']//..//p[@class='box_itemL'])[1]"
    element_base_price = "(//p[text()=':מחיר מחירון']//..//p[@class='box_itemL'])[1]"

    return_sale_element = None
    return_quantity_discount = None
    return_base_price = None


    def __init__(self, page: Page):
        self.page = page


    def valid_element_click_next(self):
        BasketItems.return_base_price = Decimal(self.page.locator(self.element_base_price).inner_text().translate(self.replacements))
        allure.attach(body=self.page.screenshot(full_page=True), name="basket",attachment_type=allure.attachment_type.PNG)
        DataPriceList().check_price_list(BasketItems.return_base_price)
        self.page.locator("text=מחיר מחירון").first.wait_for(state="visible")
        try:
            sale_item = self.page.locator(self.sale_price)
            sale_price = 0
            price_count = sale_item.count()
            for i in range(price_count):
                price_text = sale_item.nth(i).inner_text()
                price_text = price_text.translate(self.replacements).strip()
                price = float(price_text)
                sale_price += price
            if price_count > 0:
                sale_items = sale_item.count()
                print(f"Total Sale sum: {sale_price} ₪")
                print(f"Total Sale item: {sale_items}")
                BasketItems.return_sale_element = (sale_price, sale_items)
            else:
                BasketItems.return_sale_element = (0, 0)
            return self
        except Exception as e:
            print(f"error sale: {e}")
        finally:
            Generalfunction(self.page).next_button()


    def update_item_quantity(self, item_index: int, button: str, times: int):
        button_selector = self.plus_items_button if button == "+" else self.minus_items_button
        item_button = f"{button_selector}[{item_index}]"
        for _ in range(times):
            self.page.click(item_button)
            time.sleep(0.3)
        time.sleep(0.5)


    def get_quantity_discount(self):
        quantity_discount = Decimal(self.page.locator(self.quantity_discount_price).inner_text().translate(self.replacements))
        BasketItems.return_quantity_discount = quantity_discount
        return self


    def delete_all_items(self):
        self.page.locator(self.select_item_button).nth(0).click()
        self.page.locator(self.select_item_button).first.check()
        self.page.locator(self.delete_button).click()
        self.page.get_by_role("button", name="כן").click()
        self.page.locator('[class*="MuiCircularProgress-circle"]').wait_for(state="detached")
        expect(self.page.get_by_role("heading")).to_contain_text("הסל שלך ריק בינתיים")


    # container_xpath = '(//*[@class="basket_item_container MuiBox-root css-0"])'


    def change_format(self, item_index: int, change_format_to: str):
        format_button = self.page.locator(f'({self.count_item_conatiner}[{item_index}]//*[@aria-haspopup="listbox"])[1]')
        format_button.click()
        self.page.locator('//ul[@role="listbox"]//li').filter(has_text=change_format_to).click()
        return self


    def change_cover(self, item_index: int, change_cover_to: str):
        cover_button = self.page.locator(f'({self.count_item_conatiner}[{item_index}]//*[@aria-haspopup="listbox"])[2]')
        cover_button.click()
        self.page.locator('//ul[@role="listbox"]//li').filter(has_text=change_cover_to).click()
        return self