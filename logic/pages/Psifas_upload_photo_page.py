from infra.page_base import PageBase


class PsifasPhotosPage(PageBase):

    LocalPhotosBottom = '//div[@class="rounded_box"]'
    googleChoosePhoto_button = '(//div[@class="rounded_box"])[2]'
    button_next = "//button[@class= 'lupa-btn']"
    sizesMenu="//select[@class='select-css']"
    def __init__(self, page):
        super().__init__(page)

    def Psifas_upload_photos(self,path):
        with self.pw_page.expect_file_chooser() as fc_info:
            self.pw_page.click(self.LocalPhotosBottom)
            file_chooser = fc_info.value
            file_chooser.set_files(path)
            self.pw_page.wait_for_timeout(20000)
            self.pw_page.select_option(self.sizesMenu,"2")


