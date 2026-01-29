"""
Example test file demonstrating the test structure.
This example focuses on YouTube functionality using base_url fixture.
"""
import re
import pytest
from playwright.sync_api import Page, expect
from tests.test_base import TestWebBase
from logic.pages.BPM_login_page import BPMLoginPage


class TestExample(TestWebBase):
    @pytest.mark.smoke
    def test_example_BPM_web_page_creation(self, page: Page, base_url):
        login_page = BPMLoginPage(page)
        login_page.login("pini","mari")
        expect(page.get_by_text("Incorrect username or password")).to_be_visible()

