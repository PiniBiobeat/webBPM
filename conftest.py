from playwright.sync_api import Playwright
import pytest




test_co = ({"username": "test","password": "Acf325A12!"})

#desktop
@pytest.fixture(scope="session")
def browser_context(playwright: Playwright,request):
    viewport = {'width': 1280, 'height': 720}

    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--window-position=-1920,0"] * False)
    context = browser.new_context(http_credentials=test_co,color_scheme='light',viewport=viewport)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    failed_before = request.session.testsfailed
    yield context
    if request.session.testsfailed != failed_before:
        context.tracing.stop(path="zone_trace.zip")
    context.close()
    browser.close()

#mobile
@pytest.fixture(scope="session")
def mobile_browser_context(playwright: Playwright,request):
    device = playwright.devices['iPhone 15 Pro Max']

    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--window-position=-1920,0"] * False)
    context = browser.new_context(http_credentials=test_co,color_scheme='light',**device)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    failed_before = request.session.testsfailed
    yield context
    if request.session.testsfailed != failed_before:
        context.tracing.stop(path="zone_mobile_trace.zip")
    context.close()
    browser.close()


#desktop page
@pytest.fixture(scope="session")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()

#mobile page
@pytest.fixture(scope="session")
def page_mobile(mobile_browser_context):
    page = mobile_browser_context.new_page()
    yield page
    page.close()



#URLS
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
@pytest.fixture(scope="module")
def Payment_url_books_prod(request):
    page = request.getfixturevalue('page' if 'page' in request.fixturenames else 'page_mobile')
    page.goto(config['GLOBAL']['Payment_url_books_prod'])

@pytest.fixture(scope="module")
def Payment_url_books_test(request):
    page = request.getfixturevalue('page' if 'page' in request.fixturenames else 'page_mobile')
    page.goto(config['GLOBAL']['Payment_url_books_test'])

@pytest.fixture(scope="module")
def Payment_url_tiles_prod(request):
    page = request.getfixturevalue('page' if 'page' in request.fixturenames else 'page_mobile')
    page.goto(config['GLOBAL']['Payment_url_tiles_prod'])

@pytest.fixture(scope="module")
def Payment_url_tiles_test(request):
    page = request.getfixturevalue('page' if 'page' in request.fixturenames else 'page_mobile')
    page.goto(config['GLOBAL']['Payment_url_tiles_test'])









































from infra.config.config_provider import init_config
config_path = ""
browser = {}


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.ini")


def pytest_configure(config):
    config_path = config.getoption('--config')
    init_config(config_path)

