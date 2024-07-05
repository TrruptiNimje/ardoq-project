import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class CartPage(BasePage):
    __cart_link = (By.CSS_SELECTOR, "body.page-with-filter.page-products.categorypath-men-tops-men-tees-men.category-tees-men.catalog-category-view.page-layout-2columns-left:nth-child(2) div.page-wrapper:nth-child(5) header.page-header div.header.content div.minicart-wrapper > a.action.showcart:nth-child(1)")
    __checkout_btn = (By.CSS_SELECTOR, "#top-cart-btn-checkout")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_cart(self):
        super()._click(self.__cart_link)
        time.sleep(2)
        super()._click(self.__checkout_btn)
        time.sleep(2)
