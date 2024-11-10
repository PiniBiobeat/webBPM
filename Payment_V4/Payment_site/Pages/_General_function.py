from playwright.sync_api import Page

import configparser
config = configparser.ConfigParser()
config.read('../../../config.ini')



class Generalfunction:


    def __init__(self, page: Page):
        self.page = page

    def navigate(self, site):
        self.page.goto(config['GLOBAL'][site])

    def next_button(self):
        self.page.get_by_role("button", name="בואו נמשיך").click()







