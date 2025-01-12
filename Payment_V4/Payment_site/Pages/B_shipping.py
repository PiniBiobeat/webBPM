from playwright.sync_api import Page, expect
from Payment_V4.Payment_site.Pages._General_function import Generalfunction


class Shipping:
    selector_asafta_b = "//div[@class='shipping_method']/h3[contains(text(), 'אספתא')]"
    selector_bar_shops = "//div[@class='shipping_method']/h3[contains(text(), 'איסוף מנקודות מסירה')]"
    selector_post_il = "//div[@class='shipping_method']/h3[contains(text(), 'דואר רשום')]"
    selector_bar_home = "//div[@class='shipping_method']/h3[contains(text(), 'שליחות עד הבית')]"

    selector_ship_price = "//div[@class='shipping_methods selected available']/div/h3"

    shops_menu_city = "#city"
    shops_list_city = "//ul[@id='city-listbox']/li"
    shops_menu_point = "#select_collecting_point"
    shops_list_point = "//ul[@id='select_collecting_point-listbox']/li"

    selector_bar_shops_valid_city = "#city-helper-text"
    selector_bar_shops_valid_point = "#select_collecting_point-helper-text"
    close_icon = 'data-testid=CloseIcon'

    isof_button = "//p[contains(text(), 'קוד להזמנה מרוכזת')]"
    isof_fill = "//label[text()='קוד קופון']"
    isof_confirm = "//button[text()='אישור']"
    isof_error = "//p[@id=':r6:-helper-text']"
    return_ship_price_value = None


    def __init__(self, page: Page):
        self.page = page


    def ship_coupon_name(self, coupon_code):
        if "Home" in coupon_code:
            self.home()
        elif "Post" in coupon_code:
            self.post()
        elif "Shops" in coupon_code:
            self.shops("פתח תקוה", "ברזיל הקטנה")


    def asafta(self):
        self.page.click(self.selector_asafta_b)
        self.page.get_by_role("button", name="מידע נוסף").click()
        ship_selected_price = self.page.locator(self.selector_ship_price).inner_text().replace("₪", "")
        Generalfunction(self.page).next_button()
        self.return_ship_price(ship_selected_price)
        return self


    def shops(self, city="פתח תקוה", point="ברזיל הקטנה"):
        self.page.click(self.selector_bar_shops)
        self.page.get_by_role("button", name="מידע נוסף").click()
        self.page.locator(self.shops_menu_city).click()
        self.page.locator(self.shops_list_city).get_by_text(city, exact=True).click()
        self.page.locator(self.shops_menu_point).click()
        self.page.locator(self.shops_list_point).get_by_text(point, exact=True).click()
        ship_selected_price = self.page.locator(self.selector_ship_price).inner_text().replace("₪", "")
        Generalfunction(self.page).next_button()
        self.return_ship_price(ship_selected_price)
        return self


    def post(self):
        self.page.click(self.selector_post_il)
        self.page.get_by_role("button", name="מידע נוסף").click()
        ship_selected_price = self.page.locator(self.selector_ship_price).inner_text().replace("₪", "")
        Generalfunction(self.page).next_button()
        self.return_ship_price(ship_selected_price)
        return self


    def home(self):
        self.page.click(self.selector_bar_home)
        self.page.get_by_role("button", name="מידע נוסף").click()
        ship_selected_price = self.page.locator(self.selector_ship_price).inner_text().replace("₪", "")
        Generalfunction(self.page).next_button()
        self.return_ship_price(ship_selected_price)
        return self


    def return_ship_price(self, ship_selected_price):
        Shipping.return_ship_price_value = ship_selected_price
        return self


    def no_shops_selection(self):
        self.page.click(self.selector_bar_shops)
        Generalfunction(self.page).next_button()
        expect(self.page.locator(self.selector_bar_shops_valid_city)).to_be_visible()
        expect(self.page.locator(self.selector_bar_shops_valid_point)).to_be_visible()


    def no_shops_validation(self):
        self.page.click(self.selector_bar_shops)
        self.page.locator(self.shops_menu_city).click()
        self.page.locator(self.shops_list_city).get_by_text("פתח תקוה", exact=True).click()
        self.page.locator(self.shops_menu_point).last.click()
        self.page.locator(self.shops_list_point).get_by_text("ברזיל הקטנה", exact=True).click()
        self.page.locator(self.shops_menu_city).click()
        self.page.locator(self.shops_list_city).get_by_text("אופקים", exact=True).click()
        self.page.wait_for_timeout(3000)
        expect(self.page.locator("h1")).not_to_have_text("פרטים אישיים")


    def no_shops_deleting(self):
        self.page.click(self.selector_bar_shops)
        self.page.locator(self.shops_menu_city).click()
        self.page.locator(self.shops_list_city).get_by_text("תנובות", exact=True).click()
        self.page.locator(self.shops_menu_point).last.click()
        self.page.locator(self.shops_list_point).get_by_text("E-MOBILE", exact=True).click()
        self.page.locator(self.close_icon).first.dblclick(force=True)
        Generalfunction(self.page).next_button()
        expect(self.page.locator(self.selector_bar_shops_valid_city)).to_be_visible()
        expect(self.page.locator(self.selector_bar_shops_valid_point)).to_be_visible()


    def no_shipping_selection_back_and_forward(self):
        self.page.click(self.selector_bar_home)
        self.page.go_back()
        self.page.go_forward()
        Generalfunction(self.page).next_button()
        expect(self.page.get_by_text("אי אפשר להמשיך בלי לבחור משלוח ללופה שלך")).to_be_visible()


    def add_isof_code(self, isof_code):
        self.page.locator(self.isof_button).click()
        self.page.locator(self.isof_fill).fill(isof_code)
        self.page.locator(self.isof_confirm).click()
        try:
            expect(self.page.locator("h1")).to_have_text("פרטים אישיים")
            Generalfunction(self.page).next_button()

        except:
            error_isof_msg = self.page.locator(self.isof_error).inner_text()
            print(error_isof_msg)
            return error_isof_msg
