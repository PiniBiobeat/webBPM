# playwright-test.py

import json
import urllib
import subprocess
from playwright.sync_api import sync_playwright

desired_cap = {
    'browser': 'chrome',
    'browser_version': 'latest',
    'browserstack.username': 'pinimari_LOj7uc',
    'browserstack.accessKey': '4W91xpp1XNB7qVf4Ezg2',
    'project': 'My First Project',
    'build': 'playwright-python-1',
    'name': 'My First Test',
    'buildTag': 'reg',
    'resolution': '1280x1024',
    'browserstack.local': 'false',
    'browserstack.localIdentifier': 'local_connection_name',
    'browserstack.playwrightVersion': '1.latest',
    'client.playwrightVersion': '1.latest',
    'browserstack.debug': 'true',
    'browserstack.console': 'info',  # Enabling Console logs for the test
    'browserstack.networkLogs': 'true',  # Enabling network logs for the test
    'browserstack.interactiveDebugging': 'true',
}


def test_run_session(playwright):
    clientPlaywrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
    desired_cap['client.playwrightVersion'] = clientPlaywrightVersion

    cdpUrl = 'wss://cdp.browserstack.com/playwright?caps=' + urllib.parse.quote(json.dumps(desired_cap))

    browser = playwright.chromium.connect_over_cdp(cdpUrl)

    page = browser.new_page()
    try:
        page.goto("https://www.google.co.in/")
        page.fill("[aria-label='Search']", 'Browserstack')
        locator = page.locator("[aria-label='Google Search'] >> nth=0")
        locator.click()
        title = page.title()

        if title == "Browserstack - Google Search":
            # following line of code is responsible for marking the status of the test on BrowserStack as 'passed'. You can use this code in your after hook after each test
            mark_test_status("passed", "Title matched", page)
        else:
            mark_test_status("failed", "Title did not match", page)
    except Exception as err:
        mark_test_status("failed", str(err), page)

    browser.close()


def mark_test_status(status, reason, page):
    page.evaluate("_ => {}",
                  "browserstack_executor: {\"action\": \"setSessionStatus\", \"arguments\": {\"status\":\"" + status + "\", \"reason\": \"" + reason + "\"}}");


with sync_playwright() as playwright:
    test_run_session(playwright)
