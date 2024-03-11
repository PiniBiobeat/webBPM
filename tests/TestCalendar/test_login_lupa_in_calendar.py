import pytest
from tests.TestTiles.test_base import TestBase
from infra.config.config_provider import configuration
from logic.pages.login_online_page import LogInOnline
from logic.pages.calendar_home_page import CalendarPage
from logic.pages.login_calendar_page import LoginCalendarPage
import json

email1 = 'pinim@lupa.co.il'
pass1 = "Pinimari!1"




class TestLoginCalendar(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_log_in_online_with_lupa(self):
        page: CalendarPage = self.browser.navigate(configuration['calendar_url'], CalendarPage)
        page.open_menu()
        page.open_screen_login_from_menu()

        page: LoginCalendarPage = self.browser.create_page(LoginCalendarPage)
        page.insert_user_and_pass(email1,pass1)
        page.click_login_button()
        token_after_login = page.take_token()
        a = json.loads(token_after_login)
        b =  a['token']
        assert b is not None