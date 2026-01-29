import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

load_dotenv()


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright) -> Browser:
    headed = os.getenv("HEADED", "false").lower() == "true"

    browser = playwright.chromium.launch(
        headless=not headed,
        args=["--disable-dev-shm-usage"]
    )
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser, request) -> BrowserContext:
    if "BASE_URL" not in os.environ:
        raise RuntimeError("BASE_URL environment variable is not set")

    context = browser.new_context(
        base_url=os.environ["BASE_URL"],
        viewport={"width": 1280, "height": 720},
        record_video_dir="artifacts/videos"
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    if request.node.rep_call.failed:
        context.tracing.stop(
            path=f"artifacts/traces/{request.node.name}.zip"
        )
    else:
        context.tracing.stop()

    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
