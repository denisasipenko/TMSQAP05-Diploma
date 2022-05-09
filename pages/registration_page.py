from pages.locators import RegisterLocators, HeadersLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def should_be_gender_radiobuttons(self):
        assert self.is_element_present(*RegisterLocators.MALE_RADIOBUTTON) \
               and self.is_element_present(*RegisterLocators.FEMALE_RADIOBUTTON), 'Gender radiobutton is not presented'

    def should_be_firstname_field(self):
        assert self.is_element_present(*RegisterLocators.FIRSTNAME_FIELD), 'Firstname field not presented'

    def should_be_lastname_field(self):
        assert self.is_element_present(*RegisterLocators.LASTNAME_FIELD), 'Lastname field not presented'

    def should_be_email_field(self):
        assert self.is_element_present(*RegisterLocators.EMAIL_FIELD), "Email field not presented"

    def should_be_password_field(self):
        assert self.is_element_present(*RegisterLocators.PASSWORD_FIELD), "Password field not presented"

    def should_be_confirm_password_field(self):
        assert self.is_element_present(*RegisterLocators.CONFIRM_PASSWORD_FIELD), "Confirm password field not presented"

    def should_be_register_button(self):
        assert self.is_element_present(*RegisterLocators.REGISTER_BUTTON), 'Register button not presented'

    def should_be_register_result_page(self):
        expected_url = 'http://demowebshop.tricentis.com/registerresult/1'
        actual_url = self.browser.current_url
        assert expected_url == actual_url, 'Registration failed, please try again'

    def log_out(self):
        self.browser.find_element(*HeadersLocators.LOG_OUT_LINK).click()

    def register_new_user(self, first_name, last_name, email, password):
        self.browser.find_element(*RegisterLocators.MALE_RADIOBUTTON).click()
        self.browser.find_element(*RegisterLocators.FIRSTNAME_FIELD).send_keys(first_name)
        self.browser.find_element(*RegisterLocators.LASTNAME_FIELD).send_keys(last_name)
        self.browser.find_element(*RegisterLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*RegisterLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*RegisterLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*RegisterLocators.REGISTER_BUTTON).click()