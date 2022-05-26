from infra.page_base import PageBase


class EditPage(PageBase):

    group_images = "//div[@class='skewed_border lupa-gallery']"
    choose_image_1 = "//div[@class='photo_thumbnail' and contains(@data-id,'957')]"
    choose_image_2 = "//div[@class='photo_thumbnail' and contains(@data-id,'958')]"
    button_next = "//button[@class='lupa-btn']"
    drop_image = "//div[@class='cropping_overlay']"

    def __init__(self, page):
        super().__init__(page)
       # self.pw_page.wait_for_selector(self.title_button, state="visible")

    def move_image(self):
        pass
       #self.pw_page.mouse.move(2,173)
       #   new =  "transform-origin: center center; position: absolute; filter: none; transform: translate3d(-544.452px, -284.968px, 0px) scale(0.290965);"
       # # oneBoundingBox = self.pw_page.evaluate("""transform-origin: center center; position: absolute; filter: none; transform: translate3d(-544.452px, -284.968px, 0px) scale(0.290965);""".format("h1"))
       #   s = "//div[@class='edit_box']"
       #
       #   self.pw_page.mouse.move(s.x,new.y)
       #   self.pw_page.mouse.down()
       #   self.pw_page.mouse.move(
       #          twoBoundingBox.x + twoBoundingBox.width / 2,
       #          twoBoundingBox.y + twoBoundingBox.height / 2,
       #
       #      )
       #  self.pw_page.mouse.up()
        # selector = "h1"
        # x_pos = page.evaluate("""document.querySelector("{}").getBoundingClientRect()["x"]""".format(selector)
        # y_pos = page.evaluate("""document.querySelector("{}").getBoundingClientRect()["y"]""".format(selector)
        # page.mouse.move(x=x_pos, y=y_pos, steps=100)
        # page.hover(selector)
        # page.click(selector)

    def select_group_images(self):
        self.pw_page.click(self.group_images)