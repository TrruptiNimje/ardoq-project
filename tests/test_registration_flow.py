import time

import pytest

from pages.registration_page import RegistrationPage


class TestRegisterNewAcc:
    @pytest.mark.registerAcc
    def test_acc_registration(self, driver, user_credentials):
        # Creating instance of page object class to call and use the function
        registration_page = RegistrationPage(driver)

        # Navigating to the Create an Account page
        registration_page.open()
        print(f"\nNavigated to create account page")

        # Filling out the registration form
        registration_page.execute_acc_registration(user_credentials["first_name"], user_credentials["last_name"], user_credentials["email"], user_credentials["password"], user_credentials["password"])
        time.sleep(2)

        registration_page.submit_info()
        print(f"New user registered successfully")
        time.sleep(2)

        # Verify other element 'Thank you for registering.....'
        verification_txt = registration_page.registration_verification_msg_displayed()
        assert verification_txt, "Verification text is not displayed"
        print("Verified text:", verification_txt)
        print(f"Verifying User is now logged In")
