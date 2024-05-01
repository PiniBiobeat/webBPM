import pytest
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.login_online_page import LogInOnline
from logic.pages.calendar_home_page import CalendarPage
from logic.pages.login_calendar_page import LoginCalendarPage
from logic.pages.choose_format_calendar_page import ChooseFormatCalendarPage
from logic.pages.settings_calendar_page import SettingsCalendarPage
from logic.pages.choose_themes_calendar_page import ThemesCalendarPage
from logic.pages.edit_personal_date_page import EditPersonalDates
from infra.generic_helpers import sql_get_calendar,sql_get_path_calendar,sql_get_event_date ,sql_delete_personal_date
import random
import os
import json
path_images = ["./shutterstock_315831767.jpg"]
r1 = random.randint(1, 1000)
email1 = 'jenkinslupa@gmail.com'
pass1 = "8777775"
master_id = 3189204


class TestAddPersonamDate(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_personal_date_with_image(self):

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
        page.click_add_personal_date()

        page: EditPersonalDates = self.browser.create_page(EditPersonalDates)
        page.select_event_eype()
        page.select_attribution_selection()
        page.input_name_event("event name")
        page.click_add_photos()
        page.add_photos_from_local(path_images)
        page.click_save_image()
        page.click_save_event()
        page.click_checkbox()
        page.click_checkbox_next()

        calendar_date_a = sql_get_event_date(3606890)
        print(f"after script  - >{calendar_date_a}/n")
        sql_delete_personal_date(3606890)
        assert len(calendar_date_a) > 0
