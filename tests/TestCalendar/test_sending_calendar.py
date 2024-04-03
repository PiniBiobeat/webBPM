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
        for month in range(1, 14):
            if month < 7:
                self.choose_layout(month)
                a = self.get_locaors_plus()
                for times in range(a):
                    self.click_plus_to_add_photos()
                    self.choose_image_from_storage()
            else:
                self.click_plus_to_add_photos()
                self.choose_image_from_storage()
            self.choose_month(month)
        self.click_to_checkout()
        self.next_to_checkout()
        self.click_accsept()
        time.sleep(20)
        #self.wait_for_payments()
        print("Success")
