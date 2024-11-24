from playwright.sync_api import Page, expect


class PersonalDetails:

    first_name = "#:r6:"
    last_name = "#:7:"
    city = "#:8:"
    city_list = "#:9:"
    street = "#:ra:"
    street_list = "/ul[@id=':ra:-listbox']/li"
    house_num = "#:rd"
    apt_num = "#:rd:-label"
    zip_num = "#:re:"
    phone_num = "#:rf:"
    phone_area = "(//div[@class='font_m'])[1]"

    checkbox_business = "(//input[@type='checkbox'])[1]"
    company_name = "#:r2o:"
    company_id = "#:r2p:"
    company_city = "#:r2q:"
    company_city_list = "/ul[@id=':r2q:-listbox']/li"
    company_street = "#:r2s:"
    company_street_list = "/ul[@id=':r2s:-listbox']/li"

    checkbox_shipping = "(//input[@type='checkbox'])[2]"
    first_name_for = "#:6:"
    last_name_for = "#:r2v:"
    city_for = "#:r30:"
    city_list_for = "/ul[@id=':r30:-listbox']/li"
    street_for = "#:r32:"
    street_list_for = "/ul[@id=':r32:-listbox']/li"
    house_num_for = "#:r34:"
    apt_num_for = "#:r35:"
    zip_num_for = "#:r36:"
    phone_num_for = "#:r37:"
    phone_area_for = "(//div[@class='font_m'])[2]"


    def __init__(self, page: Page):
        self.page = page




    def fill_personal_details(self, first_name, last_name, city_list, street_list, house_num, apt_num, zip_num, phone_num, phone_area):
        self.page.fill(self.first_name, first_name)
        self.page.fill(self.last_name, last_name)
        self.page.locator(self.city).click()
        self.page.locator(self.city_list).get_by_text(city_list, exact=True).click()
        self.page.locator(self.street).click()
        self.page.locator(self.street_list).get_by_text(street_list, exact=True).click()
        self.page.fill(self.house_num, house_num)
        self.page.fill(self.apt_num, apt_num)
        self.page.fill(self.zip_num, zip_num)
        self.page.fill(self.phone_num, phone_num)
        self.page.locator(self.phone_area).click()
        self.page.get_by_role("option", name=phone_area,exact=True).click()



    def fill_company_details(self, company_name, company_id, company_city_list, company_street_list):
        self.page.locator(self.checkbox_business).check()
        self.page.fill(self.company_name, company_name)
        self.page.fill(self.company_id, company_id)
        self.page.locator(self.company_city).click()
        self.page.locator(self.company_city_list).get_by_text(company_city_list, exact=True).click()
        self.page.locator(self.company_street).click()
        self.page.locator(self.company_street_list).get_by_text(company_street_list, exact=True).click()


    def fill_shipping_details(self, first_name_for, last_name_for, city_list_for, street_list_for, house_num_for, apt_num_for, zip_num_for, phone_num_for, phone_area_for):
        self.page.locator(self.checkbox_shipping).check()
        self.page.fill(self.first_name_for, first_name_for)
        self.page.fill(self.last_name_for, last_name_for)
        self.page.locator(self.city_for).click()
        self.page.locator(self.city_list_for).get_by_text(city_list_for, exact=True).click()
        self.page.locator(self.street_for).click()
        self.page.locator(self.street_list_for).get_by_text(street_list_for, exact=True).click()
        self.page.fill(self.house_num_for, house_num_for)
        self.page.fill(self.apt_num_for, apt_num_for)
        self.page.fill(self.zip_num_for, zip_num_for)
        self.page.fill(self.phone_num_for, phone_num_for)
        self.page.locator(self.phone_area_for).click()
        self.page.get_by_role("option", name=phone_area_for,exact=True).click()


