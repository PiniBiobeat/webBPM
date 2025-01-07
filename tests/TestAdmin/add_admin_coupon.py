import pytest
import os
from playwright.sync_api import Page
from Payment_V4.Payment_site.Pages.F_thanks import Thanks
from infra.config.config_provider import configuration
from logic.pages.admin_page import AdminPage

user = 'pini'
passw = 'pinim1'





class AdminCoupon:

    def add_admin_discount(self, page):
        order_id = Thanks.status
        page: AdminPage = AdminPage(page)
        page.pw_page.goto(configuration['admin_url_prod'])
        page.log_in_admin(user, passw)
        details_url = page.click_login_button(str(order_id))
        page.pw_page.goto(details_url)
        page.add_num_sale(2)
        page.click_open_link()
        page.get_url_from_new_page(str(order_id))


    def add_coupon_manual(self, page):
        page: AdminPage = AdminPage(page)
        page.pw_page.goto(configuration['admin_url_prod'])
        page.log_in_admin(user, passw)
        page.pw_page.goto('https://admin.lupa.co.il/admin_tiles/couponFromMaster.aspx')
        page.input_coupon_value('118')
        page.input_email_user('pinim@lupa.co.il')
        page.choose_date()
        page.click_ok()


# class TestTest:
#     def testadmin(self, page: Page):
#         AdminCoupon().add_admin_discount(page)
#         AdminCoupon().add_coupon_manual(page)
