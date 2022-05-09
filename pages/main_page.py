from pages.base_page import BasePage
from pages.locators import HeadersLocators


class MainPage(BasePage):
    def should_be_register_button(self):
        assert self.is_element_present(*HeadersLocators.REGISTER_BUTTON), 'Register button not present'

    def should_be_login_button(self):
        assert self.is_element_present(*HeadersLocators.LOGIN_LINK), 'Login button is not present'

    def should_be_cart_button(self):
        assert self.is_element_present(*HeadersLocators.CART_LINK), 'Cart button is not present'

    def should_be_wishlist_button(self):
        assert self.is_element_present(*HeadersLocators.WISHLIST_BUTTON), 'Wishlist button is not present'