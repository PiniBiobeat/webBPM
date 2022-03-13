from infra.page_base import PageBase


class InstagramPage(PageBase):

    choose_image_from_instagram_1 = "//div[@data-id= '17892985862326647']"
    choose_image_from_instagram_2 = "//div[@data-id= '17955143470490995']"
    button_next = "//button[@class= 'lupa-btn']"

    def __init__(self, page):
        super().__init__(page)

    def upload_photos_from_instagram(self):
       self.pw_page.click(self.choose_image_from_instagram_1)
       self.pw_page.click(self.choose_image_from_instagram_2)
       self.pw_page.click(self.button_next)
