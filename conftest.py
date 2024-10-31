from playwright.sync_api import Playwright, Page , expect
import pytest_playwright
import pytest



test_co = ({"username": "test","password": "Acf325A12!"})
@pytest.fixture(scope="session")
def browser_context(playwright: Playwright,request):
    viewport = {'width': 1280, 'height': 1080}
    device = playwright.devices['iPhone 15 Pro Max']

    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--window-position=-1920,0"] * False)
    context = browser.new_context(http_credentials=test_co,color_scheme='light')
    context.tracing.start(screenshots=True, snapshots=True, sources=False)

    failed_before = request.session.testsfailed
    yield context
    if request.session.testsfailed != failed_before:
        context.tracing.stop(path="zone_trace.zip")
    context.close()
    browser.close()




@pytest.fixture(scope="session")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()





def test_play2(page):
    page.goto("https://tiles.lupa.co.il")
    expect(page.get_by_role("button", name="בחירת תמונות")).to_be_visible()
    page.pause()
















from infra.config.config_provider import init_config
config_path = ""
browser = {}


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.ini")


def pytest_configure(config):
    config_path = config.getoption('--config')
    init_config(config_path)

