import os
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

import pytest
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.login_online_page import LogInOnline
from logic.pages.calendar_home_page import CalendarPage
from logic.pages.login_calendar_page import LoginCalendarPage
from logic.pages.choose_format_calendar_page import ChooseFormatCalendarPage
from logic.pages.settings_calendar_page import SettingsCalendarPage
from logic.pages.choose_themes_calendar_page import ThemesCalendarPage
from infra.generic_helpers import sql_get_calendar,sql_get_path_calendar
import random
import json
load_dotenv()
r1 = random.randint(1, 1000)
email1 = 'pinim@lupa.co.il'
pass1 = "Pinimari!1"
master_id = 3189204


class TestCreateCalendar(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_create_calendar_and_check_in_DB_A5_and_Diamonds(self):

        page: CalendarPage = self.browser.navigate(configuration['calendar_url_'+os.getenv('env')], CalendarPage)
        page.open_menu()
        page.open_screen_login_from_menu()

        page: LoginCalendarPage = self.browser.create_page(LoginCalendarPage)
        page.insert_user_and_pass(email1, pass1)
        page.click_login_button()

        page: ChooseFormatCalendarPage = self.browser.create_page(ChooseFormatCalendarPage)
        page.click_choose_A5()

        page: SettingsCalendarPage = self.browser.create_page(SettingsCalendarPage)
        page.insert_name_calendar("calendar A5_" + str(r1))
        page.click_button_next()

        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        page.click_shoose_themes()
        page.click_next_on_theme()
        token_after_calendar = page.take_token_calendar()
        calendar_data = sql_get_calendar(token_after_calendar)
        assert 'Diamonds' == calendar_data[0][1]
        assert 92 == calendar_data[0][0]

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_create_calendar_and_check_in_DB_A4_and_Diamonds(self):
        page: CalendarPage = self.browser.navigate(configuration['calendar_url_'+os.getenv('env')], CalendarPage)
        page.open_menu()
        page.open_screen_login_from_menu()

        page: LoginCalendarPage = self.browser.create_page(LoginCalendarPage)
        page.insert_user_and_pass(email1, pass1)
        page.click_login_button()

        page: ChooseFormatCalendarPage = self.browser.create_page(ChooseFormatCalendarPage)
        page.click_choose_A4()

        page: SettingsCalendarPage = self.browser.create_page(SettingsCalendarPage)
        page.insert_name_calendar("calendar A4_" + str(r1))
        page.click_button_next()

        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        page.click_shoose_themes()
        page.click_next_on_theme()
        token_after_calendar = page.take_token_calendar()
        calendar_data = sql_get_calendar(token_after_calendar)
        assert 'Diamonds' == calendar_data[0][1]
        assert 240 == calendar_data[0][0]

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_create_calendar_and_check_in_DB_A3_and_Diamonds(self):
        page: CalendarPage = self.browser.navigate(configuration['calendar_url_'+os.getenv('env')], CalendarPage)
        page.open_menu()
        page.open_screen_login_from_menu()

        page: LoginCalendarPage = self.browser.create_page(LoginCalendarPage)
        page.insert_user_and_pass(email1, pass1)
        page.click_login_button()

        page: ChooseFormatCalendarPage = self.browser.create_page(ChooseFormatCalendarPage)
        page.click_choose_A3()

        page: SettingsCalendarPage = self.browser.create_page(SettingsCalendarPage)
        page.insert_name_calendar("calendar A3_" + str(r1))
        page.click_button_next()

        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        page.click_shoose_themes()
        page.click_next_on_theme()
        token_after_calendar = page.take_token_calendar()
        calendar_data = sql_get_calendar(token_after_calendar)
        assert 'Diamonds' == calendar_data[0][1]
        assert 260 == calendar_data[0][0]
