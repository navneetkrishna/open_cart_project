import pytest
from selenium import webdriver
from utilities import read_properties
from utilities.custom_logger import LogGen


# session-level scope ensures one driver per test session
# Autouse: Not autouse > since autouse is not specified (or implicitly False), this fixture will not run automatically.
# It must be explicitly requested by test functions that need it.
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

    yield logger


@pytest.fixture(scope="session", autouse=True)
def setup(driver, logger):
    # parameter driver is a fixture from conftest module

    url = read_properties.ReadConfig.get_application_URL()
    driver.get(url)
    driver.maximize_window()
    logger.info(f'Loading URL: {url} and launching browser')

    yield driver, logger

# Since autouse is set to True, this fixture will be automatically invoked for every test without needing to be
# explicitly requested by a test method.
# This means that as soon as the session starts, the setup fixture will run,
# and the driver and logger will be set up and available for the duration of the session.
