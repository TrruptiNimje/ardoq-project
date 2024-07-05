import time

import pytest

from pages.login_page import LoginPage
from pages.order_confirmation_page import OrderConfirmationPage


class TestPurchaseOrderDetails:
    @pytest.mark.registerAcc
    def test_purchase_order_details(self, driver, user_credentials):
        # Creating instance of page object class to call and use the function
        login_page = LoginPage(driver)
        order_confirmation_page = OrderConfirmationPage(driver)

        # Navigating to the SignIn page
        login_page.open()
        print(f"\nNavigated to Sign In page")
        # Executing and verifying successful login
        login_page.execute_login(user_credentials["email"], user_credentials["password"])
        time.sleep(2)
        print(f"Verify Logged-in successfully")

        # Navigating to the Order details page
        order_confirmation_page.go_to_order_number_page()
        # Verifying Pending status
        status = order_confirmation_page.verify_status()
        assert status == "PENDING", "Status is not displayed as Pending"
        print(f"Status is ", status)
        # Verifying price tab is visible
        order_confirmation_page.price_tab_displayed()
        assert order_confirmation_page.price_tab_displayed(), "Price tab is not displayed"
        print("Price tab is visible")
        # Verifying product price
        price = order_confirmation_page.product_pricing()
        assert price == ('$42.00', '$39.00'), "Amount does not match"
        print("Price verification for each product is successful", price)
        # Verify Grand total row is displayed
        order_confirmation_page.grand_total_row_displayed()
        assert order_confirmation_page.grand_total_row_displayed(), "Grand total row is not displayed"
        print("Grand total tab is visible")
        # Verify total price
        order_confirmation_page.total_price()
        assert order_confirmation_page.total_price() == "$81.00", "Amount does not match"
        print("Total Price verification is successful")
        print(f"Order details verified successfully")
