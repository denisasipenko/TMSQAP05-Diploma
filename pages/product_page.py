import time


from pages.locators import ItemsPageLocators, HeadersLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from pages.dataset import TestDatasets


class ProductPage(BasePage):
    def should_be_adding_button(self):
        assert self.is_element_present(*ItemsPageLocators.ADD_TO_CART_BUTTON), 'Adding to cart button not presented'

    def should_be_correct_books_link(self):
        expected_url = 'http://demowebshop.tricentis.com/books'
        actual_url = self.browser.current_url
        assert expected_url == actual_url, 'The link to all books is incorrect'

    def should_be_correct_item_link(self):
        expected_url = 'http://demowebshop.tricentis.com/health'
        actual_url = self.browser.current_url
        assert expected_url == actual_url, 'The link to the product is incorrect'

    def should_be_success_adding_massage(self):
        assert self.is_element_present(
            *ItemsPageLocators.SUCCESS_ADDING_MASSAGE), 'The addition of the product did not happen'

    def press_button_add_to_cart(self):
        self.browser.find_element(*ItemsPageLocators.ADD_TO_CART_BUTTON).click()

    def press_button_add_from_all_books(self):
        self.browser.find_element(*ItemsPageLocators.ADD_TO_CART_FROM_ALL_PRODUCT).click()

    def change_quantity_of_item(self):
        self.browser.find_element(*ItemsPageLocators.QUANTITY_ITEMS_FIELD).click()
        self.browser.find_element(*ItemsPageLocators.QUANTITY_ITEMS_FIELD).send_keys('10')

    def press_update_cart_button(self):
        self.browser.find_element(*ItemsPageLocators.UPDATE_CART_BUTTON).click()

    def press_go_to_cart_button(self):
        self.browser.find_element(*HeadersLocators.CART_LINK).click()

    def press_to_agree_checkbox(self):
        self.browser.find_element(*ItemsPageLocators.AGREE_CHECKBOX).click()

    def press_to_checkout_button(self):
        self.browser.find_element(*ItemsPageLocators.CHECKOUT_BUTTON).click()

    def making_order(self):
        select = Select(self.browser.find_element_by_tag_name("select"))
        select.select_by_value("66")
        self.browser.find_element(*ItemsPageLocators.CITY_ORDER_FIELD).send_keys(TestDatasets.city)
        self.browser.find_element(*ItemsPageLocators.ADDRESS1_ORDER_FIELD).send_keys(TestDatasets.address1)
        self.browser.find_element(*ItemsPageLocators.ZIP_CODE_ORDER_FIELD).send_keys(TestDatasets.zip_code)
        self.browser.find_element(*ItemsPageLocators.PHONE_ORDER_FIELD).send_keys(TestDatasets.phone)
        self.browser.find_element(*ItemsPageLocators.NEW_ADDRESS_CONTINUE_BUTTON).click()
        self.browser.find_element(*ItemsPageLocators.PICKUP_CHECKBOX).click()
        self.browser.find_element(*ItemsPageLocators.SHIPPING_ADDRESS_CONTINUE_BUTTON).click()
        self.browser.find_element(*ItemsPageLocators.PAYMENT_METHOD_RADIOBUTTON).click()
        self.browser.find_element(*ItemsPageLocators.PAYMENT_CONTINUE_BUTTON).click()
        self.browser.find_element(*ItemsPageLocators.PAYMENT_INFO_CONTINUE_BUTTON).click()
        self.browser.find_element(*ItemsPageLocators.CONFIRM_ORDER_BUTTON).click()
        time.sleep(1)

    def should_be_confirm_order_result_page(self):
        expected_url = 'http://demowebshop.tricentis.com/checkout/completed/'
        actual_url = self.browser.current_url
        assert expected_url == actual_url, 'Confirm order failed, please try again'