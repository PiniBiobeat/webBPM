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
        calendar_data = self.get_token()
        print(f"Calendar data: {calendar_data}")

        file_path = os.path.join(calendar_data[0][2], 'Dat', 'projectObj.dat')
        print(f"Attempting to access file at: {file_path}")

        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            pytest.fail(f"Directory not found: {dir_path}")
        else:
            print(f"Directory contents: {os.listdir(dir_path)}")

        if file_path.startswith('\\\\'):
            print("This is a network path. Verify network connectivity.")

        try:
            with open(file_path, "rb") as file:
                data = json.load(file)

            assert calendar_data[0][1] == 'White', "Calendar data theme is not set to White"
            assert data['ThemeName'] == 'White', "Project object theme is not set to White"

            print("Theme successfully changed to White")
        except FileNotFoundError:
            pytest.fail(f"File not found: {file_path}")
        except PermissionError:
            pytest.fail(f"Permission denied: {file_path}")
        except json.JSONDecodeError:
            pytest.fail(f"Invalid JSON in file: {file_path}")
        except Exception as e:
            pytest.fail(f"Unexpected error: {str(e)}")
