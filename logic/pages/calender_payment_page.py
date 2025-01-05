from infra.page_base import PageBase

class CalenderPaymentPage(PageBase):


    text_open_my_calender = '//span[contains(.,"לוחות השנה שלי")]'
    text_checkbox = "//input[@class='PrivateSwitchBase-input css-1m9pwf3']"
    icon_delete = "//img[@class='delete_icon_white MuiBox-root css-0']"
    pupa_yes_delete = "//button[@class='MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root  css-swbn5f']"

    def __init__(self, page):
        super().__init__(page)


    def delete_from_basket(self):
        self.pw_page.click(self.text_checkbox)
        self.pw_page.click(self.icon_delete)
        self.pw_page.click(self.pupa_yes_delete)

    def get_url(self):
        # Get the current URL
        current_url = self.pw_page.url
        return current_url