import allure
from typing import Pattern
from playwright.sync_api import Page, expect
from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    """
    Base class for all PageObject
    """

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        """
        Opens a page at url and waits for complete loading
        """
        step = f"Opening the url '{url}'"

        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle")

    def reload(self):
        """
        Reloads the page and waits DOM loading
        """
        step = f"Reloading page with url '{self.page.url}'"

        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        """
        Checks the current url mathes pattern
        """
        step = f"Checking the current url matches pattern '{expected_url.pattern}'"

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
