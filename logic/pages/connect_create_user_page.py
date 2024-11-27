from infra.page_base import PageBase
import time
import json
from playwright.sync_api import expect



class ConnectCreateUserPage(PageBase):

    click_open_menu =  "(//*[@type='button']//*[name()='svg'])[5]"
    text_yes_delete = "//a[@class='cancel' and contains(text(),'כן, למחוק')]"
    text_input = "//input[@placeholder='הוסיפו כותרת לתמונה']"
    text_button_save = "text = שמרו "
    text_create_user = "(//button[@type='button' and contains(.,'ליצירת חשבון')])[1]"
    text_my_books =  "//img[@src='/assets/img/my_books.svg']"
    img_user = "//img[@src='/assets/img/avatar.svg']"
    text_connect_user = "//a[@class='ng-star-inserted']"
    text_first_name = "//input[@id=':r4:']"
    text_last_name = "//input[@id=':r5:']"
    text_email = "//input[@id=':r6:']"
    text_num_phone = "//input[@id=':r9:']"
    frame_connect = "//iframe[@src='https://connect-v2-ui.lupa.co.il/loginregister?channel=websitev2']"
    frame = "//iframe[@frameborder='0']"
    text_password1 = "//input[@id=':ra:']"
    text_password2 = "//input[@id=':rb:']"
    text_checkbox = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[2]"
    text_checkbox_newswetter = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[1]"
    text_button_create_user = "//button[@data-testid='btn-register']"
    get_exists_text = "//div[@class='color_red font_xs MuiBox-root css-0' and contains(text(),'זה מייל שיש לו כבר חשבון בלופה')]"
    get_error_f_name = "(//div[@class='color_red font_xs MuiBox-root css-0' and contains(text(),'רק לרובוטים יש ספרות בשם')])[1]"
    get_error_l_name = "//p[@id=':r5:-helper-text']"
    get_error_email_name = "//p[@id=':r6:-helper-text']"
    get_error_phone_name = "//p[@id=':r9:-helper-text']"
    get_error_password_name = "//p[@id=':ra:-helper-text']"
    get_error_password = "//p[@id=':rb:-helper-text']"
    get_error_approval_regulations = "//p[@role='policy-helper-register']"
    text_popup_date = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw']"
    text_11_day = "(//button[@class='MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin css-ub1r1'])[1]"
    text_approve_date = "(//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-1ujsas3'])[2]"
    text_popup_title = " //h2[@id='alert-dialog-title']"
    text_my_books_name = "//img[@src='/assets/img/my_books.svg']//..//..//..//button[@class='header_button ng-star-inserted']"
    text_add_book_to_payment = "(//*[contains(text(), 'הוספת ספר לסל')])[1]"
    text_choose_format = 'img[alt="ריבועי גדול"]'
    text_next_to_choose_cover= "//button[@class='mat-raised-button mat-accent' and contains(.,'המשיכו')]"
    text_choose_cover = 'img[alt="כריכה קשה"]'

    def __init__(self, page):
        super().__init__(page)
        #self.pw_page.wait_for_selector(self.text_my_books, state="visible")


    def click_my_book(self):
        self.pw_page.click(self.text_my_books)

    def wait_for_mybooks(self):
        target_url = "https://account.lupa.co.il/my-projects.aspx"
        self.pw_page.wait_for_url(target_url)

    def click_icon_user(self):
        self.pw_page.click(self.img_user)

    def click_add_book_to_payment(self):
        with self.pw_page.context.expect_page() as new_page_info:
            self.pw_page.click(self.text_add_book_to_payment)  # Opens a new tab
        new_page = new_page_info.value

        # Interact with the new page normally
        new_page.click(self.text_choose_format)
        new_page.click(self.text_next_to_choose_cover)
        new_page.click(self.text_choose_cover)
        new_page.click(self.text_next_to_choose_cover)
        new_page.click(self.text_next_to_choose_cover)

    def click_add_book_to_payment_with_link(self):
        self.pw_page.click(self.text_add_book_to_payment)
        self.pw_page.click(self.text_choose_format)
        self.pw_page.click(self.text_next_to_choose_cover)
        self.pw_page.click(self.text_choose_cover)
        self.pw_page.click(self.text_next_to_choose_cover)
        self.pw_page.click(self.text_next_to_choose_cover)

    def wait_payment_url(self):
        target_url = "https://paymentsv4-ui.lupa.co.il/marketing"
        self.pw_page.wait_for_url(target_url)



    def wait_for_lupa_online(self):
        target_url = "https://online.lupa.co.il/"
        self.pw_page.wait_for_url(target_url)

    def click_my_book_name(self):
        time.sleep(20)
        self.pw_page.click(self.text_my_books_name)

    def click_connect_user(self):
        self.pw_page.click(self.text_connect_user)
        self.pw_page.wait_for_selector(self.frame, state="visible")
       # self.pw_page.frame_locator(self.frame).locator("//button[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-1r09c7j']").click()

    def click_connect_user_up(self):
        self.pw_page.click(self.text_connect_user)
        #self.pw_page.wait_for_selector(self.frame, state="visible")
        self.pw_page.frame_locator(self.frame).locator("//button[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-1r09c7j']").click()

    def click_create_account(self):
        #self.pw_page.click(self.text_connect_user)
        # self.pw_page.wait_for_selector(self.frame, state="visible")
        self.pw_page.frame_locator(self.frame).locator("//button[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-1r09c7j']").click()


    def insert_user_details(self, firt_name, last_name, emailEx,num_phone, password):
        self.pw_page.frame_locator(self.frame).locator(self.text_first_name).fill(firt_name)
        self.pw_page.frame_locator(self.frame).locator(self.text_last_name).fill(last_name)
        self.pw_page.frame_locator(self.frame).locator(self.text_email).fill(emailEx)
        self.pw_page.frame_locator(self.frame).locator(self.text_num_phone).fill(num_phone)
        self.pw_page.frame_locator(self.frame).locator(self.text_password1).fill(password)
        self.pw_page.frame_locator(self.frame).locator(self.text_password2).fill(password)

    def click_open_popup(self):
        self.pw_page.frame_locator(self.frame).locator(self.text_popup_date).click()


    def insert_user_details_pass(self, firt_name, last_name, emailEx,num_phone, password):
        self.pw_page.frame_locator(self.frame).locator(self.text_first_name).fill(firt_name)
        self.pw_page.frame_locator(self.frame).locator(self.text_last_name).fill(last_name)
        self.pw_page.frame_locator(self.frame).locator(self.text_email).fill(emailEx)
        self.pw_page.frame_locator(self.frame).locator(self.text_num_phone).fill(num_phone)

        self.pw_page.frame_locator(self.frame).locator(self.text_password1).fill(password)
        self.pw_page.frame_locator(self.frame).locator(self.text_password2).fill(password+ "wwwww")


    def click_checkbox_with_newsletter(self):
        self.pw_page.frame_locator(self.frame).locator(self.text_checkbox_newswetter).click()
        self.pw_page.frame_locator(self.frame).locator(self.text_checkbox).click()

    def click_button_create_user(self):
        self.pw_page.frame_locator(self.frame).locator(self.text_button_create_user).click()

    def click_checkbox(self):
        self.pw_page.frame_locator(self.frame).locator(self.text_checkbox).click()
    def take_token(self):
        time.sleep(8)
        token = self.pw_page.context.storage_state(path="state.json")
        user_token = token['origins'][0]['localStorage'][3]['value']
        return user_token

    def take_token_online(self):
        time.sleep(8)
        token = self.pw_page.context.storage_state(path="state.json")
        user_token = token['origins'][0]['localStorage'][3]['value']
        return user_token

    def get_message_when_user_exists_text(self):
        text_error = self.pw_page.frame_locator(self.frame).locator(self.get_exists_text).text_content()
        return text_error

    def get_text_error_f_name_with_num(self):
        text_error = self.pw_page.frame_locator(self.frame).locator(self.get_error_f_name).text_content()
        return text_error

    def get_text_error_l_name_with_num(self):
        text_error = self.pw_page.frame_locator(self.frame).locator(self.get_error_l_name).text_content()
        return text_error

    def get_text_error_email_with_num(self):
        text_error = self.pw_page.frame_locator(self.frame).locator(self.get_error_email_name).text_content()
        return text_error

    def get_text_error_phone_with_num(self):
        text_error = self.pw_page.frame_locator(self.frame).locator(self.get_error_phone_name).text_content()
        return text_error

    def get_text_error_password_with_num(self):
        text_error = self.pw_page.frame_locator(self.frame).locator(self.get_error_password_name).text_content()
        return text_error

    def get_text_error_password(self):
        text_error = self.pw_page.frame_locator(self.frame).locator(self.get_error_password).text_content()
        return text_error

    def get_text_error_approval_regulations(self):
        text_error = self.pw_page.frame_locator(self.frame).locator(self.get_error_approval_regulations).text_content()
        return text_error

    def select_date_birth(self):
        self.pw_page.frame_locator(self.frame).locator(self.text_11_day).click()
        self.pw_page.frame_locator(self.frame).locator(self.text_approve_date).click()

    def get_text_title_popup(self):
        text_error = self.pw_page.frame_locator(self.frame).locator(self.text_popup_title).text_content()
        return text_error


