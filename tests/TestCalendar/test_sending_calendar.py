from tests.TestCalendar.CalendarGenericFunctions import CalendarPagesManager
import pytest


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
        #self.click_plus_to_add_photos()
       # self.link_add_images_after()
        #self.open_choose_laout_1()
        #self.open_choose_laout_2()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_1()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_2()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_3()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_4()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_5()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_6()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_7()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_8()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_9()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_10()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_11()
        self.click_plus_to_add_photos()
        self.choose_image_from_storage()
        self.choose_month_12()
        self.open_choose_laout_1()
        self.choose_month()


        self.createPreview()
        self.choose_image_from_storage()
        #click_plos_image()
        #select_image
        #click_next_monso
        #chenge_lyat
        # click_plos_image()
        # click_plos_image()
        # click_next_monso


        page: ThemesCalendarPage = self.browser.create_page(ThemesCalendarPage)
        token_after_calendar = page.take_token_calendar_after_login()
        calendar_data = sql_get_calendar(token_after_calendar)
        with open(calendar_data[0][2]+'\\Dat\\projectObj.Dat'+'', "rb") as file:
            data = json.load(file)
        if calendar_data[0][0] != "eTo" and data['Format'] == "eTo":
            # error
            assert "Error"
        else:
            # database update correctly!
            assert "Success"
