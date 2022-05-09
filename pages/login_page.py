from pages.locators import LoginLocators
from pages.locators import HeadersLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_email_field(self):
        assert self.is_element_present(*LoginLocators.EMAIL_FIELD), "Email field not presented"

    def should_be_password_field(self):
        assert self.is_element_present(*LoginLocators.PASSWORD_FIELD), "Password field not presented"

    def should_be_login_button(self):
        assert self.is_element_present(*LoginLocators.LOGIN_BUTTON), 'Login button not presented'

    def login(self, email, password):
        self.browser.find_element(*LoginLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def should_be_login_result_page(self):
        assert self.browser.find_element(*HeadersLocators.ACCOUNT_BUTTON), 'Not logged in'