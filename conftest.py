import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    print("Creating Chrome driver")
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    my_driver.implicitly_wait(20)
    yield my_driver
    print("Closing Chrome driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (only chrome supported)"
    )


@pytest.fixture(scope="session")
def user_credentials():
    return {
        "first_name": "Ola",
        "last_name": "Richi",
        "email": "olarichi11@mail.com",
        "password": "Qwer@1234"
    }
