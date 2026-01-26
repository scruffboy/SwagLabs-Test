import allure
from playwright.sync_api import Page
from tools.logger import get_logger
from .base_page import BasePage

logger = get_logger("LOGIN_PAGE")


class LoginPage(BasePage):
    """
    Class for work with LoginPage
    """

    def __init__(self, page: Page):
        super().__init__(page)

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"
        self.inventory_container = "#inventory_container"

    @allure.step("Click login button")
    def click_login(self):
        logger.debug("Clicking login button")
        self.page.click(self.login_button)
        return self

    @allure.step("Confirm login with '{username}'")
    def login(self, username: str, password: str):
        logger.info(f"Login to user account: {username}")
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.click_login()
        return self

    @allure.step("Get error message text")
    def get_error_text(self) -> str | None:
        if self.page.is_visible(self.error_message):
            text = self.page.text_content(self.error_message)
            logger.info(f"Error found: {text}")
            return text
        logger.debug("No error message found")
        return None

    @allure.step("Check if inventory page is displayed")
    def is_inventory_displayed(self) -> bool:
        return self.page.is_visible(self.inventory_container)
