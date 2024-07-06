import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    # Setup: Initialize the WebDriver instance
    print("Creating Chrome driver")
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    my_driver.implicitly_wait(20)
    yield my_driver
    # Teardown: Close the WebDriver instance
    print("Closing Chrome driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (only chrome supported)"
    )


@pytest.fixture(scope="session")
def user_credentials():
    return {
        "first_name": "Tom",
        "last_name": "Cruise",
        "email": "tomcruise72@mail.com",
        "password": "Qwer@1234"
    }
