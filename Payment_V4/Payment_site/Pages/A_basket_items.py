from playwright.sync_api import Page, expect
from Payment_V4.Payment_site.Pages._General_function import Generalfunction


class BasketItems:
    count_item_conatiner = "//div[@class='basket_item_container MuiBox-root css-0']"
    plus_items_button = "(//button[contains(text(), '+')])"
    minus_items_button = "(//button[contains(text(), '-')])"
    select_item_button = "//input[@class='PrivateSwitchBase-input css-1m9pwf3']"
    delete_button = "//div[@class='count_selected_items_and_icon MuiBox-root css-0']/img"
    image_src = "(//button/img)"


    def __init__(self, page: Page):
        self.page = page


    def valid_image_item(self):
        link = "https://paymentsv4-api.lupa.co.il/ImageBasket.aspx?order_id=7816706&token=fPon5DahDbeWopYCcxzXTnAGVt0aeH2JDwVIhEy5DeOu1HlPZr-OOMCkYIIBndkzP5Dyehgr8S6nzvsQ1NkaxqvhIX7wD4SV09trsj28fg8RO44luwaemoCav5F2T6NHZpJL1RqF5XckCOVlxMFBs0IP00a1sv0X840kgB2Xv5dVT0RPdkZ7YrUtubY5rSupBUUQ9X6hhgwJpzMxRrPmARybNbkpGld7uvx9tb8FsVIxk279kv0SCjKM0Q0UEUnj5wVEyEE9KMikQuK1vDUrFIeAnJSkaMWCcvdq02L8Tp4vkv9xhr9h-H4TQQ2R_pGuAL_PUc4l_e78t0QDQaACCQ2&project_tick=241125094640183-9"
        expect(self.page.locator(self.image_src).first).not_to_have_attribute("src", link)
        Generalfunction(self.page).next_button()


    def delete_all_items(self):
        self.page.locator(self.select_item_button).nth(0).click()
        self.page.locator(self.select_item_button).first.check()
        self.page.locator(self.delete_button).click()
        self.page.get_by_role("button", name="כן").click()
        expect(self.page.get_by_role("heading")).to_contain_text("הסל שלך ריק בינתיים")


    def update_item_quantity(self, item_index: int, button: str, times: int):
        button_selector = self.plus_items_button if button == "+" else self.minus_items_button
        item_button = f"{button_selector}[{item_index}]"
        for _ in range(times):
            self.page.click(item_button)
