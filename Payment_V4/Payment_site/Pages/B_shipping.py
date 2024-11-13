from playwright.sync_api import Page, expect



class Shipping:

    asafta = "//div[@class='shipping_method']/h3[contains(text(), 'אספתא')]"
    bar_shops = "//div[@class='shipping_method']/h3[contains(text(), 'איסוף מנקודות מסירה')]"
    post_il = "//div[@class='shipping_method']/h3[contains(text(), 'דואר רשום')]"
    bar_home = "//div[@class='shipping_method']/h3[contains(text(), 'שליחות עד הבית')]"


    isof_button = "//p[contains(text(), 'מרוכזת')]"
    isof_fill = "//input[@id=':rb:']"



    def __init__(self, page: Page):
        self.page = page
