from pages.base_page import BasePage
from pages.locators import CustomerLocators


class ChangepasswordPage(BasePage):
    def should_be_old_password_field(self):
        assert self.is_element_present(*CustomerLocators.OLD_PASS_FIELD), 'old password field not presented'

    def should_be_new_password_field(self):
        assert self.is_element_present(*CustomerLocators.NEW_PASS_FIELD), 'old password field not presented'

    def should_be_confirm_password_field(self):
        assert self.is_element_present(*CustomerLocators.CONFIRM_PASS_FIELD), 'confirm password field not presented'

    def should_be_change_password_button(self):
        assert self.is_element_present(*CustomerLocators.CHANGE_PASS_BUTTON), 'change password button not presented'

    def should_be_change_pass_result(self):
        assert self.is_element_present(*CustomerLocators.CHANGE_PASS_RESULT), 'change password result not presented'

    def change_password(self, password, new_password):
        self.browser.find_element(*CustomerLocators.OLD_PASS_FIELD).send_keys(password)
        self.browser.find_element(*CustomerLocators.NEW_PASS_FIELD).send_keys(new_password)
        self.browser.find_element(*CustomerLocators.CONFIRM_PASS_FIELD).send_keys(new_password)
        self.browser.find_element(*CustomerLocators.CHANGE_PASS_BUTTON).click()