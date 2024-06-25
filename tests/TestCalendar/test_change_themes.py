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
        self.setSettings("for testing ")
        self.setThemes()
        self.setPersonalDates()
        self.setPhotos()
        self.changeChooseThemes()
        self.setThemeWhite()
        #a = self.get_calendar_theme()
        calendar_data = self.get_token()
        print(calendar_data)

        file_path = os.path.join(calendar_data[0][2], 'Dat', 'projectObj.dat')
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                data = json.load(file)

            assert calendar_data[0][1] == 'White', "Calendar data theme is not set to White"
            assert data['ThemeName'] == 'White', "Project object theme is not set to White"

            print("Theme successfully changed to White")
        else:
            pytest.fail(f"File not found: {file_path}")

