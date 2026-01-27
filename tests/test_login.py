import allure
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from utils.config import Config


@allure.epic("UI testing SwagLabs")
class TestLogin:
    """
    Class for grouping tests
    """

    @allure.feature("Successful login")
    @pytest.mark.parametrize(
        "user",
        ["standard_user", "performance_glitch_user"],
        ids=["Standard_User", "Slow_User"],
    )
    def test_successful_login(self, page: Page, user):
        login_page = LoginPage(page)
        login_page.visit(Config.BASE_URL)
        login_page.login(user, "secret_sauce")

        assert login_page.is_inventory_displayed()

    @allure.feature("Negative login")
    @pytest.mark.parametrize(
        "user, password, expected_error",
        [
            ("standard_user", "wrong_password", "Username and password do not match"),
            ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
            ("", "", "Username is required"),
        ],
        ids=["Wrong_Password", "Locked_User", "Empty_Fields"],
    )
    def test_negative_login(self, page: Page, user, password, expected_error):
        login_page = LoginPage(page)
        login_page.visit(Config.BASE_URL)
        if user or password:
            login_page.login(user, password)
        else:
            login_page.click_login()

        error = login_page.get_error_text()
        assert expected_error in error
