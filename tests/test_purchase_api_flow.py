import time

import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.api_util import ApiUtil


class TestPurchasingProducts:
    @pytest.mark.purchase
    def test_purchasing_product(self, driver, user_credentials):
        # Creating instance of page object class to call and use the function
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Navigating to the SignIn page
        login_page.open()
        print(f"\nNavigated to Sign In page")
        # Executing and verifying successful login
        login_page.execute_login(user_credentials["email"], user_credentials["password"])
        time.sleep(2)
        print(f"Verify Logged-in successfully")

        # Execute and verify purchase of first product
        product_page.execute_first_purchase()
        assert product_page.product_added_to_cart_msg_displayed(), "Verification text is not displayed"
        print(f"Jacket added to cart successfully")
        # Execute and verify purchase of second product
        product_page.execute_second_purchase()
        assert product_page.product_added_to_cart_msg_displayed(), "Verification text is not displayed"
        print(f"Tees added to cart successfully")
        # Proceed to Checkout page through cart
        cart_page.go_to_cart()
        time.sleep(5)
        print(f"Successfully navigated to checkout page")
        # Completing Checkout process
        checkout_page.checkout_process("High street", "OldYork", "52345-6789", "273582758")
        time.sleep(2)
        print(f"Successfully completed filling out the checkout form and Navigated to Payments page")
        current_api_url = driver.current_url
        print(f"Current URL: {current_api_url}")

        # API verification
        # Make a GET request to the purchase confirmation URL
        response = ApiUtil.get(current_api_url)
        # Print the response details
        if response:
            print(f"Status Code: {response.status_code}")
        else:
            print("Failed to get a response from the server")
        # Verify the status code is 200
        assert response is not None, "Failed to get a response from the server"
        ApiUtil.verify_status_code(response, 200)
        time.sleep(5)
