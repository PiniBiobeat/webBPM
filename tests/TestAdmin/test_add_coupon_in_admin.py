import pytest
import os
from tests.TestOnline.test_base_online import TestBaseOnline
from dotenv import load_dotenv
from infra.config.config_provider import configuration
from logic.pages.admin_page import AdminPage
from infra.generic_helpers import sql_get_total_order_price

user = 'pini'
passw = 'pinim1'
order_id = 14142616

class TestAdmin(TestBaseOnline):


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_coupons_pay_with_link(self):
        page: AdminPage = self.browser_online.navigate(configuration['admin_url_'+os.getenv('env')], AdminPage)
        page.log_in_admin(user, passw)
        details_url =  page.click_login_button(str(order_id))
        page.pw_page.goto(details_url)
        page.add_num_sale(2)
        page.click_open_link()
        page.get_url_from_new_page(str(order_id))
        page.pay_order()


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_coupons(self, value='50'):
        page: AdminPage = self.browser_online.navigate(configuration['coupon_manager_'+os.getenv('env')], AdminPage)
        page.log_in_admin(user, passw)
        page.input_coupon_value(value)
        page.input_email_user('pinim@lupa.co.il')
        page.choose_date()
        page.click_ok()

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_order_with_status_1_and_change_shipping(self):
        page: AdminPage = self.browser_online.navigate(configuration['admin_url_' + os.getenv('env')], AdminPage)
        page.log_in_admin(user, passw)
        details_url = page.click_login_button(str(order_id))
        page.pw_page.goto(details_url)
        page.change_shipping()
        page.click_open_link()
        page.get_url_from_new_page(str(order_id))
        get_total_pay =  page.pay_order()
        get_total_pay_sql = sql_get_total_order_price(order_id)
        assert str(get_total_pay_sql[0][0]) == get_total_pay.replace('₪', '')





