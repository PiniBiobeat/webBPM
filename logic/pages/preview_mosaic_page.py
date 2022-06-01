from infra.page_base import PageBase

class PreviewMosaicScreen(PageBase):


    title_button = "//span[@style='font-size: 22px;']"
    all_selector_in_page = '//div[@class="vh_div"]'
    psifas_size = '// option[ @ value = "1"]'
    icon_add_image = "//img[@class='upload_icon']"
    icon_google = "//img[@src='/static/media/icon_google_photos.776cf4ac.svg']"
    test_logout = "//div[@class='first-row-el'][1]"
    icon_delete = "(//img[@src='/static/media/icon_trash.5d8f7be3.svg'])[1]"
    text_yes_delete = "//span[@class='lupa-btn-content' and contains(.,'כן')]"
    icon_edit = "(//img[@src='/static/media/icon_image_edit.d59295f7.svg'])[1]"
    gel_all_size = "//option[@direction='rtl']"
    wait_for_ele =  "//select[@class='select-css']"

    def __init__(self, page):
        super().__init__(page)

    def get_image(self):
        self.pw_page.wait_for_selector(self.all_selector_in_page, state="visible")
        images = self.pw_page.query_selector_all(self.all_selector_in_page)
        num_of_image = len(images)
        return num_of_image

    def get_price(self):
        text = self.pw_page.text_content(self.title_button)
        return text

    def get_psifas_size(self):
        text_psifas_size = self.pw_page.text_content(self.psifas_size)
        return text_psifas_size

    def click_add_image(self):
        self.pw_page.click(self.icon_add_image)

    def get_psifas_size_1(self):
        self.pw_page.wait_for_selector(self.wait_for_ele, state="visible")
        size = self.pw_page.locator(self.gel_all_size).count()
        return size

    def click_add_image_from_google(self):
        self.pw_page.click(self.icon_google)

    def click_log_out(self):
        self.pw_page.click(self.test_logout)

    #def move_the_image(self):
       # self.pw_page.click('canvas',{position: {x: 50,y: 100}})







