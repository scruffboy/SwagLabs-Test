import allure
import pytest
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright


@allure.step("1. Successful login: 'standard_user'")
def test_successful_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.visit("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in page.url
        assert login_page.is_inventory_displayed()

        browser.close()


@allure.step("2. The login with incorrect password")
def test_wrong_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.visit("https://www.saucedemo.com/")
        login_page.login("standard_user", "wrong_password")

        error = login_page.get_error_text()
        assert error is not None
        assert "Username and password do not match" in error

        browser.close()


@allure.step("3. The locked login: 'locked_out_user'")
def test_locked_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.visit("https://www.saucedemo.com/")
        login_page.login("locked_out_user", "secret_sauce")

        error = login_page.get_error_text()
        assert error is not None
        assert " Sorry, this user has been locked out." in error

        browser.close()


@allure.step("4. The login with empty fields")
def test_empty_fields():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.visit("https://www.saucedemo.com/")
        login_page.click_login()

        error = login_page.get_error_text()
        assert error is not None
        assert "Username is required" in error

        browser.close()


@allure.step("5. The login: 'perfomance_glitch_user'")
def test_perfomance_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.visit("https://www.saucedemo.com/")
        login_page.login("performance_glitch_user", "secret_sauce")

        page.wait_for_timeout(2000)
        assert "inventory.html" in page.url
        assert login_page.is_inventory_displayed()

        browser.close()
