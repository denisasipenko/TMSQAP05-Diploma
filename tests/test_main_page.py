import pytest
import allure
from pages.locators import LinksLocators
from pages.main_page import MainPage


@allure.feature('Test main page links')
@pytest.mark.fields
class TestMainPageLinks:
    def test_basic_links(self, browser):
        page = MainPage(browser, LinksLocators.MAIN_PAGE_LINK)
        page.open()
        page.should_be_register_button()
        page.should_be_login_button()
        page.should_be_cart_button()
        page.should_be_wishlist_button()