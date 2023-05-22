import asyncio

import pytest
from playwright.sync_api import Playwright, Page, sync_playwright

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        new_page = browser.new_page()

        yield new_page
        browser.close()



