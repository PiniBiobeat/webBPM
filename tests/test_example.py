"""
Example test file demonstrating the test structure.
This example focuses on YouTube functionality using base_url fixture.
"""
import re
import pytest
from playwright.sync_api import Page, expect
from tests.test_base import TestWebBase
from logic.pages.youtube_page import YTPage


class TestExample(TestWebBase):
    """Example test class for YouTube"""
    
    @pytest.mark.smoke
    def test_example_youtube_page_creation(self, page: Page, base_url):
        """Example test method - create YouTube page object"""
        # Create YouTube page object
        youtube_page = YTPage(page)
        
        # Verify page object was created successfully
        assert youtube_page is not None
        assert youtube_page.side_menu == "id=guide-icon"
        
        # Use Playwright's expect for better assertions
        expect(page).to_have_title(re.compile("YouTube", re.IGNORECASE))
    
    def test_youtube_basic_navigation(self, page: Page, base_url):
        """Example test for basic YouTube navigation"""
        # Use Playwright's expect for better assertions
        expect(page).to_have_title(re.compile("YouTube", re.IGNORECASE))
        expect(page).to_have_url(re.compile("youtube.com"))
        
        # Verify page elements are present
        expect(page.locator("id=guide-icon").first).to_be_visible()
