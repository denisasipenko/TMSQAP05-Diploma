import pytest
import allure
from pages.locators import LinksLocators
from pages.login_page import LoginPage
from pages.registration_page import RegisterPage
from pages.dataset import TestDatasets, register_dataset


@allure.feature('Login page fields ')
@pytest.mark.fields
class TestLoginPageFields:
    @allure.story('Checking if there is an email field')
    def test_email_field(self, browser):
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.should_be_email_field()

    @allure.story('Checking if there is a password field')
    def test_password_field(self, browser):
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.should_be_password_field()

    @allure.story('Checking if there is a login button')
    def test_login_button(self, browser):
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.should_be_login_button()


@allure.feature('Checking the login on ready-made data(smoke)')
@pytest.mark.smoke
class TestLogin:
    def test_login(self, browser):
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email=TestDatasets.email, password=TestDatasets.password)
        page.should_be_login_result_page()


@allure.feature('Login after registration')
@pytest.mark.smoke
class TestLoginAfterRegistration:
    @allure.story('Login verification for new random data')
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        first_name, last_name, email, password = register_dataset()
        page.register_new_user(first_name, last_name, email, password)
        page.should_be_register_result_page()
        page.log_out()
        return email, password

    @allure.story('Login')
    def test_login(self, browser, setup):
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email=setup[0], password=setup[1])
        page.should_be_login_result_page()