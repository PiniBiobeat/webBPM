from playwright.sync_api import Page
from dotenv import load_dotenv
import configparser
import os
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'config.ini')), load_dotenv()

class Generalfunction:


    def __init__(self, page: Page):
        self.page = page


    def navigate(self, site):
        self.page.goto(config['GLOBAL'][site+"_"+os.getenv('env')])


    def next_button(self):
        self.page.get_by_role("button", name="בואו נמשיך").click()
