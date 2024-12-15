from playwright.sync_api import Page, expect
from Payment_V4.Payment_site.Pages._General_function import Generalfunction, config, os


class CreditGuard:

    iframe = "//div[@class='iframe_container MuiBox-root css-0']/iframe"
    credit_num = '#card-number'
    exp_year_num = '#expYear'
    exp_month_num = '#expMonth'
    cvv_num = "#cvv"
    pay = '#cg-submit-btn'
    price = '#cg-amount-sum'



    def __init__(self, page: Page):
        self.page = page


    def fill_credit_card(self, card="card", year="2028", month="05", cvv="684"):
        self.page.frame_locator(self.iframe).locator(self.credit_num).fill(config['GLOBAL'][card+"_"+os.getenv('env')])
        self.page.frame_locator(self.iframe).locator(self.exp_year_num).select_option(value=year)
        self.page.frame_locator(self.iframe).locator(self.exp_month_num).select_option(value=month)
        self.page.frame_locator(self.iframe).locator(self.cvv_num).fill(cvv)
        return self


    def to_pay(self):
        creditprice = float(self.page.frame_locator(self.iframe).locator(self.price).inner_text().replace("₪", ""))
        self.page.frame_locator(self.iframe).locator(self.pay).click()
        return self, creditprice






























    # option2
    # def fill_credit_card(self, card="4580110747314414", year="2028", month="05", cvv="684"):
    #     page = self.page.frame_locator(self.iframe)
    #     page.locator(self.credit_num).fill(card)
    #     page.locator(self.exp_year_num).select_option(value=year)
    #     page.locator(self.exp_month_num).select_option(value=month)
    #     page.locator(self.cvv_num).fill(cvv)
    #     return self
    #
    # def to_pay(self):
    #     page = self.page.frame_locator(self.iframe)
    #     page.locator(self.pay).click()
    #     return self