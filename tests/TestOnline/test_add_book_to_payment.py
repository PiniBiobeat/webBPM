# import time
#
# import pytest
# from logic.pages.choose_format_cover_page import ChooseFormatCoverPage
# from tests.TestOnline.test_base_online import TestBaseOnline
# from infra.config.config_provider import configuration
# from logic.pages.login_online_page import LogInOnline
# from infra.generic_helpers import generate_random_email_and_password
# from logic.pages.connect_create_user_page import ConnectCreateUserPage
#
# text_user_name_instagram = "pinitesttiles"
# text_password_instagram = "Pinimari2020!"
# text_googleUserName="lupadevtest@gmail.com"
# text_googlePassword="lupadevtest!128"
# Short_name = "B"
# name_book =  "Book Automation"
# firt_name = "פיני"
# last_name = "mari"
# rand_email = generate_random_email_and_password()
# email =  rand_email["email"]
# password = rand_email["password"]
# num_and_pass =  password + "1"+ "!"
# email1 = 'automation@lupa.co.il'
# num_phone = '0537608055'
# firt_name1 = "פיני1"
# last_name1 = "mari1"
# email2 = "pinilupa.co.il"
# pass1 = "a123123"
# pass_not_same = "pinim123"
#
#
#
# class TestAddBookOnliToPayment(TestBaseOnline):
#
#
#
#     @pytest.mark.smoke
#     @pytest.mark.usefixtures("before_after_test")
#     def test_add_book_to_payment_from_mybooks_with_link(self):
#         page: ConnectCreateUserPage = self.browser_online.navigate(configuration['my_book_url_prod'], ConnectCreateUserPage)
#         page.click_add_book_to_payment()
#
#
#     @pytest.mark.smoke
#     @pytest.mark.usefixtures("before_after_test")
#     def test_add_book_to_payment_from_mybooks(self):
#         page: ConnectCreateUserPage = self.browser_online.navigate(configuration['online_url_prod'], ConnectCreateUserPage)
#         page.click_icon_user()
#         page.click_connect_user()
#
#         page: LogInOnline = self.browser_online.create_page(LogInOnline)
#         page.insert_user_and_pass(email1, pass1)
#         page.click_login_button()
#
#         page: ConnectCreateUserPage = self.browser_online.create_page(ConnectCreateUserPage)
#         page.click_my_book_name()
#         page.wait_for_mybooks()
#         page.click_add_book_to_payment()


class AddBookOnline:
    token = {
        "אלבום ספר אונליין לבדיקות קופה": "9ec661a662bf4f4fbe883c6712e8d56b",
    }

    def api_request_for_add_book_online(self, page, album_name):
        token = self.token.get(album_name)
        response = page.context.request.post(
            f"https://paymentsv4-api.lupa.co.il/api.aspx?token=UMcuQ9PnpUS41iHamIcZCzMaT7kN_nKIbc3xMfusOrwjKNEyiHQvWNp2v8kfeSwfboinkFTJk5iJKxVwi5i4sLKCHM38NRQClnaD-Dd3CnFkc20udFcXRIO14trI4gwD8piuGl-uliMWXaC8I8I2abYj6g-QWs3By72KcfcYJzWmkrEsAhu9jRtk_SAZyQHyYmmczYEKTgXD0ZS0VDqiM7PgpLRaFO7p1vK1_i5VMVlQilE52p04XRAC-QrdhI8SUe6aOCTh-3sOV7okZRUlGGPTTOeHH3HyXck8gtTMQBe5FvZ0DFx-EfEg3s7L37ljCtJ-oWL9pkqvVCgYZUhfVg2&event_token={token}&device_type=web&lang=he&method=add_basket&format=35&cover_type=0&page_type=0&quantity=1&source_type=books&source_device=mobile")
        assert response.ok
        assert response.status == 200


class TestAddBookOnline:
    def test_api_request_online(self, page):
        AddBookOnline().api_request_for_add_book_online(page,"אלבום ספר אונליין לבדיקות קופה")