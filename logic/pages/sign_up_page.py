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
    text_yes_markting  = "//div[@class='left-btn']"
    day = "27"
    month = "2"
    year = "1987"
    emailEx = "pinim@lupa.co.il"
    get_exists_text = "//div[@class='center'  and contains(.,'למייל')]"
    get_text_name_f_with_num = "//div[@class='error'  and contains(.,'שם פרטי לא יכול להכיל ספרות')]"
    get_text_name_l_with_num = "//div[@class='error'  and contains(.,'רק לרובוט יש ספרות בשם')]"



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

    def input_user_details_exists(self,firt_name,last_name,emailEx,passwor):
        self.pw_page.fill(self.text_first_name, firt_name)
        self.pw_page.fill(self.text_last_name,
                          last_name)  # self.pw_page.select_option("//select[@class='select-css']","2")
        self.pw_page.fill(self.text_email, emailEx)
        self.pw_page.select_option(self.selectoption_day, self.day)
        self.pw_page.select_option(self.selectoption_month, self.month)
        self.pw_page.select_option(self.selectoption_year, self.year)
        self.pw_page.fill(self.text_password_1, passwor)
        self.pw_page.fill(self.text_password_2, passwor)

    def click_checkbox(self):
        self.pw_page.locator(self.checkbox).click()

    def approval_regulations(self):
        self.pw_page.check(self.checkbox_approval_regulations)

    def click_next(self):
        self.pw_page.click(self.button_next)

    def take_token(self):
        time.sleep(5)
        token = self.pw_page.context.storage_state(path="state.json")
        user_token = token['origins'][0]['localStorage'][0]['value']
        return user_token

    def Sign_me_up_without_mailing(self):
        self.pw_page.click(self.text_yes_markting)

    def get_message_when_user_exists_text(self):
        text_error = self.pw_page.text_content(self.get_exists_text)
       # self.pw_page.close()
        return text_error

    def get_text_error_f_name_with_num(self):
        text_error = self.pw_page.text_content(self.get_text_name_f_with_num)
        return text_error
    def get_text_error_l_name_with_num(self):
        text_error = self.pw_page.text_content(self.get_text_name_l_with_num)
        return text_error








