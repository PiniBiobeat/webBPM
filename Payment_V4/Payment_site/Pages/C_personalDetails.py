from playwright.sync_api import Page, expect
from Payment_V4.Payment_site.Pages._General_function import Generalfunction


class PersonalDetails:

    first_name = '[data-testid="first_name_sender"] input'
    last_name = '[data-testid="last_name_sender"] input'
    city = '[data-testid="city_sender"] input'
    city_list = "(//div/ul/li)"
    street = '[data-testid="street_sender"] > div > input:not([disabled])'
    street_list = "(//div/ul/li)"
    house_num = '[data-testid="building_num_sender"] input'
    apt_num = '[data-testid="apartment_num_sender"] input'
    zip_num = '[data-testid="zip_sender"] input'
    phone_num = '[data-testid="phone_number_sender"] input'
    phone_area = "(//div[@class='font_m'])[1]"

    checkbox_business = "(//input[@type='checkbox'])[1]"
    company_name = '[data-testid="company_business"] input'
    company_id = '[data-testid="company_id_business"] input'
    company_city = 'data-testid="company_city_business"'
    company_city_list = "(//div/ul/li)"
    company_street = '[data-testid="company_street_business"] > div > input:not([disabled])'
    company_street_list = "(//div/ul/li)"

    checkbox_shipping = "(//input[@type='checkbox'])[2]"
    first_name_for = '[data-testid="first_name_receiver"] input'
    last_name_for = '[data-testid="last_name_receiver"] input'
    city_for = '[data-testid="city_receiver"]'
    city_list_for = "(//div/ul/li)"
    street_for = '[data-testid="street_receiver"] > div > input:not([disabled])'
    street_list_for = "(//div/ul/li)"
    house_num_for = '[data-testid="building_num_receiver"] input'
    apt_num_for = '[data-testid="apartment_num_receiver"] input'
    zip_num_for = '[data-testid="zip_receiver"] input'
    phone_num_for = '[data-testid="phone_number_receiver"] input'
    phone_area_for = "(//div[@class='font_m'])[2]"


    def __init__(self, page: Page):
        self.page = page


    def filler_detail(self):
        self.page.locator(self.city).fill("פתח תקוה")
        self.page.locator(self.city_list).get_by_text("פתח תקוה", exact=True).click()
        self.page.locator(self.street).fill("תוצרת הארץ")
        self.page.locator(self.street_list).get_by_text("תוצרת הארץ", exact=True).click()
        self.page.fill(self.house_num, "3")
        Generalfunction(self.page).next_button()


    def fill_personal_details(self, first_name, last_name, city_list, street_list, house_num, apt_num, zip_num, phone_num, phone_area_list):
        self.page.fill(self.first_name, first_name)
        self.page.fill(self.last_name, last_name)
        self.page.locator(self.city).fill(city_list)
        self.page.locator(self.city_list).get_by_text(city_list, exact=True).click()
        self.page.locator(self.street).fill(street_list)
        self.page.locator(self.street_list).get_by_text(street_list, exact=True).click()
        self.page.fill(self.house_num, house_num)
        self.page.fill(self.apt_num, apt_num)
        self.page.fill(self.zip_num, zip_num)
        self.page.fill(self.phone_num, phone_num)
        self.page.locator(self.phone_area).click()
        self.page.get_by_role("option", name=phone_area_list, exact=True).click()


    def fill_company_details(self, company_name, company_id, company_city_list, company_street_list):
        self.page.locator(self.checkbox_business).check()
        self.page.fill(self.company_name, company_name)
        self.page.fill(self.company_id, company_id)
        self.page.locator(self.company_city).fill(company_city_list)
        self.page.locator(self.company_city_list).get_by_text(company_city_list, exact=True).click()
        self.page.locator(self.company_street).fill(company_street_list)
        self.page.locator(self.company_street_list).get_by_text(company_street_list, exact=True).click()


    def fill_shipping_details(self, first_name_for, last_name_for, city_list_for, street_list_for, house_num_for, apt_num_for, zip_num_for, phone_num_for, phone_area_for):
        self.page.locator(self.checkbox_shipping).check()
        self.page.fill(self.first_name_for, first_name_for)
        self.page.fill(self.last_name_for, last_name_for)
        self.page.locator(self.city_for).fill(city_list_for)
        self.page.locator(self.city_list_for).get_by_text(city_list_for, exact=True).click()
        self.page.locator(self.street_for).fill(street_list_for)
        self.page.locator(self.street_list_for).get_by_text(street_list_for, exact=True).click()
        self.page.fill(self.house_num_for, house_num_for)
        self.page.fill(self.apt_num_for, apt_num_for)
        self.page.fill(self.zip_num_for, zip_num_for)
        self.page.fill(self.phone_num_for, phone_num_for)
        self.page.locator(self.phone_area_for).click()
        self.page.get_by_role("option", name=phone_area_for, exact=True).click()


