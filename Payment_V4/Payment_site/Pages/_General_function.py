from playwright.sync_api import Page
from dotenv import load_dotenv
import configparser
import os
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'config.ini')), load_dotenv()


class Generalfunction:
    source_db_data = None

    def __init__(self, page: Page):
        self.page = page


    def navigate(self, site):
        self.page.goto(config['GLOBAL'][site+"_"+os.getenv('env')])
        if "books" in site:
            Generalfunction.source_db_data = "lupa_online"
        else:
            Generalfunction.source_db_data = "lupa_square"


    def next_button(self):
        self.page.get_by_role("button", name="בואו נמשיך").click()

