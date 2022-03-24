from infra.page_base import PageBase


class GooglePhotosPage(PageBase):
    googleAllPhotos_button = "//p[@class= 'album_title']"
    googleChoosePhoto_button = "//div[@class='content ']"
    button_next = "//button[@class= 'lupa-btn']"

    def __init__(self, page):
        super().__init__(page)

    def upload_photos_from_google(self,Quanity=1):
        self.pw_page.click(self.googleAllPhotos_button)
        # for i in range(Quanity):
        self.pw_page.click(self.googleChoosePhoto_button)
        self.pw_page.click(self.button_next)
