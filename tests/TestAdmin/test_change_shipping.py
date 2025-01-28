import pytest
import os
from tests.TestOnline.test_base_online import TestBaseOnline
from dotenv import load_dotenv
from infra.config.config_provider import configuration
from logic.pages.admin_page import AdminPage
from infra.generic_helpers import sql_get_total_order_price,monitor_order_status,sql_get_transact_online_tbl
from logic.pages.admin_page import AdminPage

user = 'pini'
passw = 'pinim1'
order_id = 7835568

class TestChangeShipping(TestBaseOnline):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_order_with_status_PP_and_change_shipping(self):
        page: AdminPage = self.browser_online.navigate(configuration['admin_url_' + os.getenv('env')], AdminPage)
        monitor_order_status(order_id)
        page.log_in_admin(user, passw)
        details_url = page.click_login_button(str(order_id))
        page.pw_page.goto(details_url)
        page.change_shipping_printing_process()
        get_total_pay_sql = sql_get_transact_online_tbl(order_id)
        assert get_total_pay_sql == 26.00

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
        get_total_pay = page.pay_order()
        get_total_pay_sql = sql_get_total_order_price(order_id)
        assert str(get_total_pay_sql[0][0]) == get_total_pay.replace('₪', '')