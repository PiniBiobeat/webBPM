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
from tests.TestCalendar.CalendarGenericFunctions import CalendarPagesManager
import random
import json
path_images = ["./shutterstock_315831767.jpg"]
r1 = random.randint(1, 1000)
email1 = 'jenkinslupa@gmail.com'
pass1 = "8777775"
master_id = 3189204


class TestAddPersonamDate(CalendarPagesManager):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_order_with_coupon(self):
        self.openLogin()