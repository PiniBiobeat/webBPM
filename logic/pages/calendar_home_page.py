from infra.page_base import PageBase

class CalendarPage(PageBase):

    init_indication = "(//button[@type='button'])[1]"
    open_menu_page = "(//button[@type='button'])[1]"
    text_open_menu = '//span[contains(.,"התחברות")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'

    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.init_indication, state="visible")

    def open_menu(self):
        self.pw_page.click(self.open_menu_page)

    def open_screen_login_from_menu(self):
        self.pw_page.click(self.text_open_menu)
       # self.pw_page.on("response", lambda response: response if key in response.body())


