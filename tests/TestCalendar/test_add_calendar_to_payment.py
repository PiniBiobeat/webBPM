from tests.TestCalendar.CalendarGenericFunctions import CalendarPagesManager
import pytest
import time, os

from dotenv import load_dotenv


class TestAddCalendarToPayment(CalendarPagesManager):


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_calendar_to_paymentA3(self):
            self.openLogin()
            self.clickMyCalendar()
            self.addToBasket()

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_calendar_to_paymentA4(self):
        self.openLogin()
        self.clickMyCalendar()
        self.addToBasket()

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_add_calendar_to_paymentA5(self):
        self.openLogin()
        self.clickMyCalendar()
        self.addToBasket()
