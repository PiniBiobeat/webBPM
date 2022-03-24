from infra.page_base import PageBase

class PreviewScreen(PageBase):


    title_button = "//span[@style='font-size: 22px;']"
    all_selector_in_page = '//div[@class="vh_div"]'
    psifas_size = '// option[ @ value = "1"]'

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





