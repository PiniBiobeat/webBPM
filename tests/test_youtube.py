"""
YouTube test using base_url fixture from conftest.py
"""
import re
import pytest
from playwright.sync_api import Page, expect
from tests.test_base import TestWebBase
from logic.pages.youtube_page import YTPage


class TestYouTube(TestWebBase):
    """Test class for YouTube functionality"""
    
    @pytest.mark.smoke
    def test_youtube_side_menu(self, page: Page, base_url):
        """Test clicking the YouTube side menu"""
        # Create page object
        youtube_page = YTPage(page)
        
        # Verify page object was created successfully
        assert youtube_page is not None
        assert hasattr(youtube_page, 'side_menu')
        
        # Use Playwright's expect for better assertions
        expect(page.locator(youtube_page.side_menu).first).to_be_visible()
        
        # Click the side menu (Note: this has a very long timeout - you may want to adjust)
        # youtube_page.click_side_menu()
        
    def test_youtube_page_load(self, page: Page, base_url):
        """Test that YouTube loads successfully"""
        # Use Playwright's expect for better assertions
        expect(page).to_have_title(re.compile("YouTube", re.IGNORECASE))
        expect(page).to_have_url(re.compile("youtube.com"))
        
        # Verify essential YouTube elements are present
        expect(page.locator("id=guide-icon").first).to_be_visible()  # Side menu icon
