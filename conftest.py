import allure
from playwright.sync_api import Playwright, BrowserContext
import pytest
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
import os


test_co = ({"username": "test", "password": "Acf325A12!"})
#desktop
@pytest.fixture(scope="session")
def browser_context(playwright: Playwright, request) -> [BrowserContext, None, None]:
    env = os.getenv("DEV")
    if env == "desktop":

        viewport = {'width': 1280, 'height': 720}
        browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--window-position=-1920,0"] * False)
        context = browser.new_context(http_credentials=test_co, color_scheme='light', viewport=viewport, record_video_dir=None)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    elif env == "mobile":

        device = playwright.devices['iPhone 15 Pro Max']
        browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--window-position=-1920,0"] * False)
        context = browser.new_context(http_credentials=test_co, color_scheme='light', **device, record_video_dir=None)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    else:
        raise ValueError(f"Unknown environment: {env}")
    yield context
    # context.tracing.stop(path="trace_.zip")
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()






#mobile
@pytest.fixture(scope="session")
def mobile_browser_context(playwright: Playwright,request) -> [BrowserContext, None, None]:
    device = playwright.devices['iPhone 15 Pro Max']
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--window-position=-1920,0"] * False)
    context = browser.new_context(http_credentials=test_co, color_scheme='light', **device, record_video_dir=None)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    # context.tracing.stop(path="trace_mobile_.zip")
    context.close()
    browser.close()

#mobile page
@pytest.fixture(scope="session")
def page_mobile(mobile_browser_context):
    page = mobile_browser_context.new_page()
    yield page
    page.close()



@pytest.fixture(autouse=True)
def trace_on_failure(request, browser_context):
    context = browser_context
    yield
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        test_name = request.node.name
        trace_path = f"trace/trace_{test_name}.zip"
        context.tracing.stop(path=trace_path)
        if context.pages:
            screenshot = context.pages[0].screenshot()
            allure.attach(body=screenshot, name="FailShot", attachment_type=allure.attachment_type.PNG)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)



























from infra.config.config_provider import init_config
config_path = ""
browser = {}


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.ini")


def pytest_configure(config):
    config_path = config.getoption('--config')
    init_config(config_path)

