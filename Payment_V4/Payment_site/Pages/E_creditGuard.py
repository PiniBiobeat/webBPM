from playwright.sync_api import Page, expect
from Payment_V4.Payment_site.Pages._General_function import Generalfunction


class CreditGuard:

    iframe_selector = "//div[@class='iframe_container MuiBox-root css-0']/iframe"
    credit_num = '#card-number'
    exp_year_num = '#expYear'
    exp_month_num = '#expMonth'
    cvv_num = "#cvv"
    pay = '#cg-submit-btn'

    def __init__(self, page: Page):
        self.page = page

    def fill_credit_card(self, card="4580110747314414", year="2028", month="05", cvv="684"):
        iframe = self.page.frame_locator(self.iframe_selector)
        iframe.locator(self.credit_num).fill(card)
        iframe.locator(self.exp_year_num).select_option(value=year)
        iframe.locator(self.exp_month_num).select_option(value=month)
        iframe.locator(self.cvv_num).fill(cvv)
        return self

    def to_pay(self):
        iframe = self.page.frame_locator(self.iframe_selector)
        iframe.locator(self.pay).click()
        return self





    # def fill_credit_card(self, card="4580458045804580", year="2028", month="08", cvv="684"):
    #     self.page.fill(self.credit_num, card)
    #     self.page.select_option(self.exp_year_num, value=year)
    #     self.page.select_option(self.exp_month_num, value=month)
    #     self.page.fill(self.cvv_num, cvv)
    #     return self
    #
    # def to_pay(self):
    #     self.page.click(self.pay)
    #     return self