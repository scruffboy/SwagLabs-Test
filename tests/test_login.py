import allure
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from utils.config import Config
from tests.data import AuthData


@allure.epic("UI testing SwagLabs")
class TestLogin:
    """
    Class for grouping tests
    """

    @allure.feature("Successful login")
    @pytest.mark.parametrize(
        "user",
        AuthData.SUCCESSFUL_USERS,
        ids=["Standard_User", "Slow_User"],
    )
    def test_successful_login(self, page: Page, user: str):
        login_page = LoginPage(page)
        login_page.visit(Config.BASE_URL)
        login_page.login(user, "secret_sauce")

        assert login_page.is_inventory_displayed()

    @allure.feature("Negative login")
    @pytest.mark.parametrize(
        "user, password, expected_error",
        AuthData.NEGATIVE_LOGIN_SCENARIOS,
        ids=["Wrong_Password", "Locked_User", "Empty_Fields"],
    )
    def test_negative_login(self, page: Page, user: str, password: str, expected_error):
        login_page = LoginPage(page)
        login_page.visit(Config.BASE_URL)
        if user or password:
            login_page.login(user, password)
        else:
            login_page.click_login()

        error = login_page.get_error_text()
        assert expected_error in error
