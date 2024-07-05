import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://magento.softwaretestingboard.com/"
    __signin_link = (By.XPATH, "//body[1]/div[2]/header[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    __email_field = (By.CSS_SELECTOR, "#email")
    __password_field = (By.CSS_SELECTOR, "#pass")
    __signin_btn = (By.CSS_SELECTOR, "body.customer-account-login.page-layout-1column:nth-child(2) div.page-wrapper:nth-child(5) main.page-main div.columns:nth-child(4) div.column.main div.login-container:nth-child(3) div.block.block-customer-login:nth-child(1) div.block-content form.form.form-login fieldset.fieldset.login:nth-child(2) div.actions-toolbar:nth-child(4) div.primary button.action.login.primary > span:nth-child(1)")
    __welcome_txt = (By.CSS_SELECTOR, "body.cms-home.cms-index-index.page-layout-1column:nth-child(2) div.page-wrapper:nth-child(5) header.page-header div.panel.wrapper div.panel.header ul.header.links li.greet.welcome > span.logged-in")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, email: str, password: str):
        super()._click(self.__signin_link)
        time.sleep(2)
        super()._type(self.__email_field, email)
        time.sleep(2)
        super()._type(self.__password_field, password)
        time.sleep(2)
        super()._click(self.__signin_btn)
        time.sleep(5)
        assert super()._is_displayed(self.__welcome_txt)
