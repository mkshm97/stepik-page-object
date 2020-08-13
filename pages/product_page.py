from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Button is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_add_to_basket_message(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_message = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_MESSAGE).text
        assert book_price == book_price_message, "Price is not same"
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MESSAGE).text
        assert book_name == book_name_message, "Name is not same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"