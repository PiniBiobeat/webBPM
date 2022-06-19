from infra.page_base import PageBase
import time
import json


class NameBook(PageBase):

    init_indication = "//div[@class=' large intro-box']/h4[@class='intro-title']"
    locator_book_name = "//input[@id='mat-input-1']"
    click_button_next = "//button[@type='submit' and contains(.,'המשיכו')]"
    get_err_text = "//mat-error[@class='mat-error ng-star-inserted']"
    click_in_input = "//input[@id='mat-input-1']"
    get_err_text_short_name = "//mat-error[@class='mat-error ng-star-inserted' and contains(.,' שם הספר קצר מידי ')]"
    click_checkbox = "//input[@type='checkbox' ]//..//..//span[@class='mat-checkbox-label' and contains(.,' שניה לפני שממשיכים בבקשה אשרו את ')]"
    approval_button = "(//button[@type='submit'])[2]"
    icon_manu = "//mat-icon[@class='mat-icon']"
    text_create_album = "//a[@class='ng-tns-c0-0' and contains(text(),'יצירת ספר')]"
    text_login_title = "(//h1[@class='bold' and contains(text(),'כניסה לחשבון לופה')])[1]"
    text_iframe = "(//iframe[@frameborder='0'])[1]"

    def __init__(self, page):
        super().__init__(page)
        #self.pw_page.wait_for_selector(self.locator_book_name, state="visible")

    def click_next(self):
        self.pw_page.click(self.click_button_next)

    def click_on_manu(self):
        self.pw_page.click(self.icon_manu)

    def click_create_album(self):
        self.pw_page.click(self.text_create_album)

    def get_err(self):
        text =  self.pw_page.text_content(self.get_err_text)
        return text

    def get_text_from_login(self):
        text_title_login = self.pw_page.frame_locator(self.text_iframe).locator(self.text_login_title).text_content()
        return text_title_login

    def insert_name_book(self,name_of_book):
        self.pw_page.click(self.click_in_input)
        self.pw_page.fill(self.locator_book_name,name_of_book)

    def get_err_short(self):
        text_short = self.pw_page.text_content(self.get_err_text_short_name)
        return text_short

    def approval_regulations(self):
        self.pw_page.click(self.click_checkbox)

    def click_approval(self):
        self.pw_page.click(self.approval_button)

    def take_token(self):
         time.sleep(10)
         event_token = self.pw_page.evaluate("JSON.parse(localStorage.getItem('LUPA_TOKEN'))['event_token']")
         return event_token

    def take_frame(self):
        pass
        #frame_one = self.pw_page.wait_for_selector("(//iframe[@frameborder='0'])[1]").content_frame()




