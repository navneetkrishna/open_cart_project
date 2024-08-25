import pytest
from selenium import webdriver

from utilities.custom_logger import LogGen


# session-level scope ensures one driver per test session
@pytest.fixture(scope="session")
def driver(request):
    # Get browser option from command line (optional)
    browser = request.config.getoption("--browser")

    # Default browser: chrome (if not specified)
    if not browser:
        browser = "chrome"

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Yield the driver for tests to use
    yield driver

    # Teardown: close the browser after tests
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Browser to run tests with, e.g., chrome or edge")

@pytest.fixture(scope='session')
def logger():

    logger = LogGen.loggen()

    return logger
