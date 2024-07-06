import time

import pytest

from pages.registration_page import RegistrationPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.api_util import ApiUtil
from pages.order_confirmation_page import OrderConfirmationPage

shared_data = {}


@pytest.mark.usefixtures("driver")
class TestEndToEndFlow:
    @pytest.fixture(autouse=True)
    def setup(self, driver, user_credentials):
        self.driver = driver
        self.user_credentials = user_credentials

    def test_tc1(self):
        # Creating instance of page object class to call and use the function
        registration_page = RegistrationPage(self.driver)

        # Navigating to the Create an Account page
        registration_page.open()
        print(f"\nNavigated to create account page")
        # Filling out the registration form
        registration_page.execute_acc_registration(self.user_credentials["first_name"],
                                                   self.user_credentials["last_name"], self.user_credentials["email"],
                                                   self.user_credentials["password"], self.user_credentials["password"])
        time.sleep(2)
        registration_page.submit_info()
        print(f"New user registered successfully")
        time.sleep(2)

    def test_tc2(self):
        registration_page = RegistrationPage(self.driver)
        # Verify user registered successfully and logged in
        verification_txt = registration_page.registration_verification_msg_displayed()
        assert verification_txt, "Verification text is not displayed"
        print("Verified text:", verification_txt)
        print(f"Verifying User is now logged In")

    def test_tc3(self):
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
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
        shared_data['api_url'] = self.driver.current_url
        print(f"Current URL: {shared_data['api_url']}")

    def test_tc4(self):
        print(f"Current API URL before GET request: {shared_data.get('api_url')}")
        # API verification
        # Make a GET request to the purchase confirmation URL
        response = ApiUtil.get(shared_data.get('api_url'))
        # Print the response details
        if response:
            print(f"Status Code: {response.status_code}")
        else:
            print("Failed to get a response from the server")
        # Verify the status code is 200
        assert response is not None, "Failed to get a response from the server"
        ApiUtil.verify_status_code(response, 200)
        time.sleep(5)

    def test_tc5(self):
        order_confirmation_page = OrderConfirmationPage(self.driver)
        # Navigating to the Order details page
        order_confirmation_page.go_to_order_number_page_from_checkout_page()
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
