import pytest
import os
from tests.TestOnline.test_base_online import TestBaseOnline
from dotenv import load_dotenv
from infra.config.config_provider import configuration
from logic.pages.admin_page import AdminPage
user = 'pini'
passw = 'pinim1'


class TestAdmin(TestBaseOnline):


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_coupons(self):
        page: AdminPage = self.browser_online.navigate(configuration['admin_url_prod'], AdminPage)
        page.log_in_admin(user, passw)
        details_url =  page.click_login_button()
        page.pw_page.goto(details_url)
        #self.browser_online.get(details_url)
        page.add_num_sale(2)
        page.select_option()
        page.click_ok()
        page.click_open_link()
        page.get_url_from_new_page()
        page.pay_order()
        print("")



