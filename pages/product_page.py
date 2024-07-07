import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ProductPage(BasePage):
    __men_category = (By.XPATH, "//span[contains(text(),'Men')]")
    __jackets = (By.LINK_TEXT, "Jackets")
    __beaumont_jacket = (By.PARTIAL_LINK_TEXT, "Beaumont Summit K")
    __jacket_size = (By.XPATH, "//body/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[11]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]")
    __jacket_color = (By.XPATH, "//body/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[11]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]")
    __jacket_add_to_cart = (By.XPATH, "//body/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[11]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/button[1]/span[1]")
    __product_added_to_cart_msg = (By.XPATH, "//a[contains(text(),'shopping cart')]")
    __tees = (By.LINK_TEXT, "Tees")
    __strike_tee = (By.PARTIAL_LINK_TEXT, "Strike Endurance T")
    __tee_size = (By.XPATH, "//body/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]")
    __tee_color = (By.XPATH, "//body/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]")
    __tee_add_to_cart = (By.XPATH, "//body[1]/div[2]/main[1]/div[3]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/div[4]/div[1]/div[1]/form[1]/button[1]/span[1]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def execute_first_purchase(self):
        super()._click(self.__men_category)
        time.sleep(2)
        super()._click(self.__jackets)
        time.sleep(2)
        super()._wait_until_element_is_visible(self.__beaumont_jacket)
        time.sleep(5)
        super()._click(self.__jacket_size)
        time.sleep(2)
        super()._click(self.__jacket_color)
        time.sleep(2)
        super()._click(self.__jacket_add_to_cart)
        time.sleep(10)

    def product_added_to_cart_msg_displayed(self) -> str:
        return super()._get_text(self.__product_added_to_cart_msg)
    time.sleep(5)

    def execute_second_purchase(self):
        super()._click(self.__men_category)
        time.sleep(2)
        super()._click(self.__tees)
        time.sleep(2)
        super()._wait_until_element_is_visible(self.__strike_tee)
        time.sleep(5)
        super()._click(self.__tee_size)
        super()._click(self.__tee_color)
        super()._click(self.__tee_add_to_cart)
        time.sleep(5)
