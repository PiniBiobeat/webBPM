from infra.page_base import PageBase
import time

class SignUpPage(PageBase):

    init_indication = "//div[@class='group' and contains(.,'שם המשפחה שלך')]//input[@type='text']"
    text_first_name = "//div[@class='group' and contains(.,'השם שלך')]//input[@type='text']"
    text_last_name = "//div[@class='group' and contains(.,'שם המשפחה שלך')]//input[@type='text']"
    text_email = "//div[@class='group' and contains(.,'המייל שלך')]//input[@type='text']"
    text_password_1 = "//div[@class='group' and contains(.,'הסיסמה שלך')]//input[@type='password']"
    text_password_2 = "//div[@class='group' and contains(.,'שוב הסיסמה')]//input[@type='password']"
    button_next = "//button[@class='lupa-btn']"
    checkbox = "//div[@class='checkbox_container first checkbox_registration' and contains(.,'אני מאשר/ת קבל דואר פרסומי')]//input[@type='checkbox']//..//span[@class = 'checkmark']"
    manu =  '//img[@class="burger_menu"]'
    checkbox_approval_regulations = "//div[@class='checkbox_container checkbox_registration' and contains(.,'אני מאשר/ת את')]//input[@type='checkbox']//..//span[@class = 'checkmark']"
    selectoption_day = "//div[@class='birth-date-day']//select[@class='select-css']"
    selectoption_month = "//div[@class='birth-date-month']//select[@class='select-css']"
    selectoption_year = "//div[@class='birth-date-year']//select[@class='select-css']"
    day = "27"
    month = "2"
    year = "1987"



    def __init__(self, page):
        super().__init__(page)
        self.pw_page.wait_for_selector(self.init_indication, state="visible")

    def input_user_details(self,firt_name,last_name,email,passwor):

        self.pw_page.fill(self.text_first_name,firt_name)
        self.pw_page.fill(self.text_last_name,last_name)#self.pw_page.select_option("//select[@class='select-css']","2")
        self.pw_page.fill(self.text_email,email)
        self.pw_page.select_option(self.selectoption_day,self.day)
        self.pw_page.select_option(self.selectoption_month, self.month)
        self.pw_page.select_option(self.selectoption_year, self.year)
        self.pw_page.fill(self.text_password_1,passwor)
        self.pw_page.fill(self.text_password_2,passwor)


    def click_checkbox(self):
        self.pw_page.locator(self.checkbox).click()

    def approval_regulations(self):
        self.pw_page.check(self.checkbox_approval_regulations)

    def click_next(self):
        self.pw_page.click(self.button_next)

    def take_token(self):
        time.sleep(5)
        token = self.pw_page.context.storage_state(path="state.json")
        user_token = token['origins'][0]['localStorage'][4]['value']
        return user_token







