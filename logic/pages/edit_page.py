from infra.page_base import PageBase


class EditPage(PageBase):

    group_images = "//div[@class='skewed_border lupa-gallery']"
    choose_image_1 = "//div[@class='photo_thumbnail' and contains(@data-id,'957')]"
    choose_image_2 = "//div[@class='photo_thumbnail' and contains(@data-id,'958')]"
    button_next = "//button[@class='lupa-btn']"
    drop_image = "//div[@class='cropping_overlay']"
    button_save = "(//span[@class='lupa-btn-content'])[1]"

    def __init__(self, page):
        super().__init__(page)


    def move_image(self):
        #selector = "//img[@class='edit-image']//.."
        self.pw_page.evaluate("document.getElementsByClassName('edit-image')[0].parentElement.style.transform = 'translate3d(-440px, -284.968px, 0px) scale(0.290965)'")
        # #y_pos = 284#self.pw_page.evaluate("document.getElementsByClassName('edit-image')[0].parentElement.style.transform = 'translate3d(-427.548px, -284.968px, 0px) scale(0.290965)'")
        #
        # self.pw_page.query_selector(':nth-match(:text("id"), 2)').scroll_into_view_if_needed()
        # src_box = self.pw_page.query_selector('ul.drag-item >> xpath=li[2]').bounding_box()
        # tgt_box = self.pw_page.query_selector('text=ADD VARIABLE').bounding_box()
        #
        # self.pw_page.mouse.move(x_pos['x'] + x_pos['width'] / 2, x_pos['y'] + x_pos['height'] / 2)
        # print('Mouse move')
        # self.pw_page.mouse.down()
        # self.pw_page.mouse.move(-427.548,284.968,steps=5)
        # self.pw_page.mouse.down()
        # self.pw_page.hover(selector)
        # self.pw_page.click(selector)
        #self.pw_page.drag_and_drop("440","300"[,source_position=None])

    def click_save(self):
        self.pw_page.click(self.button_save)

    def select_group_images(self):
        self.pw_page.click(self.group_images)