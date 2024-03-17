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
import random
import json

r1 = random.randint(1, 1000)
email1 = 'pinim@lupa.co.il'
pass1 = "Pinimari!1"
master_id = 3189204
path_images = ["./shutterstock_315831767.jpg"]


class TestCreateCalendar(TestBase):
    testdata = [
        (1, 2, 'Diamonds'),
        (2, 1, 'Diamonds'),
    ]

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    @pytest.mark.parametrize("eFrom, eTo", [(92, 240), (240, 260)])
    def test_executeTest(self, eFrom, eTo):
        page: CalendarPage = self.browser.navigate(configuration['calendar_url'], CalendarPage)
        page.open_menu()
        page.open_screen_login_from_menu()

        page: LoginCalendarPage = self.browser.create_page(LoginCalendarPage)
        page.insert_user_and_pass(email1, pass1)
        page.click_login_button()

        page: ChooseFormatCalendarPage = self.browser.create_page(ChooseFormatCalendarPage)
        page.getSelectorElement(eFrom)

        page: SettingsCalendarPage = self.browser.create_page(SettingsCalendarPage)
        page.insert_name_calendar("calendar A5_" + str(r1))
        page.click_button_next()

        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        page.click_shoose_themes()
        page.click_next_on_theme()

        page: PersonalDates = self.browser.create_page(PersonalDates)
        page.click_next()

        page: ChoosePhotosCalendar = self.browser.create_page(ChoosePhotosCalendar)
        page.add_photos_from_local(path_images)

        page: ChoosePhotosDeviceCalendar = self.browser.create_page(ChoosePhotosDeviceCalendar)
        page.click_next_after_choose_photos()
        page.checkbox_approval_regulations()
        page.click_next_after_checkbox()

        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.click_edit_page()

        page: ChooseFormatCalendarPage = self.browser.create_page(ChooseFormatCalendarPage)
        page.getSelectorElement(eTo)

        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        token_after_calendar = page.take_token_calendar()
        calendar_data = sql_get_calendar(token_after_calendar)
        # assert expected == calendar_data[0][1]

        if calendar_data[0][0] != eTo:
            # error
            assert "Error"
        else:
            # database update correctly!
            assert "Success"

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    @pytest.mark.parametrize("a,b,expected", testdata)
    def test_change_format_calendar(self, a, b, expected):

        page: CalendarPage = self.browser.navigate(configuration['calendar_url'], CalendarPage)
        page.open_menu()
        page.open_screen_login_from_menu()

        page: LoginCalendarPage = self.browser.create_page(LoginCalendarPage)
        page.insert_user_and_pass(email1, pass1)
        page.click_login_button()

        page: ChooseFormatCalendarPage = self.browser.create_page(ChooseFormatCalendarPage)
        page.click_choose_A5(a)

        page: SettingsCalendarPage = self.browser.create_page(SettingsCalendarPage)
        page.insert_name_calendar("calendar A5_" + str(r1))
        page.click_button_next()

        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        page.click_shoose_themes()
        page.click_next_on_theme()

        page: PersonalDates = self.browser.create_page(PersonalDates)
        page.click_next()

        page: ChoosePhotosCalendar = self.browser.create_page(ChoosePhotosCalendar)
        page.add_photos_from_local(path_images)

        page: ChoosePhotosDeviceCalendar = self.browser.create_page(ChoosePhotosDeviceCalendar)
        page.click_next_after_choose_photos()
        page.checkbox_approval_regulations()
        page.click_next_after_checkbox()

        page: PreviewCalendar = self.browser.create_page(PreviewCalendar)
        page.click_edit_page()

        page: ChooseFormatCalendarPage = self.browser.create_page(ChooseFormatCalendarPage)
        page.click_choose_A3(b)

        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        token_after_calendar = page.take_token_calendar()
        calendar_data = sql_get_calendar(token_after_calendar)
        assert expected == calendar_data[0][1]

        if a == 1:

            assert 240 == calendar_data[0][0]
        else:
            assert 92 == calendar_data[0][0]
