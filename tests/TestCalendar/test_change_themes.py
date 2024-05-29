import pytest
from tests.TestTiles.test_base import TestBase
from tests.TestCalendar.CalendarGenericFunctions import CalendarPagesManager
import random
import json
import os

r1 = random.randint(1, 1000)
email1 = 'pinim@lupa.co.il'
pass1 = "Pinimari!1"
master_id = 3189204
path_images = ["./shutterstock_315831767.jpg"]
ThemeName = "White"


class TestChangeThemes(CalendarPagesManager):


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_change_themes(self):
        self.openLogin()
        self.setFormat()
        self.setSettings("for testing")
        self.setThemes()
        self.setPersonalDates()
        self.setPhotos()
        self.changeChooseThemes()
        self.setThemeWhite()
        a = self.get_calendar_theme()
        calendar_data = self.get_token()
        print("Success")
        with open(calendar_data[0][2] + '\\Dat\\projectObj.Dat' + '', "rb") as file:
            data = json.load(file)
        if calendar_data[0][1] != 'White':
            # error
            assert "Error"
        else:
            # database update correctly!
            assert "Success"