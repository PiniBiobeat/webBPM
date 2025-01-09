import time
import os
from infra.page_base import PageBase
from Payment_V4.Payment_site.Pages.F_thanks import Thanks
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from infra.config.config_provider import configuration
from dotenv import load_dotenv
load_dotenv()

class AdminPage(PageBase):

    init_indication = "(//button[@type='button'])[2]"
    text_user_login = "//input[@id='ctl00_ContentPlaceHolder2_txtUserName']"
    test_pass_login = "//input[@id='ctl00_ContentPlaceHolder2_txtPassword']"
    text_button_login = "//input[@name='ctl00$ContentPlaceHolder2$btnLogin']"
    text_num_coupons = "//input[@id='couponAmount']"
    test_open_option = "//select[@id='couponReason']"
    text_click_ok = "//input[@id='btnAddAdminCoupon']"
    text_open_link = "//div[@onclick='sentPaymentLink()' and contains(.,'send payment link')]"
    text_coupon_value = "//input[@id='ctl00_main_couponValueTextBox']"
    text_click_ok1= "//input[@id='ctl00_main_CreateButton']"
    text_email_user = "//input[@id='ctl00_main_couponEmailTextBox']"
    text_choose_date = "//input[@id='ctl00_main_couponEndDateTextBox']"
    text_date = "//a[@class='ui-state-default' and contains(.,'10')]"
    iframe = "//div[@class='iframe_container MuiBox-root css-0']/iframe"
    credit_num = '#card-number'
    exp_year_num = '#expYear'
    exp_month_num = '#expMonth'
    cvv_num = "#cvv"
    pay = '#cg-submit-btn'
    price = '#cg-amount-sum'
    def __init__(self, page):
        super().__init__(page)


    def log_in_admin(self, text_user, text_pass):
        self.pw_page.locator(self.text_user_login).fill(text_user)
        self.pw_page.locator(self.test_pass_login).fill(text_pass)
        self.pw_page.click(self.text_button_login)

    def input_coupon_value(self,value):
        self.pw_page.locator(self.text_coupon_value).fill(value)


    def input_email_user(self,user):
        self.pw_page.locator(self.text_email_user).fill(user)


    def choose_date(self):
        self.pw_page.click(self.text_choose_date)
        self.pw_page.click(self.text_date)

    def click_ok(self):
        self.pw_page.click(self.text_click_ok1)
    def click_login_button(self,order_id):

        if order_id.startswith('7'):  # Check if the order_id starts with '7'
            details_url = self.pw_page.url.replace("order_list.aspx", f"Order_Details.aspx?id={order_id}")
        else:
            # Handle the case where order_id does not start with '7'
            details_url = self.pw_page.url.replace("admin_online/order_list.aspx",
                                                   f"admin_tiles/Order_Details.aspx?id={order_id}")

        return details_url
    def add_num_sale(self, num_coupons):
        self.pw_page.locator(self.text_num_coupons).fill(str(num_coupons))
        self.pw_page.locator(self.test_open_option).select_option(value="הטבה שירותית")
        self.pw_page.click(self.text_click_ok)

    def click_open_link(self):
        # Set up dialog handling
        self.pw_page.once("dialog", lambda dialog: dialog.accept())

        def handle_dialog(dialog):
            print(f"Dialog message: {dialog.message}")
            dialog.accept()  # Accept the dialog
            # dialog.dismiss()  # Use this if you need to cancel the dialog

        self.pw_page.on("dialog", handle_dialog)

        # Trigger the action that opens a new page
        with self.pw_page.context.expect_page() as new_page_info:
            self.pw_page.get_by_text("send payment link").click()

        # Get the new page object
        new_page = new_page_info.value

        # Wait for the new page to load fully
        try:
            new_page.wait_for_load_state("domcontentloaded")  # Wait for the DOM to be loaded
            print(f"New Page URL: {new_page.url}")  # Debug: Print the URL of the new page
        except Exception as e:
            print(f"Error while waiting for the new page to load: {e}")

        # Wait for a more specific element instead of <body>
        try:
            body_locator = new_page.locator("body")
            body_locator.wait_for(state="visible", timeout=30000)  # Increase timeout if necessary
            print("Body is visible on the new page.")
        except Exception as e:
            print(f"Body did not become visible: {e}")
            print(f"New Page Content:\n{new_page.content()}")  # Debug: Print page content

        # Return the new page object for further interactions if needed

    def get_url_from_new_page(self, order_id):

        if order_id.startswith('7'):
            url = f"{configuration['admin_send_link_payment_' + os.getenv('env')]}?orderid={order_id}"
        else:
            url = f"{configuration['admin_send_link_payment_' + os.getenv('env')]}?orderid={order_id}"
        self.pw_page.goto(url)
        self.pw_page.wait_for_load_state()
        body_locator = self.pw_page.locator("body")
        body_locator.wait_for(state="visible")
        body_text = body_locator.text_content()
        self.pw_page.goto(body_text)


    def pay_order(self, card="5451365000064667", year="2030", month="01", cvv="973"):
        self.pw_page.frame_locator(self.iframe).locator(self.credit_num).wait_for(state="visible")
        self.pw_page.frame_locator(self.iframe).locator(self.credit_num).fill(card)
        self.pw_page.frame_locator(self.iframe).locator(self.exp_year_num).select_option(value=year)
        self.pw_page.frame_locator(self.iframe).locator(self.exp_month_num).select_option(value=month)
        self.pw_page.frame_locator(self.iframe).locator(self.cvv_num).fill(cvv)
        self.pw_page.frame_locator(self.iframe).locator(self.pay).click()
        Thanks(self.pw_page).status()




