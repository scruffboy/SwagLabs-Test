import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page

        allure.attach(
            page.screenshot(),
            name="Final Screen",
            attachment_type=allure.attachment_type.PNG,
        )
        browser.close()
