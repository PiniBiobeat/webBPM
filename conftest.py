"""
Pytest configuration and fixtures for the test automation project.
"""
import os
import time
import allure
from playwright.sync_api import Playwright, BrowserContext
import pytest
import logging
from dotenv import load_dotenv
from infra.config.config_provider import configuration

# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Test credentials should be loaded from environment variables
test_credentials = {
    "username": os.getenv("TEST_USERNAME", "test_user"),
    "password": os.getenv("TEST_PASSWORD", "test_password")
}



@pytest.fixture(scope="session")
def browser_context(playwright: Playwright, request) -> BrowserContext:
    """
    Create a browser context for the test session.
    Supports desktop and mobile environments.
    """
    env = os.getenv("DEV", "desktop")

    if env == "desktop":
        viewport = {'width': 1280, 'height': 720}
        browser = playwright.chromium.launch(
            headless=True,  # Always run in headless mode
            slow_mo=500,
            args=["--window-position=-1920,0"] if os.getenv("POSITION_BROWSER") else None
        )
        context = browser.new_context(
            http_credentials=test_credentials,
            color_scheme='light',
            viewport=viewport,
            record_video_dir=None
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    elif env == "mobile":
        device = playwright.devices['iPhone 15 Pro Max']
        browser = playwright.chromium.launch(
            headless=True,  # Always run in headless mode
            slow_mo=500,
            args=["--window-position=-1920,0"] if os.getenv("POSITION_BROWSER") else None
        )
        context = browser.new_context(
            http_credentials=test_credentials,
            color_scheme='light',
            **device,
            record_video_dir=None
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    elif env == "headless":
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(
            http_credentials=test_credentials,
            color_scheme='light'
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    else:
        raise ValueError(f"Unknown environment: {env}. Supported: desktop, mobile, headless")

    yield context

    # Cleanup
    context.close()
    browser.close()



@pytest.fixture(scope="function")
def page(browser_context, request, base_url):
    """
    Create a new page for each test.
    Automatically navigates to the base URL.
    Handles test failure screenshots and traces.
    """
    page = browser_context.new_page()
    
    # Navigate to the base URL automatically
    page.goto(base_url)
    
    failed_before = request.session.testsfailed
    
    yield page
    
    # Handle test failures
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        
        # Capture trace
        try:
            trace_path = f"traces/{test_name}_trace.zip"
            os.makedirs("traces", exist_ok=True)
            browser_context.tracing.stop(path=trace_path)
            allure.attach(
                body=open(trace_path, "rb").read(),
                name=f"{test_name}_trace",
                attachment_type="application/zip"
            )
        except Exception as e:
            print(f"Could not save trace: {e}")
        
        # Capture screenshot
        try:
            screenshot = page.screenshot()
            allure.attach(
                body=screenshot,
                name=f"{test_name}_failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Could not save screenshot: {e}")
    
    page.close()


@pytest.fixture
def before_after_test():
    """
    Setup and teardown fixture for tests that need special handling.
    """
    # Setup code here
    print("\\n=== Test Setup ===")
    
    yield
    
    # Teardown code here
    print("\\n=== Test Teardown ===")


# Pytest hooks
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "regression: mark test as regression test")
    config.addinivalue_line("markers", "integration: mark test as integration test")


def pytest_runtest_setup(item):
    """Called before each test runs."""
    test_name = item.name
    logger.info(f"Starting test: {test_name}")


def pytest_runtest_teardown(item):
    """Called after each test runs."""
    test_name = item.name
    logger.info(f"Finished test: {test_name}")