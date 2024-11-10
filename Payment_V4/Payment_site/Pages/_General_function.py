from playwright.sync_api import Page


class Generalfunction:


    def __init__(self, page: Page):
        self.page = page


    def next_button(self):
        self.page.get_by_role("button", name="בואו נמשיך").click()








