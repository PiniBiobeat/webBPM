from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.calendar_home_page import CalendarPage
from logic.pages.login_calendar_page import LoginCalendarPage
from tests.TestTiles.test_add_tiles_to_payment import TestTilesToPayment
from tests.TestOnline.test_add_book_to_payment import TestAddBookOnliToPayment
import os

email1 = 'automation@lupa.co.il'
pass1 = "a123123"
master_id = 3189204

images_base_path = "C:\\Users\\tester\\Desktop\\repositories\\pytest-lupa\\tests\\TestCalendar\\image_london\\"
#path_images = result = [f"{images_base_path} ({i}).jpg" for i in range(1, 25)]
path_images = ["./image_london/test1.jpg","./image_london/test2.jpg","./image_london/test3.jpg"]




class PaymentPagesManager(TestBase):

    def openLogin(self):
        page: CalendarPage = self.browser.navigate(configuration['calendar_url_'+os.getenv('env')], CalendarPage)
        page.open_menu()
        page.open_screen_login_from_menu()

        page: LoginCalendarPage = self.browser.create_page(LoginCalendarPage)
        page.insert_user_and_pass(email1, pass1)
        page.click_login_button()

    def choose_prod(self, num):
        match num:
            case 1:
                TestTilesToPayment.test_add_tiles_to_payment()
            case 2:
                print("You chose product 2.")
                # Add logic for product 2
                TestAddBookOnliToPayment.test_add_book_to_payment_from_mybooks_with_link()
            case _:
                print("Invalid product selection.")