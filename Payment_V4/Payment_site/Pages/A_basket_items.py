from playwright.sync_api import Page




class BasketItems:
    count_item_conatiner = "//div[@class='basket_item_container MuiBox-root css-0']"
    plus_items_button = "(//button[contains(text(), '+')])"
    minus_items_button = "(//button[contains(text(), '-')])"
    select_item_button = "//input[@class='PrivateSwitchBase-input css-1m9pwf3']"
    delete_button = "//div[@class='count_selected_items_and_icon MuiBox-root css-0']/img"

    def __init__(self, page: Page):
        self.page = page


