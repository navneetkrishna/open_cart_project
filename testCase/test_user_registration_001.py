import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from testCase.conftest import driver
from utilities import read_properties, random_email_generator
from utilities.custom_logger import LogGen
from pages import my_account, ecommerce_homepage


class TestNewUserRegistration:

    # for logging
    logger = LogGen.loggen()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):

        # parameter driver is a fixture from conftest module
        self.driver = driver
        url = read_properties.ReadConfig.get_application_URL()
        driver.get(url)
        self.driver.maximize_window()
        self.logger.info(f'Loading URL: {url} and launching browser')
        self.driver.maximize_window()

        # Navigate to home page > my account
        home_page = ecommerce_homepage.HomePage(self.driver)
        self.logger.debug('Homepage object created')

        home_page.click_my_account()

    # invalid registration > empty password
    @pytest.mark.negative
    def test_invalid_register_user(self, driver):

        self.logger.info(f'---------------------invalid registration--------------')
        self.logger.info(f'Executing test_invalid_register_user')

        # User registration process
        my_account_page = my_account.Registration(self.driver)
        self.logger.debug('My Account page object created')

        # Generate random email address
        email = random_email_generator.generate_email()
        self.logger.debug(f'Registering user with email: {email}')

        my_account_page.enter_email(email)
        # my_account_page.enter_password()
        my_account_page.click_register()

        # self.logger.debug(f'Email {email} has been registered')

        # Validating if the user has been registered successfully
        try:
            error_txt = WebDriverWait(self.driver, 10).until(
                presence_of_element_located((By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/ul[1]/li[1]"))
            )

            expected_error = 'Error: Please enter an account password.'

            assert error_txt.text == expected_error
            self.logger.debug(f'Invalid user registration, no password found for {email}')
            self.logger.info(f'test case ID:{__name__} has been executed successfully, test result: PASS')

        except Exception as e:
            self.logger.error(f'Invalid user registration, user {email} registered without password, {e}')
            self.logger.info(f'test case ID:{__name__} has been executed successfully, test result: FAIL')

            raise

    # valid registration operation
    @pytest.mark.smoke
    def test_valid_register_user(self, driver):

        self.logger.info(f'---------------------valid registration--------------')
        self.logger.info(f'Executing test_valid_register_user')

        # User registration process
        my_account_page = my_account.Registration(self.driver)
        self.logger.debug('My Account page object created')

        # Generate random email address
        email = random_email_generator.generate_email()
        self.logger.debug(f'Registering user with email: {email}')

        my_account_page.enter_email(email)
        my_account_page.enter_password()
        my_account_page.click_register()

        self.logger.debug(f'Email {email} has been registered')

        # Validating if the user has been registered successfully
        try:
            recent_orders_link = WebDriverWait(self.driver, 10).until(
                presence_of_element_located((By.XPATH, "//a[contains(text(),'recent orders')]"))
            )
            assert recent_orders_link.text == "recent orders"
            self.logger.debug('User registration validated successfully')
            self.logger.info(f'test case ID:{__name__} has been executed successfully, test result: PASS')

        except Exception as e:
            self.logger.error(f'Registration validation failed: {e}')
            self.logger.info(f'test case ID:{__name__} has been executed successfully, test result: FAIL')

            raise
