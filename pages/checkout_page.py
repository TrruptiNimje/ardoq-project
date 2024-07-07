import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    __shipping_address_header = (By.XPATH, "//div[contains(text(),'Shipping Address')]")
    __address_field = (By.XPATH,
                       "//body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/input[1]")
    __city_field = (By.XPATH,
                    "//body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[4]/div[1]/input[1]")
    __state_field = (By.XPATH,
                     "//body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[5]/div[1]/select[1]")
    __zip_code_field = (By.XPATH,
                        "//body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[7]/div[1]/input[1]")
    __country_field = (By.XPATH,
                       "//body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[8]/div[1]/select[1]")
    __phone_no_field = (By.XPATH,
                        "//body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[9]/div[1]/input[1]")
    __order_summery = (
        By.XPATH, "//body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/aside[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
    __jacket_product = (By.XPATH, "//strong[contains(text(),'Beaumont Summit Kit')]")
    __tee_product = (By.XPATH, "//strong[contains(text(),'Strike Endurance Tee')]")
    __shipping_method = (By.CSS_SELECTOR,
                         "body.checkout-index-index.page-layout-checkout:nth-child(2) div.page-wrapper:nth-child(5) main.page-main div.columns:nth-child(3) div.column.main div.checkout-container:nth-child(3) div.opc-wrapper:nth-child(5) ol.opc li.checkout-shipping-method div.checkout-shipping-method div.step-content form.form.methods-shipping table.table-checkout-shipping-method tbody:nth-child(2) tr.row:nth-child(1) td.col.col-method:nth-child(1) > input.radio")
    __next_btn = (By.XPATH, "//span[contains(text(),'Next')]")
    __place_order_btn = (By.XPATH, "//span[contains(text(),'Place Order')]")
    __payment_order_summary = (By.XPATH, "//span[contains(text(),'Order Summary')]")
    __order_confirmation = (By.XPATH, "//span[contains(text(),'Thank you for your purchase!')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def checkout_process(self, address: str, city: str, zipcode: int, phoneno: int):
        super()._wait_until_element_is_visible(self.__shipping_address_header)
        time.sleep(2)
        super()._click(self.__order_summery)
        time.sleep(2)
        super()._wait_until_element_is_visible(self.__jacket_product)
        super()._wait_until_element_is_visible(self.__tee_product)
        time.sleep(2)
        super()._type(self.__address_field, address)
        time.sleep(2)
        super()._type(self.__city_field, city)
        time.sleep(2)
        super()._click_drop_down(self.__state_field)
        time.sleep(2)
        super()._select_dropdown_by_value(self.__state_field, "12")
        time.sleep(2)
        super()._type(self.__zip_code_field, zipcode)
        time.sleep(2)
        super()._click_drop_down(self.__country_field)
        time.sleep(2)
        super()._select_dropdown_by_value(self.__country_field, "US")
        time.sleep(2)
        super()._type(self.__phone_no_field, phoneno)
        time.sleep(2)
        super()._click(self.__shipping_method)
        time.sleep(2)
        super()._click(self.__next_btn)
        time.sleep(5)
        super()._is_displayed(self.__payment_order_summary)
        super()._click(self.__place_order_btn)
        time.sleep(10)
        super()._wait_until_element_is_visible(self.__order_confirmation)
        time.sleep(10)
