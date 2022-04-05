from infra.page_base import PageBase


class PsifasPhotosPage(PageBase):

    LocalPhotosBottom = "//input[@id='f']"
    googleChoosePhoto_button = '(//div[@class="rounded_box"])[2]'
    button_next = "//button[@class= 'lupa-btn']"
    sizesMenu="//select[@class='select-css']"

    def __init__(self, page):
        super().__init__(page)

    def Psifas_upload_photos(self, path):
        self.pw_page.set_input_files(self.LocalPhotosBottom, path)



