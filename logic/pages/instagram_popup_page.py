from infra.page_base import PageBase

class InstagramPopUp(PageBase):

    user_name = "//span[@class='_9nyy2']"
    user_password = "//input[@aria-label='Password']"
    login_button = "//button[@type='submit']"
    button_login_save_1 = "//button[@type='button' and contains(., 'Save Info')]"
    button_login_save_2 = "//button[@class='sqdOP  L3NKy   y3zKF   cB_4K  ' and contains(., 'Allow')]"
    choose_image_from_instagram_1 = "//div[@data-id= '17935148023619398']"

    def __init__(self, page):
        super().__init__(page)

    def login_instagram(self,text_user_name_instagram,text_password_instagram):
        self.pw_page.wait_for_load_state()
        self.pw_page.fill(self.user_name, text_user_name_instagram)
        self.pw_page.fill(self.user_password, text_password_instagram)
        self.pw_page.click(self.login_button)
        self.pw_page.click(self.button_login_save_1)
        self.pw_page.click(self.button_login_save_2)







