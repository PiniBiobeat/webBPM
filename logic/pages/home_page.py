from infra.page_base import PageBase

class HomePage(PageBase):

    init_indication = "//div[@class=' large intro-box']/h4[@class='intro-title']"
    tiles_button = '(//span[@class="lupa-btn-content"])[1]'
    pesipas_button = '(//span[@class="lupa-btn-content"])[2]'
    menu_button = '//img[@class="burger_menu"]'
    open_login_sceen_button = '//div[@class="menu-item" and contains(.,"כניסה ")]'
    click_log_out  = '//div[@class="menu-item" and contains(.,"יציאה מהחשבון")]'
    button_sign_up = '//span[@style="display: inline-flex;" and contains(.,"יצירת חשבון חדש")]'
    manu_icon = "//img[@class='burger_menu']"
    link_log_in = "(//div[@class='menu-item'])[1]"
    button_lups_site = "(//div[@class='menu-item'])[2]"
    button_lups_tariff = "(//div[@class='menu-item'])[3]"


    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.init_indication, state="visible")

    def choose_tiles(self):
        self.pw_page.click(self.tiles_button)

    def choose_pesipas(self):
        self.pw_page.click(self.pesipas_button)
    def open_menu(self):
        self.pw_page.click(self.menu_button)

    def click_log_in(self):
        self.pw_page.click(self.link_log_in)

    def open_screen_login_from_menu(self):
        self.pw_page.click(self.open_login_sceen_button)

    def log_out(self):
        self.pw_page.click(self.click_log_out)

    def shoose_sign_up(self):
        self.pw_page.click(self.button_sign_up)

    def click_lupa_site(self):
        with self.pw_page.context.expect_page() as tab:
            self.pw_page.click(self.button_lups_site)
        new_tab = tab.value.url
        return new_tab

    def click_lupa_tariff(self):
        self.pw_page.click(self.button_lups_tariff)






