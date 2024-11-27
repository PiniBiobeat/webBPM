from infra.page_base import PageBase


class UploadPhotoPage(PageBase):

    input_photo = "//input[@id= 'f']"
    title_button = "//span[@id= 'header_title']"
    gallery_button = "//div[@class='rounded_box small dif'][1]"
    set_size_tiles = "(//li[@class='MuiListItem-root list_model_ul MuiListItem-gutters'])[1]"
    instagram_button = "//img[@src='/static/media/icon_instagram.ae47004e.svg']"
    googlePhotos_button = "//img[@src='/static/media/icon_google_photos.776cf4ac.svg']"
    group_images = "//div[@class='skewed_border lupa-gallery']"
    choose_image_1 = "//div[@class='photo_thumbnail' and contains(@data-id,'791')]"
    #'(//li[@class='MuiListItem-root list_model_ul MuiListItem-gutters'])[1]'

    def __init__(self, page):
        super().__init__(page)
       # self.pw_page.wait_for_selector(self.title_button, state="visible")

    def upload_photo(self, path):
      #  self.pw_page.click(self.set_size_tiles)
        self.pw_page.set_input_files(self.input_photo, path)

    def upload_photo_gallery(self):
        self.pw_page.click(self.gallery_button)
        self.pw_page.click(self.set_size_tiles)
        self.pw_page.click(self.group_images)
        self.pw_page.click(self.choose_image_1)

    def open_instagram(self):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.instagram_button)
        return popup_info.value

    def open_google_photos(self):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.googlePhotos_button)
        return popup_info.value







