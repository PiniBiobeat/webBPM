from infra.page_base import PageBase


class UploadPhotoPage(PageBase):

    input_photo = "//input[@id= 'f']"
    title_button = "//span[@id= 'header_title']"
    gallery_button = "//div[@class='rounded_box small'][1]"
    instagram_button = "//img[@src='/static/media/icon_instagram.ae47004e.svg']"
    googlePhotos_button = "//img[@src='/static/media/icon_google_photos.776cf4ac.svg']"

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.title_button, state="visible")

    def upload_photo(self, path):
        self.pw_page.set_input_files(self.input_photo, path)

    def upload_photo_gallery(self):
        self.pw_page.click(self.gallery_button)

    def open_instagram(self):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.instagram_button)
        return popup_info.value

    def open_google_photos(self):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.googlePhotos_button)
        return popup_info.value







