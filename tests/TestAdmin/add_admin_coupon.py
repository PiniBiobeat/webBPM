import pytest
import os
from playwright.sync_api import Page
from Payment_V4.Payment_site.Pages.F_thanks import Thanks
from infra.config.config_provider import configuration
from logic.pages.admin_page import AdminPage

user = 'ofir'
passw = 'of2023'


class AdminCoupon:

    def add_admin_discount(self, page):
        order_id = Thanks.status
        page: AdminPage = AdminPage(page)
        page.pw_page.goto(configuration['admin_url_' + os.getenv('env')])
        page.log_in_admin(user, passw)
        details_url =  page.click_login_button(str(order_id))
        page.pw_page.goto(details_url)
        page.add_num_sale(2)
        page.click_open_link()
        page.get_url_from_new_page(str(order_id))
        page.pay_order()


    def add_coupon_manual(self, page, value='50'):
        page: AdminPage = AdminPage(page)
        page.pw_page.goto(configuration['coupon_manager_'+os.getenv('env')])
        page.log_in_admin(user, passw)
        page.input_coupon_value(value)
        page.input_email_user('automation@lupa.co.il')
        page.choose_date()
        page.click_ok()
