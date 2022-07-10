from infra.page_base import PageBase
import time
import json




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


    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.text_button_upload, state="visible")

    def click_upload_photos(self):
        self.pw_page.locator(self.text_button_upload).set_input_files(self.path_images)

    def sum_all_images(self):
        self.pw_page.wait_for_selector(self.text_sum_with_test, state="visible")
        images = self.pw_page.query_selector_all(self.text_sum_with_test)
        num_of_image = len(images)
        return num_of_image

    def click_upload_photos_to_check_low_quality(self):
        self.pw_page.locator(self.text_button_upload).set_input_files(self.image_with_low_quality)

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

