from infra.page_base import PageBase


class GalleryPage(PageBase):

    group_images = "//div[@class='skewed_border lupa-gallery']"
    choose_image_1 = "//div[@class='photo_thumbnail' and contains(@data-id,'957')]"
    choose_image_2 = "//div[@class='photo_thumbnail' and contains(@data-id,'958')]"
    button_next = "//button[@class='lupa-btn']"

    def __init__(self, page):
        super().__init__(page)
       # self.pw_page.wait_for_selector(self.title_button, state="visible")

    def select_group_images(self):
        self.pw_page.click(self.group_images)

    def select_image(self):
        self.pw_page.click(self.choose_image_1)

    def select_image_2(self):
        self.pw_page.click(self.choose_image_2)

    def click_button_next(self):
        self.pw_page.click(self.button_next)