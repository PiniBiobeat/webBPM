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

    
    # def test_youtube_basic_navigation(self, page: Page, base_url):
    #     """Example test for basic YouTube navigation"""
    #     # Use Playwright's expect for better assertions
    #     expect(page).to_have_title(re.compile("YouTube", re.IGNORECASE))
    #     expect(page).to_have_url(re.compile("youtube.com"))
    #
    #     # Verify page elements are present
    #     expect(page.locator("id=guide-icon").first).to_be_visible()
