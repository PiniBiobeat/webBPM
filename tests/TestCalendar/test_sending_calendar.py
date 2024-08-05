from tests.TestCalendar.CalendarGenericFunctions import CalendarPagesManager
import pytest
import time, os

from dotenv import load_dotenv


class TestSendingCalendar(CalendarPagesManager):


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_send_calendar(self):
        try:
            self.openLogin()
            self.setFormat()
            self.setSettings(f"for testing: {time.time()}")
            self.setThemes()
            self.setPersonalDates()
            self.setPhotos()
            self.click_x_to_next()
            for month in range(1, 13):
                if month < 5:
                    self.choose_layout(month)
                    a = self.get_locaors_plus()
                    for times in range(a):
                        self.click_plus_to_add_photos()
                        self.choose_image_from_storage()
                else:
                    self.click_plus_to_add_photos()
                    self.choose_image_from_storage()
                self.choose_month(month+1)
            self.click_plus_to_add_photos()
            self.choose_image_from_storage()
            self.click_to_checkout()
            time.sleep(20)
            print("Success")

        except Exception as e:
            print(e)
            assert False

