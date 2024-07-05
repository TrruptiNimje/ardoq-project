import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    __url = "https://magento.softwaretestingboard.com/customer/account/create/"
    __first_name_field = (By.ID, "firstname")
    __last_name_field = (By.ID, "lastname")
    __email_address_field = (By.ID, "email_address")
    __password_field = (By.ID, "password")
    __confirm_password_field = (By.ID, "password-confirmation")
    __create_acc_btn = (By.CSS_SELECTOR, "button[title='Create an Account']")
    __successfully_registered_msg = (By.XPATH, "//div[contains(text(),'Thank you for registering with Main Website Store.')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_acc_registration(self, first_name: str, last_name: str, email: str, password: str, confm_password: str):
        super()._type(self.__first_name_field, first_name)
        time.sleep(1)
        super()._type(self.__last_name_field, last_name)
        time.sleep(1)
        super()._type(self.__email_address_field, email)
        time.sleep(1)
        super()._type(self.__password_field, password)
        time.sleep(1)
        super()._type(self.__confirm_password_field, confm_password)

    def submit_info(self):
        super()._click(self.__create_acc_btn)

    def registration_verification_msg_displayed(self) -> str:
        return super()._get_text(self.__successfully_registered_msg)
