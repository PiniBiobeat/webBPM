from infra.page_base import PageBase


class GooglePhotosPage(PageBase):
    googleAllPhotos_button = "//p[@class= 'album_title']"
    googleChoosePhoto_button = "//div[@class='content ']"
    button_next = "//button[@class= 'lupa-btn']"
    choose_mosaic_album = "(//div[@class='album_thumbnail'])[2]"
    choose_image_1210_x_1210 = "//div[@data-id='ANJqiFRS5d7_pKdChZclZp1Rl_MVEbBERu5T8yHYiK9H6ijJ1bM-Xc_Jl2inmhvJAjd8CFszIXPs9BmDugr1yTkmU1Fy2K53tw']"
    big_image = "//div[@data-id='ANJqiFQnSawnOwdpafsFa2HaPzwITsuvSGyKN9wVEe0LRzPtpVha66waVOiy6f0wIcwk57FDCa0JlfftAjHtGvs4FJLhDlreLQ']"

    def __init__(self, page):
        super().__init__(page)

    def upload_photos_from_google(self):
        self.pw_page.click(self.googleAllPhotos_button)
        # for i in range(Quanity):
        self.pw_page.click(self.googleChoosePhoto_button)
        self.pw_page.click(self.button_next)

    def upload_image_for_mosaic(self):
        self.pw_page.click(self.choose_mosaic_album)
        self.pw_page.click(self.big_image)
        self.pw_page.click(self.button_next)


