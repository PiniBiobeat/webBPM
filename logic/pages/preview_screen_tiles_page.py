from infra.page_base import PageBase

class PreviewScreen(PageBase):


    title_button = "//span[@style='font-size: 22px;']"

    def __init__(self, page):
        super().__init__(page)

    def get_price(self):
        num_of_image = self.pw_page.query_selector_all('//div[@class="vh_div"]')
        # s = num_of_image.count("preview=JSHandle@node")
        # print(s)
        #return num_of_image

        rr = len(num_of_image)
        print()
        text = self.pw_page.text_content(self.title_button)

        return text


