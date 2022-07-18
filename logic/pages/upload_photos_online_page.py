from infra.page_base import PageBase
import time
import json
from playwright.sync_api import expect



class UploadPhotosOnline(PageBase):

    text_button_upload = "(//div[@class='card-content'])[1]"
    path_images = ["C:/Users/lupa/Desktop/london/IMG_2549.jpg","C:/Users/lupa/Desktop/london/IMG_2561.jpg",
                   "C:/Users/lupa/Desktop/london/IMG_2569.jpg", "C:/Users/lupa/Desktop/london/IMG_2595.jpg",
                   "C:/Users/lupa/Desktop/london/IMG_2596.jpg", "C:/Users/lupa/Desktop/london/IMG_2618.jpg",
                                                                "C:/Users/lupa/Desktop/london/IMG_2549.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_425742643.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_428941816.jpg", "C:/Users/lupa/Desktop/london/shutterstock_445141507.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_473627458.jpg", "C:/Users/lupa/Desktop/london/shutterstock_448948483.jpg",
                                                                "C:/Users/lupa/Desktop/london/shutterstock_499513999.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_502044016.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_506010544.jpg", "C:/Users/lupa/Desktop/london/shutterstock_504251206.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_517165138.jpg", "C:/Users/lupa/Desktop/london/shutterstock_507392950.jpg",
                                                                "C:/Users/lupa/Desktop/london/shutterstock_517686724.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_583939735.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_607084640.jpg", "C:/Users/lupa/Desktop/london/shutterstock_607235345.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_661848901.jpg", "C:/Users/lupa/Desktop/london/shutterstock_711632317.jpg",
                   "C:/Users/lupa/Desktop/london/shutterstock_279024293.jpg"
                   ]
    image_with_low_quality = ["C:/Users/lupa/Desktop/london/shutterstock_711632317.jpg", "C:/Users/lupa/Desktop/Test Mosaic/1210-1210.jpg","C:/Users/lupa/Desktop/auto/shutterstock_5.jpg"]
    text_sum_with_test = "//div[@class='image ng-tns-c11-4 ng-star-inserted visible active']"
    text_low_quality = 'text = איכות נמוכה'
    text_unprintable_quality = 'text = איכות לא ניתנת להדפסה'
    text_click_pupap = "//div[@class='mat-dialog-actions']"
    text_button_locators = "//button[@class='ng-tns-c9-4 mat-raised-button mat-accent']"
    text_button_next = "(//button)[6]"
    text_buttom_image = "(//div[@class='image-wrap'])[2]"
    text_button_delete = "//a[@class='delete']"
    text_edit_button = "//a[@class='editPhoto']"
    text_set_cover_image = "//a[@class='setCover']"
    adxax = "//div[@class='overlay ng-tns-c9-3 ng-star-inserted'] and"


    def __init__(self, page):
        super().__init__(page)
       # self.pw_page.wait_for_selector(self.text_button_upload, state="visible")

    def click_upload_photos(self):
        self.pw_page.locator(self.text_button_upload).set_input_files(self.path_images)

    def sum_all_images(self):
        self.pw_page.wait_for_selector(self.text_sum_with_test, state="visible")
        images = self.pw_page.query_selector_all(self.text_sum_with_test)
        num_of_image = len(images)
        return num_of_image

    def click_upload_photos_to_check_low_quality(self):
        self.pw_page.locator(self.text_button_upload).set_input_files(self.image_with_low_quality)
        self.pw_page.click(self.text_click_pupap)

    def click_choose_one_image(self):
        self.pw_page.click(self.text_buttom_image)

    def click_on_set_cover_image(self):
        self.pw_page.click(self.text_set_cover_image)

    def click_on_edit_button(self):
        self.pw_page.click(self.text_edit_button)

    def click_on_delete_button_image(self):
        self.pw_page.click(self.text_button_delete)

    def get_text_low_quality(self):
        self.pw_page.wait_for_selector(self.text_low_quality, state="visible")
        self.pw_page.click(self.text_click_pupap)
        return_low_quality = self.pw_page.locator(self.text_low_quality).text_content()
        return return_low_quality

    def get_unprintable_quality(self):
        self.pw_page.wait_for_selector(self.text_unprintable_quality, state="visible")
        self.pw_page.click(self.text_click_pupap)
        return_low_quality = self.pw_page.locator(self.text_unprintable_quality).text_content()
        return return_low_quality

    def get_locator_button(self):
        test_text =  self.pw_page.locator(self.text_button_next)
        return test_text

    def get_locator_button1(self):
        test_text1 =  self.pw_page.locator(self.adxax)
        return test_text1


