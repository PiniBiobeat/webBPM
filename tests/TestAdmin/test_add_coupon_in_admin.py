import pytest
import os
from tests.TestOnline.test_base_online import TestBaseOnline
from dotenv import load_dotenv
from infra.config.config_provider import configuration
from logic.pages.admin_page import AdminPage
user = 'pini'
passw = 'pinim1'
order_id = 7827943

class TestAdmin(TestBaseOnline):


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_coupons_pay_with_link(self):
        page: AdminPage = self.browser_online.navigate(configuration['admin_url_prod'], AdminPage)
        page.log_in_admin(user, passw)
        details_url =  page.click_login_button(str(order_id))
        page.pw_page.goto(details_url)
        page.add_num_sale(2)
        page.click_open_link()
        page.get_url_from_new_page(str(order_id))
        page.pay_order()


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_coupons(self):
        page: AdminPage = self.browser_online.navigate(configuration['admin_url_prod'], AdminPage)
        page.log_in_admin(user, passw)
        page.pw_page.goto('https://admin.lupa.co.il/admin_tiles/couponFromMaster.aspx')
        page.input_coupon_value('118')
        page.input_email_user('pinim@lupa.co.il')
        page.choose_date()
        page.click_ok()




