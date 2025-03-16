from typing import Type
from playwright.sync_api import sync_playwright
from infra.page_base import PageBase


class Browser:
    browser = None
    context = None
    page = None
    popup = None

    def __init__(self):

        playwright = sync_playwright().start()
        available_devices = playwright.devices
        print("Available devices:", available_devices)

        # Choose the correct device name, for example, 'iPhone 12 Pro Max'
        device_name = 'iPhone 12 Pro Max'
        device = available_devices[device_name]

        self.browser = playwright.chromium.launch(headless=False,slow_mo=500)
        self.context = self.browser.new_context(**device, ignore_https_errors=True)
        self.context.tracing.start(screenshots=True, snapshots=True)
        self.page = self.context.new_page()



    def navigate(self, address, page_type: Type[PageBase]):
        self.page.goto(address, wait_until="load")
        self.page.evaluate("localStorage.clear()")
        self.page.reload()
        return self.create_page(page_type)

    def create_page(self, page_type):
        return page_type(self.page)

    def create_popup(self, popup, new_popup):
        self.popup = popup
        return new_popup(self.popup)

    def stop_trace(self):
        self.context.tracing.stop(path="trace.zip")


