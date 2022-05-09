import allure
import pytest

from pages.change_password_page import ChangepasswordPage
from pages.dataset import TestDatasets, register_dataset
from pages.locators import LinksLocators
from pages.login_page import LoginPage
from pages.registration_page import RegisterPage


@allure.feature('Change password test')
class TestChangePasswordPage:
    @allure.story('Setup')
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        first_name, last_name, email, password = register_dataset()
        page.register_new_user(first_name, last_name, email, password)
        page.should_be_register_result_page()
        page.log_out()
        return email, password

    @allure.story('Checking password change smoke')
    @pytest.mark.smoke
    def test_change_password(self, browser, setup):
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email=setup[0], password=setup[1])
        page = ChangepasswordPage(browser, LinksLocators.CHANGE_PASS_LINK)
        page.open()
        page.change_password(password=setup[1], new_password=TestDatasets.new_password)
        page.should_be_change_pass_result()

    @allure.story('Checking fields change password')
    @pytest.mark.fields
    def test_fields_change_password_page(self, browser, setup):
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email=setup[0], password=setup[1])
        page = ChangepasswordPage(browser, LinksLocators.CHANGE_PASS_LINK)
        page.open()
        page.should_be_old_password_field()
        page.should_be_new_password_field()
        page.should_be_confirm_password_field()
        page.should_be_change_password_button()