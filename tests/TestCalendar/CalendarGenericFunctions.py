import time
from logic.pages.upload_storage_images_calendar_page import UploadStorageImagesCalendar
import pytest
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.login_online_page import LogInOnline
from logic.pages.personal_date_page import PersonalDates
from logic.pages.choose_photos_device_page import ChoosePhotosDeviceCalendar
from logic.pages.choose_photos_calendar_page import ChoosePhotosCalendar
from logic.pages.calendar_home_page import CalendarPage
from logic.pages.login_calendar_page import LoginCalendarPage
from logic.pages.preview_calendar_page import PreviewCalendar
from logic.pages.choose_format_calendar_page import ChooseFormatCalendarPage
from logic.pages.settings_calendar_page import SettingsCalendarPage
from logic.pages.choose_themes_calendar_page import ThemesCalendarPage
from infra.generic_helpers import sql_get_calendar
from tests.TestCalendar.test_create_calendar import TestCreateCalendar
import os

email1 = 'pinim@lupa.co.il'
pass1 = "Pinimari!1"
master_id = 3189204

images_base_path = "C:\\Users\\tester\\Desktop\\repositories\\pytest-lupa\\tests\\TestCalendar\\image_london\\"
#path_images = result = [f"{images_base_path} ({i}).jpg" for i in range(1, 25)]
path_images = ["./image_london/test1.jpg"
     ,"./image_london/test2.jpg","./image_london/test3.jpg"]
    # ,"./image_london/shutterstock_307343513.jpg","./image_london/shutterstock_310935740.jpg"
    # ,"./image_london/shutterstock_314718617.jpg","./image_london/shutterstock_315831839.jpg"
    # ,"./image_london/shutterstock_318750242.jpg","./image_london/shutterstock_318750290.jpg"
    # ,"./image_london/shutterstock_338033549.jpg","./image_london/shutterstock_369746171.jpg"
    # ,"./image_london/shutterstock_407506189.jpg"]
    # , "./image_london/shutterstock_409552375.jpg", "./image_london/shutterstock_422969926.jpg"
    # , "./image_london/shutterstock_422970067.jpg", "./image_london/shutterstock_425742643.jpg"
    # , "./image_london/shutterstock_428941816.jpg", "./image_london/shutterstock_445141507.jpg"
    # , "./image_london/shutterstock_448948483.jpg", "./image_london/shutterstock_473627458.jpg"
    # , "./image_london/shutterstock_499513999.jpg", "./image_london/shutterstock_502044016.jpg"
    # , "./image_london/shutterstock_504251206.jpg"]



class CalendarPagesManager(TestBase):

    def openLogin(self):
        page: CalendarPage = self.browser.navigate(configuration['calendar_url_'+os.getenv('env')], CalendarPage)
        page.open_menu()
        page.open_screen_login_from_menu()

        page: LoginCalendarPage = self.browser.create_page(LoginCalendarPage)
        page.insert_user_and_pass(email1, pass1)
        page.click_login_button()

    def setFormat(self):
        page: ChooseFormatCalendarPage = self.browser.create_page(ChooseFormatCalendarPage)
        page.getSelectorElement(92)

    def setSettings(self, name):
        page: SettingsCalendarPage = self.browser.create_page(SettingsCalendarPage)
        page.insert_name_calendar(name)
        page.click_button_next()

    def setThemes(self):
        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        page.click_shoose_themes()
        page.click_next_on_theme()

    def setThemeWhite(self):
        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        page.click_shoose_themes_white()
        page.click_next_on_theme()
    def get_token(self):
        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        token_after_calendar = page.take_token_calendar_after_login()
        calendar_data = sql_get_calendar(token_after_calendar)
        return calendar_data
    def get_calendar_theme(self):
        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        token_after_calendar = page.take_token_calendar_API()
        return token_after_calendar


    def setPersonalDates(self):
        page: PersonalDates = self.browser.create_page(PersonalDates)
        page.click_next()
        #page.pw_page.wait_for_url("**/preview")

    def setPhotos(self):
        page: ChoosePhotosCalendar = self.browser.create_page(ChoosePhotosCalendar)
        page.add_photos_from_local(path_images)
        page.click_next_after_choose_photos()
        page.checkbox_approval_regulations()
        page.click_next_after_checkbox()

    def changeChooseThemes(self):
        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.click_X()
        page.click_change_themes()
    def createPreview(self):
        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.click_edit_page()

    def link_add_images_after(self):
        page: ChoosePhotosCalendar = self.browser.create_page(ChoosePhotosCalendar)
        page.click_link_add_images_after()
        page.do_reload()

    def choose_layout(self, month):
        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.click_open_laout(month)

    def click_x_to_next(self):
        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.click_X()
    def get_locaors_plus(self):
        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        return page.get_locator_plus()

    def click_plus_to_add_photos(self):
        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.click_plus_to_add_images()

    def choose_image_from_storage(self):
        page: UploadStorageImagesCalendar = self.browser.create_page(UploadStorageImagesCalendar)
        page.click_first_image()
        #page.click_save_image()
        page.click_save_image_in_storage()

    def click_to_checkout(self):
        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.next_to_checkout()
        page.click_checkbox_accsept()
        page.click_ok_accsept()




    def wait_for_payments(self):
        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.pw_page.wait_for_url("https://paymentsv4-ui.lupa.co/")

    def choose_month(self, month):
        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.click_choose_month_(month)

    def changeThemes(self):
        pass

    def changeCalendarName(self, name):
        pass



    def executeSquence(self, pointers):
        if len(pointers) != 0:
            for p in pointers:
                p()