from playwright.sync_api import Page, expect
from Payment_V4.Payment_site.Pages._General_function import Generalfunction, config, os


class Thanks:


    order_status_msg = "(//h3)[1]"
    order_number_msg = "(//h3)[3]"


    def __init__(self, page: Page):
        self.page = page


    def thank_page_status(self):
        thank_msg = self.page.locator(self.order_status_msg).inner_text()
        if thank_msg == "תודה שעשית את שלך, עכשיו התור שלנו":
            pass
        else:
            raise Exception("Charge failed")


    def status(self):
        self.thank_page_status()
        try:
            order_number = self.page.locator(self.order_number_msg).inner_text()
            print(order_number)
            return order_number
        except:
            print("phone order")
