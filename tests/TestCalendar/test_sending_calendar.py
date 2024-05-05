from tests.TestCalendar.CalendarGenericFunctions import CalendarPagesManager
import pytest
import time

class TestSendingCalendar(CalendarPagesManager):


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_send_calendar(self):
        self.openLogin()
        self.setFormat()
        self.setSettings("for testing")
        self.setThemes()
        self.setPersonalDates()
        self.setPhotos()
        for month in range(1, 13):
            if month < 6:
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
