from infra.page_base import PageBase

class UploadPhotoPage(PageBase):

    input_photo = "//input[@id= 'f']"
    title_button = "//span[@id= 'header_title']"
    gallery_button = "//img[@src='/static/media/icon_gallery_old.e4c596ba.svg']"
    instagram_button = "//img[@src='/static/media/icon_instagram.ae47004e.svg']"
    title_instagram  = "//h1[@class='NXVPg Szr5J  coreSpriteLoggedOutWordmark  ']"
    user_name = "//span[@class='_9nyy2']"
    user_password = "//input[@aria-label='Password']"
    login_button = "//button[@type='submit']"
    button_login_save_1 = "//button[@class='sqdOP  L3NKy   y3zKF     ']"
    button_login_save_2 = "//button[@class='sqdOP  L3NKy   y3zKF   cB_4K  ']"
    title_instagram_photos = "//span[@id= 'header_title']"
    wait_for_save = "//button[@class= 'sqdOP  L3NKy   y3zKF     ']"
    googlePhotos_button ="//img[@src='/static/media/icon_google_photos.776cf4ac.svg']"
    googleUserName_button="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b']"
    googleFillEmail_button="//input[@type='email']"
    googleFillPassword_button="//input[@type='password']"
    googleFillAllow_button="//span[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe P62QJc xYnMae TrZEUc lw1w4b']"
    googleAllPhotos_button="//p[@class= 'album_title']"
    googlePhoto_button="//div[@class='content ']"
    choose_image_from_instagram_1 = "//div[@data-id= '17892985862326647']"
    choose_image_from_instagram_2 = "//div[@data-id= '17955143470490995']"
    button_next = "//button[@class= 'lupa-btn']"

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.title_button, state="visible")

    def upload_photo(self, path):
        self.pw_page.set_input_files(self.input_photo, path)

    def upload_photo_gallery(self):
        self.pw_page.click(self.gallery_button)

    def login_to_instagram(self, text_user_name,text_password):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.instagram_button)
        popup = popup_info.value
        popup.wait_for_load_state()
        popup.fill(self.user_name,text_user_name)
        popup.fill(self.user_password,text_password)
        popup.click(self.login_button)
        popup.wait_for_timeout(7000)
        popup.click(self.button_login_save_1)
        popup.click(self.button_login_save_2)

    def upload_photos_from_instagram(self):
        self.pw_page.click(self.choose_image_from_instagram_1)
        self.pw_page.click(self.choose_image_from_instagram_2)
        self.pw_page.click(self.button_next)
        print("")

       # print(popup.title())
        self.pw_page.wait_for_selector(self.title_instagram_photos, state="visible")

    def upload_photo_googlePhotos(self, text_user_name,text_password):
        with self.pw_page.expect_popup() as popup_info:
            self.pw_page.click(self.googlePhotos_button)
        popup = popup_info.value
        popup.wait_for_load_state()
        popup.fill(self.googleFillEmail_button,text_user_name)
        popup.click(self.googleUserName_button)
        popup.wait_for_timeout(4000)
        popup.fill(self.googleFillPassword_button,text_password)
        popup.click(self.googleUserName_button)
        popup.click(self.googleUserName_button)
        popup.wait_for_timeout(1000)
        popup.click(self.googleAllPhotos_button)
        popup.wait_for_timeout(1000)
        popup.click(self.googlePhoto_button)
        #self.pw_page.wait_for_selector(self.wait_for_save, state="visible")
        popup.wait_for_timeout(7000)
        popup.click(self.login1)
        popup.click(self.login2)

       # print(popup.title())
        self.pw_page.wait_for_selector(self.title_instagram_photos, state="visible")


    def login_imstagram(self, text_user_name):
         #  self.pw_page.wait_for_selector(self.title_instagram, state="visible")
       # self.pw_page.on("https://tiles-tiny.lupa.co.il/single")

        self.pw_page.fill(self.user_name,text_user_name)
        # self.pw_page.evaluate_handle()
        #
        #
        # self.pw_page.wait_for_load_state()
        pass


