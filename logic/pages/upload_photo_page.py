from infra.page_base import PageBase

class UploadPhotoPage(PageBase):

    input_photo = "//input[@id= 'f']"
    #path = "C:\\Users\\lupa\\Desktop\\london\\IMG_2549.jpg"
    title_button = "//span[@id= 'header_title']"

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.title_button, state="visible")

    def upload_photo(self, path):
        self.pw_page.set_input_files(self.input_photo, path)
