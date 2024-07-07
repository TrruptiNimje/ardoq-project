** Magento Web and API test automation Project** 
  Test automation project for https://magento.softwaretestingboard.com/ website.
  
*Following are the test cases covered*
Test Cases:
TC1: Successfully register a new account at Account Creation Link. This test should simulate a user filling out the registration form and submitting it.
TC2: Verify that the account was created successfully by ensuring that the 'My Account' page is displayed after registration. This involves checking for specific elements or messages that confirm the user is logged in.
TC3: Complete the entire end-to-end process by purchasing the following products:
    ○ Men > Tops > Jackets > Beaumont Summit Kit (Red, and size large)
    ○ Men > Tops > Tees > Strike Endurance Tee (Black, and size large)
TC4: Verify the API call once the purchase is complete. For example, check that this request URL returns the correct status code (e.g., 200 OK) once the purchase is complete -> Request URL: https://magento.softwaretestingboard.com/checkout/onepage/success/
TC5: Click on the order number and verify the purchase using assertions. TC5: Verification example - Check that the highlighted items are visible


1. test_all_test_case.py:-  is the main test where it covers all end to end functionality check in one go, plus API verification.
2. Other test files are just divided in a way to run each function at a time.
3. reports directory:- This holds the reports generated for the test run, this report can be opened in any web browser.


** Note: Registering a user first is mandatory as per the test flow I have writen. 
To make the happy flow work seamless just change the Email ID in conftest.py every time before running the test **  
