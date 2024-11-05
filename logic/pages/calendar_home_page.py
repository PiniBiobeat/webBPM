from infra.page_base import PageBase

class CalendarPage(PageBase):

    init_indication = "(//button[@type='button'])[2]"
    icon_open_menu = "(//button[@type='button'])[1]"
    open_menu_page = "(//button[@type='button'])[2]"
    text_open_menu = '//span[contains(.,"התחברות")]'
    text_choose_create_user = '//button[contains(.,"ליצירת חשבון")]'
    text_open_my_calender = '//span[contains(.,"לוחות השנה שלי")]'

    def __init__(self, page):
        super().__init__(page)


    def open_menu(self):
        self.pw_page.click(self.open_menu_page)

    def open_menu_after_login(self):
        self.pw_page.click(self.icon_open_menu)
    def open_screen_login_from_menu(self):
        self.pw_page.click(self.text_open_menu)
       # self.pw_page.on("response", lambda response: response if key in response.body())

    def open_screen_my_calendar_from_menu(self):
        self.pw_page.click(self.text_open_my_calender)


