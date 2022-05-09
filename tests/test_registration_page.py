import pytest
import allure
from pages.locators import LinksLocators
from pages.registration_page import RegisterPage
from pages.dataset import register_dataset


@pytest.mark.fields
class TestRegistrationPageFields:
    @allure.story('Checking checkboxes')
    def test_gender_checkbox(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_gender_radiobuttons()

    @allure.story('Checking the name field')
    def test_first_name_field(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_firstname_field()

    @allure.story('Checking the last name field')
    def test_last_name_field(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_lastname_field()

    @allure.story('Checking the email field')
    def test_email_field(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_email_field()

    @allure.story('Checking the password field')
    def test_password_field(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_password_field()

    @allure.story('Checking confirm password field ')
    def test_confirm_password_field(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_confirm_password_field()

    @allure.story('Checking the register button')
    def test_should_see_register_button(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_register_button()


@allure.feature('Registration new user(smoke)')
@pytest.mark.smoke
class TestRegistrationNewUser:
    def test_registration_new_user(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        first_name, last_name, email, password = register_dataset()
        page.register_new_user(first_name, last_name, email, password)
        page.should_be_register_result_page()
