import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class OrderConfirmationPage(BasePage):
    __welcome_user_link_home_page = (By.CSS_SELECTOR, "body.cms-home.cms-index-index.page-layout-1column:nth-child(2) div.page-wrapper:nth-child(5) header.page-header div.panel.wrapper div.panel.header ul.header.links li.customer-welcome span.customer-name > button.action.switch")
    __welcome_user_link_checkout_page = (By.CSS_SELECTOR, "body.checkout-onepage-success.page-layout-1column:nth-child(2) div.page-wrapper:nth-child(5) header.page-header div.panel.wrapper div.panel.header ul.header.links li.customer-welcome span.customer-name > button.action.switch")
    __my_account_link_home_page = (By.CSS_SELECTOR, "body.cms-home.cms-index-index.page-layout-1column:nth-child(2) div.page-wrapper:nth-child(5) header.page-header div.panel.wrapper div.panel.header ul.header.links li.customer-welcome.active div.customer-menu ul.header.links li:nth-child(1) > a:nth-child(1)")
    __my_account_link_checkout_page = (By.CSS_SELECTOR, "body.checkout-onepage-success.page-layout-1column:nth-child(2) div.page-wrapper:nth-child(5) header.page-header div.panel.wrapper div.panel.header ul.header.links li.customer-welcome.active div.customer-menu ul.header.links li:nth-child(1) > a:nth-child(1)")
    __view_order_link = (By.CSS_SELECTOR, "body.account.customer-account-index.page-layout-2columns-left:nth-child(2) div.page-wrapper:nth-child(5) main.page-main div.columns:nth-child(3) div.column.main:nth-child(1) div.block.block-dashboard-orders:nth-child(6) div.block-content div.table-wrapper.orders-recent table.data.table.table-order-items.recent tbody:nth-child(3) tr:nth-child(1) td.col.actions:nth-child(6) a.action.view:nth-child(1) > span:nth-child(1)")
    __pending_status = (By.XPATH, "//span[contains(text(),'Pending')]")
    __price_tab = (By.XPATH, "//th[contains(text(),'Price')]")
    __jacket_price = (By.XPATH, "//body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[3]/span[1]/span[1]/span[1]")
    __tee_price = (By.XPATH, "//body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[2]/tr[1]/td[3]/span[1]/span[1]/span[1]")
    __grand_total = (By.XPATH, "//strong[contains(text(),'Grand Total')]")
    __total_price = (By.CSS_SELECTOR, "body.account.sales-order-view.page-layout-2columns-left:nth-child(2) div.page-wrapper:nth-child(5) main.page-main div.columns:nth-child(3) div.column.main:nth-child(1) div.order-details-items.ordered:nth-child(3) div.table-wrapper.order-items table.data.table.table-order-items tfoot:nth-child(5) tr.grand_total td.amount strong:nth-child(1) > span.price")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_order_number_page(self):
        super()._click_drop_down(self.__welcome_user_link_home_page)
        time.sleep(5)
        super()._click(self.__my_account_link_home_page)
        time.sleep(5)
        super()._click(self.__view_order_link)
        time.sleep(10)

    def go_to_order_number_page_from_checkout_page(self):
        super()._click_drop_down(self.__welcome_user_link_checkout_page)
        time.sleep(5)
        super()._click(self.__my_account_link_checkout_page)
        time.sleep(5)
        super()._click(self.__view_order_link)
        time.sleep(10)

    def verify_status(self) -> str:
        return super()._get_text(self.__pending_status)

    def price_tab_displayed(self) -> bool:
        return super()._is_displayed(self.__price_tab)

    def product_pricing(self) -> str:
        jacket = super()._get_text(self.__jacket_price)
        tee = super()._get_text(self.__tee_price)
        return jacket, tee

    def grand_total_row_displayed(self) -> bool:
        return super()._is_displayed(self.__grand_total)

    def total_price(self) -> str:
        total = super()._get_text(self.__total_price)
        return total
