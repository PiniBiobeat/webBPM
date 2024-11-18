from playwright.sync_api import Page, expect



class Shipping:

    asafta_b = "//div[@class='shipping_method']/h3[contains(text(), 'אספתא')]"
    bar_shops = "//div[@class='shipping_method']/h3[contains(text(), 'איסוף מנקודות מסירה')]"
    post_il = "//div[@class='shipping_method']/h3[contains(text(), 'דואר רשום')]"
    bar_home = "//div[@class='shipping_method']/h3[contains(text(), 'שליחות עד הבית')]"

    shops_menu_city = "#city"
    shops_list_city = "//ul[@id='city-listbox']/li"
    shops_menu_point = "#select_collecting_point"
    shops_list_point = "//ul[@id='select_collecting_point-listbox']/li"

    isof_code = "//p[contains(text(), 'קוד להזמנה מרוכזת')]"
    isof_fill = "//input[@id=':rb:']"
    isof_error = "//p[@id=':r6:-helper-text']"

    bar_shops_valid_city = "#city-helper-text"
    bar_shops_valid_point = "#select_collecting_point-helper-text"
    close_icon = 'data-testid=CloseIcon'


    def __init__(self, page: Page):
        self.page = page


    def asafta(self):
        self.page.click(self.asafta_b)
        self.page.get_by_role("button", name="מידע נוסף").click()


    def shops(self, city, point):
        self.page.click(self.bar_shops)
        self.page.get_by_role("button", name="מידע נוסף").click()
        self.page.locator(self.shops_menu_city).click()
        self.page.locator(self.shops_list_city).get_by_text(city, exact=True).click()
        self.page.locator(self.shops_menu_point).click()
        self.page.locator(self.shops_list_point).get_by_text(point, exact=True).click()


    def post(self):
        self.page.click(self.post_il)
        self.page.get_by_role("button", name="מידע נוסף").click()


    def home(self):
        self.page.click(self.bar_home)
        self.page.get_by_role("button", name="מידע נוסף").click()


    def no_shops_selection(self):
        self.page.click(self.bar_shops)
        self.page.get_by_role("button", name="בואו נמשיך").click()
        expect(self.page.locator(self.bar_shops_valid_city)).to_be_visible()
        expect(self.page.locator(self.bar_shops_valid_point)).to_be_visible()


    def no_shops_validation(self):
        self.page.click(self.bar_shops)
        self.page.locator(self.shops_menu_city).click()
        self.page.locator(self.shops_list_city).get_by_text("פתח תקוה", exact=True).click()
        self.page.locator(self.shops_menu_point).last.click()
        self.page.locator(self.shops_list_point).get_by_text("ברזיל הקטנה", exact=True).click()
        self.page.locator(self.shops_menu_city).click()
        self.page.locator(self.shops_list_city).get_by_text("אופקים", exact=True).click()
        self.page.wait_for_timeout(3000)
        expect(self.page.locator("h1")).not_to_have_text("פרטים אישיים")


    def no_shops_deleting(self):
        self.page.click(self.bar_shops)
        self.page.locator(self.shops_menu_city).click()
        self.page.locator(self.shops_list_city).get_by_text("תנובות", exact=True).click()
        self.page.locator(self.shops_menu_point).last.click()
        self.page.locator(self.shops_list_point).get_by_text("E-MOBILE", exact=True).click()
        self.page.locator(self.close_icon).first.click(force=True)
        self.page.get_by_role("button", name="בואו נמשיך").click()
        expect(self.page.locator(self.bar_shops_valid_city)).to_be_visible()
        expect(self.page.locator(self.bar_shops_valid_point)).to_be_visible()


    def no_shipping_selection_back_and_forward(self):
        self.page.click(self.bar_home)
        self.page.go_back()
        self.page.go_forward()
        self.page.get_by_role("button", name="בואו נמשיך").click()
        expect(self.page.get_by_text("אי אפשר להמשיך בלי לבחור משלוח ללופה שלך")).to_be_visible()