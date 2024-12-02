from datetime import timedelta, datetime

import pytest
from tests.TestTiles.test_base import TestBase
from dotenv import load_dotenv
from infra.config.config_provider import configuration
from logic.pages.calendar_home_page import CalendarPage
from tests.TestPayment.PaymantGenericFunctions import PaymentPagesManager
import random
import json
import os
load_dotenv()

r1 = random.randint(1, 1000)
email1 = 'pinim@lupa.co.il'
pass1 = "Pinimari!1"
master_id = 3189204
path_images = ["./shutterstock_315831767.jpg"]


class TestChangeFormatCalendar(TestBase):
    testdata = [
        1, 'H7GMH36J', '52',
        1, 'H7GMH36J', '60',
    ]

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    @pytest.mark.parametrize("a,b,expected", testdata)
    def test_timedistance_v0(self,a, b, expected):
        PaymentPagesManager.choose_prod(a)
        #Add_coupon
        #Add_cal
        #Add_tiles
        page.open_menu()
        page.open_screen_login_from_menu()