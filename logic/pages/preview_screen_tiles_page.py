from infra.page_base import PageBase

class PreviewScreen(PageBase):


    title_button = "//span[@style='font-size: 22px;']"

    def __init__(self, page):
        super().__init__(page)

    def get_image(self):
        images = self.pw_page.query_selector_all('//div[@class="vh_div"]')
        num_of_image = len(images)
        return num_of_image

    def get_price(self):
        text = self.pw_page.text_content(self.title_button)
        return text


