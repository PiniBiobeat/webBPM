import time
import os
from infra.page_base import PageBase
from Payment_V4.Payment_site.Pages.F_thanks import Thanks
from Payment_V4.Payment_site.Pages.E_creditGuard import CreditGuard
from infra.config.config_provider import configuration
from dotenv import load_dotenv
load_dotenv()
from datetime import date
from infra.generic_helpers import monitor_order_status
from infra.generic_helpers import sql_get_total_order_price

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
    current_date = date.today()
    formatted_date = current_date.strftime("%d")
    date_new = int(formatted_date)
    text_date = f"//a[@class='ui-state-default' and contains(.,'{date_new+1}')]"
    iframe = "//div[@class='iframe_container MuiBox-root css-0']/iframe"
    credit_num = '#card-number'
    exp_year_num = '#expYear'
    exp_month_num = '#expMonth'
    cvv_num = "#cvv"
    pay = '#cg-submit-btn'
    price = '#cg-amount-sum'
    test_open_option_shipping = "//select[@id='ctl00_main_myShippmentControl_control_shipping_method']"
    text_click_ok_save = "//input[@value='SAVE']"
    text_open_link_change_shipping = "//a[@id='change_order']"
    text_shipping = "//select[@id='ddl_transact_shipment']"
    text_click_ok_change = "//span[@id='spanUpdating']//..//input[@id='btn_charge']"
    test_iframe_change_shipping = "//iframe[@id='iframe_chnage_order']"


    def __init__(self, page):
        super().__init__(page)

    def orders_status(self):
        monitor_order_status('77777777')

    def log_in_admin(self, text_user, text_pass):
        self.pw_page.locator(self.text_user_login).fill(text_user)
        self.pw_page.locator(self.test_pass_login).fill(text_pass)
        self.pw_page.click(self.text_button_login)

    def input_coupon_value(self,value):
        self.pw_page.select_option("#ctl00_main_control_coupon_name", "222383")
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
    def change_shipping_printing_process(self):
        self.pw_page.click(self.text_open_link_change_shipping)
        self.pw_page.frame_locator(self.test_iframe_change_shipping).first.locator(self.text_shipping).select_option(value="Registered")
        self.pw_page.frame_locator(self.test_iframe_change_shipping).first.locator(self.text_click_ok_change).click()
    def change_shipping(self):
        self.pw_page.locator(self.test_open_option_shipping).select_option(value="דואר רשום (30 ₪)")
        self.pw_page.click(self.text_click_ok_save)
        self.pw_page.wait_for_load_state("domcontentloaded")

    def wait_for_status_printing_prosses(self, order_id):
        monitor_order_status(order_id)

    def click_open_link(self):
        self.pw_page.once("dialog", lambda dialog: dialog.accept())

        def handle_dialog(dialog):
            # print(f"Dialog message: {dialog.message}")
            dialog.accept()

        self.pw_page.on("dialog", handle_dialog)
        with self.pw_page.context.expect_page() as new_page_info:
            self.pw_page.get_by_text("send payment link").click()
        new_page = new_page_info.value
        try:
            new_page.wait_for_load_state("domcontentloaded")  #
            # print(f"New Page URL: {new_page.url}")
        except Exception as e:
            # print(f"Error while waiting for the new page to load: {e}")
            pass
        try:
            body_locator = new_page.locator("body")
            body_locator.wait_for(state="visible", timeout=60000)
            # print("Body is visible on the new page.")
        except Exception as e:
            # print(f"Body did not become visible: {e}")
            # print(f"New Page Content:\n{new_page.content()}")
            pass

    def get_url_from_new_page(self, order_id):

        if order_id.startswith('7'):
            url = f"{configuration['admin_send_link_payment_' + os.getenv('env')]}?orderid={order_id}"
        else:
            url = f"{configuration['admin_send_link_payment_tiles_' + os.getenv('env')]}?orderid={order_id}"
        self.pw_page.goto(url, timeout=60000)
        self.pw_page.wait_for_load_state('load')
        body_locator = self.pw_page.locator("body")
        body_locator.wait_for(state="visible")
        body_text = body_locator.text_content()
        self.pw_page.goto(body_text, timeout=60000)
        self.pw_page.wait_for_load_state('load')

    def pay_order(self, card="5451365000064667", year="2030", month="01", cvv="973"):
        self.pw_page.frame_locator(self.iframe).locator(self.credit_num).wait_for(state="visible")
        self.pw_page.frame_locator(self.iframe).locator(self.credit_num).fill(card)
        self.pw_page.frame_locator(self.iframe).locator(self.exp_year_num).select_option(value=year)
        self.pw_page.frame_locator(self.iframe).locator(self.exp_month_num).select_option(value=month)
        self.pw_page.frame_locator(self.iframe).locator(self.cvv_num).fill(cvv)
        self.pw_page.frame_locator(self.iframe).locator(self.pay).click()
        a =  self.pw_page.frame_locator(self.iframe).locator("//div[@id='cg-amount-sum']").text_content()
        Thanks(self.pw_page).status()
        return a




