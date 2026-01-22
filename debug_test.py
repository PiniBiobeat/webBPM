"""
Debug test to check navigation
"""
from playwright.sync_api import Page, expect
from infra.config.config_provider import configuration

def test_debug_navigation():
    """Debug test to check if navigation works"""
    print(f"Base URL from config: {configuration['url']}")
    
    # Let's try a simple navigation test
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("Navigating to YouTube...")
        page.goto(configuration['url'])
        
        print(f"Current URL: {page.url}")
        print(f"Page title: {page.title()}")
        
        # Check if page loaded
        try:
            page.wait_for_load_state('networkidle', timeout=10000)
            print("Page loaded successfully")
        except Exception as e:
            print(f"Page load error: {e}")
        
        browser.close()

if __name__ == "__main__":
    test_debug_navigation()
