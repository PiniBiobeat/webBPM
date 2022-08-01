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
    text_click_pupap = 'text = הבנתי בואו נתקדם'
    text_button_locators = "//button[@class='ng-tns-c9-4 mat-raised-button mat-accent']"
    text_button_next = "(//button)[6]"
    text_buttom_image = "(//div[@class='image-wrap'])[2]"
    text_button_delete = "//a[@class='delete']"
    text_edit_button = "//a[@class='editPhoto']"
    text_set_cover_image = "//a[@class='setCover']"
    text_cover_image = "(//div[@class='select-wrap'])[2]"
    text_button_add_image = "text = הוסיפו עוד תמונות"
    text_button_add_from_local = "text = מחשב"
    text_button_add_text = "text = הוספת טקסט "
    text_from_image = "(//div[@class='select-wrap'])[2]"
    image_with_text = ["C:/Users/lupa/Desktop/london/IMG_2549.jpg","C:/Users/lupa/Desktop/london/IMG_2561.jpg","C:/Users/lupa/Desktop/london/IMG_2569.jpg"]


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

    def click_upload_Photos_for_text(self):
        self.pw_page.locator(self.text_button_upload).set_input_files(self.image_with_text)
        self.pw_page.click(self.text_click_pupap)

    def click_add_images(self):
        self.pw_page.click(self.text_button_add_image)

    def click_add_images_from_local(self):
        self.pw_page.locator(self.text_button_add_from_local).set_input_files(self.path_images)

    def click_choose_one_image(self):
        self.pw_page.click(self.text_buttom_image)

    def click_add_text(self):
        self.pw_page.click(self.text_button_add_text)

    def click_on_set_cover_image(self):
        self.pw_page.click(self.text_set_cover_image)

    def click_on_edit_button(self):
        self.pw_page.click(self.text_edit_button)

    def click_on_delete_button_image(self):
        self.pw_page.click(self.text_button_delete)

    def get_text_low_quality(self):
        self.pw_page.wait_for_selector(self.text_low_quality, state="visible")
        return_low_quality = self.pw_page.locator(self.text_low_quality).text_content()
        return return_low_quality

    def get_unprintable_quality(self):
        self.pw_page.wait_for_selector(self.text_unprintable_quality, state="visible")
        return_low_quality = self.pw_page.locator(self.text_unprintable_quality).text_content()
        return return_low_quality

    def get_locator_button(self):
        test_text =  self.pw_page.locator(self.text_button_next)
        return test_text

    def get_locator_image(self):
        return_text_image = self.pw_page.locator(self.text_cover_image)
        return return_text_image

    def get_text_from_image(self):
        return_text_from_image = self.pw_page.locator(self.text_from_image).text_content()
        return return_text_from_image


