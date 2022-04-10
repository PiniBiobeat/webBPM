from infra.page_base import PageBase

class HomePage(PageBase):

    init_indication = "//div[@class=' large intro-box']/h4[@class='intro-title']"
    tiles_button = '(//span[@class="lupa-btn-content"])[1]'
    pesipas_button = '(//span[@class="lupa-btn-content"])[2]'
    menu_button = '//img[@class="burger_menu"]'
    open_login_sceen_button = '//div[@class="menu-item" and contains(.,"כניסה ")]'




    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.init_indication, state="visible")

    def choose_tiles(self):
        self.pw_page.click(self.tiles_button)

    def choose_pesipas(self):
        self.pw_page.click(self.pesipas_button)
    def open_menu(self):
        self.pw_page.click(self.menu_button)

    def open_screen_login_from_menu(self):
        self.pw_page.click(self.open_login_sceen_button)


