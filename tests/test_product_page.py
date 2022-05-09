import pytest
import allure

from pages.dataset import register_dataset
from pages.locators import LinksLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.registration_page import RegisterPage


@allure.feature('Product page fields')
@pytest.mark.fields
class TestProductPageFields:
    @allure.story('Checking the correct link to all products')
    def test_correct_books_link(self, browser):
        page = ProductPage(browser, LinksLocators.BOOKS_LINK)
        page.open()
        page.should_be_correct_books_link()

    @allure.story('Checking the correct link to the health book')
    def test_correct_item_link(self, browser):
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.should_be_correct_item_link()

    @allure.story('Checking the button to add a product')
    def test_adding_button(self, browser):
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.should_be_adding_button()


@allure.feature('Adding item to cart(smoke)')
@pytest.mark.smoke
class TestAddingItemToCart:
    @allure.story('Adding a product from the product details page')
    def test_adding_item_to_cart(self, browser):
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.press_button_add_to_cart()
        page.should_be_success_adding_massage()

    @allure.story('Adding a product from the Product list page')
    def test_adding_item_from_all_product(self, browser):
        page = ProductPage(browser, LinksLocators.BOOKS_LINK)
        page.open()
        page.press_button_add_from_all_books()
        page.should_be_success_adding_massage()


@allure.feature('Checkout order(smoke)')
@pytest.mark.smoke
class TestCheckoutOrder:
    @allure.story('setup')
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        first_name, last_name, email, password = register_dataset()
        page.register_new_user(first_name, last_name, email, password)
        page.should_be_register_result_page()
        page.log_out()
        return email, password

    @allure.story('Checking the order and login on new data')
    def test_checkout_order_with_login(self, browser, setup):
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email=setup[0], password=setup[1])
        page.should_be_login_result_page()
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.press_button_add_to_cart()
        page.should_be_success_adding_massage()
        page.press_go_to_cart_button()
        page.change_quantity_of_item()
        page.press_update_cart_button()
        page.press_to_agree_checkbox()
        page.press_to_checkout_button()
        page.making_order()
        page.should_be_confirm_order_result_page()