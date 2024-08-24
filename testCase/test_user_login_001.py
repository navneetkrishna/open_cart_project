import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from utilities import read_properties
from utilities.cutom_logger import LogGen
from pages import my_account, ecommerce_homepage


class TestUserLogin:
    # For logging
    logger = LogGen.loggen()

    # Fixture > scope = function > executed before each function
    # Fixture > autouse = True > executed before each function automatically (without needing to explicitly pass it as an argument.)
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        # parameter driver is a fixture from conftest module

        self.driver = driver
        url = read_properties.ReadConfig.get_application_URL()
        self.driver.get(url)
        self.driver.maximize_window()
        self.logger.info(f'Loading URL: {url} and launching browser')

        # Navigate to home page > my account
        home_page = ecommerce_homepage.HomePage(self.driver)
        home_page.click_my_account()
        self.logger.debug('Homepage object created')

    # Login with invalid email
    def test_invalid_login_invalid_email(self):
        self.logger.info('--------------------invalid login---------------------')
        self.logger.info('test_invalid_login_invalid_email')

        # User login process
        my_account_page = my_account.Login(self.driver)
        self.logger.debug('My Account page object created')

        # Providing invalid username & password
        email = 'username@invalid.com'
        password = 'invalid@pass'
        self.logger.debug(f'*Invalid email: {email} and password:{password} used*')

        my_account_page.enter_username(email)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            msg_text = WebDriverWait(self.driver, 10).until(presence_of_element_located(
                (By.XPATH, "//li[contains(text(),'Unknown email address. Check again or try your username')]")
            ))
            expected_error = "Unknown email address. Check again or try your username."
            assert msg_text.text == expected_error

            self.logger.debug(f'Invalid Login, User: {email} is invalid.')
            self.logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            self.logger.error(f'Login with invalid login credentials: {e}')
            self.logger.info('Test case has been executed successfully, test result: FAIL')
            raise

    # Login with invalid username
    def test_invalid_login_invalid_username(self):
        self.logger.info('--------------------invalid login---------------------')
        self.logger.info('test_invalid_login_invalid_username')

        # User login process
        my_account_page = my_account.Login(self.driver)
        self.logger.debug('My Account page object created')

        # Providing invalid username & password
        user_name = 'I_am_Invalid_User'
        password = 'I_am_Invalid_User'
        self.logger.debug(f'*Invalid username: {user_name} and password:{password} used*')

        my_account_page.enter_username(user_name)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            msg_text = WebDriverWait(self.driver, 10).until(presence_of_element_located(
                (By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/ul[1]/li[1]")
            ))
            expected_error = (f"Error: The username {user_name} is not registered on this site. If you are unsure of "
                              f"your username, try your email address instead.")
            assert msg_text.text == expected_error

            self.logger.debug(f'Invalid Login, User: {user_name} is invalid.')
            self.logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            self.logger.error(f'Login with invalid login credentials: {e}')
            self.logger.info('Test case has been executed successfully, test result: FAIL')
            raise

    # Login with empty username
    def test_invalid_login_empty_username(self):
        self.logger.info('--------------------invalid login---------------------')
        self.logger.info('test_invalid_login_empty_username')

        # User login process
        my_account_page = my_account.Login(self.driver)
        self.logger.debug('My Account page object created')

        # Providing empty username & password
        user_name = ''
        password = ''
        self.logger.debug(f'*Empty username and password used*')

        my_account_page.enter_username(user_name)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            msg_text = WebDriverWait(self.driver, 10).until(presence_of_element_located(
                (By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/ul[1]/li[1]")
            ))
            expected_error = "Error: Username is required."
            assert msg_text.text == expected_error

            self.logger.debug('Invalid Login, Username is empty.')
            self.logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            self.logger.error(f'Login with empty username: {e}')
            self.logger.info('Test case has been executed successfully, test result: FAIL')
            raise

    # Login with empty password
    def test_invalid_login_empty_password(self):
        self.logger.info('--------------------invalid login---------------------')
        self.logger.info('test_invalid_login_empty_password')

        # User login process
        my_account_page = my_account.Login(self.driver)
        self.logger.debug('My Account page object created')

        # Providing empty password with valid username
        user_name = read_properties.ReadConfig.get_username()
        password = ''
        self.logger.debug(f'*Valid username: {user_name} and blank password used*')

        my_account_page.enter_username(user_name)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            msg_text = WebDriverWait(self.driver, 10).until(presence_of_element_located(
                (By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/ul[1]/li[1]")
            ))
            expected_error = "Error: The password field is empty."
            assert msg_text.text == expected_error

            self.logger.debug('Invalid Login, password is blank.')
            self.logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            self.logger.error(f'Login with empty password: {e}')
            self.logger.info('Test case has been executed successfully, test result: FAIL')
            raise

    # Login with valid credentials
    def test_valid_user_login(self):
        self.logger.info('--------------------valid login---------------------')
        self.logger.info('Executing test case ID: test_valid_user_login')

        # User login process
        my_account_page = my_account.Login(self.driver)
        self.logger.debug('My Account page object created')

        user_name = read_properties.ReadConfig.get_username()
        password = read_properties.ReadConfig.get_password()
        self.logger.debug(f'*Read username: {user_name} and password from config.ini file*')

        my_account_page.enter_username(user_name)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            recent_orders_link = WebDriverWait(self.driver, 10).until(
                presence_of_element_located((By.XPATH, "//a[contains(text(),'recent orders')]"))
            )
            assert recent_orders_link.text == "recent orders"

            self.logger.debug(f'User: {user_name} has been logged in successfully')
            self.logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            self.logger.error(f'Login validation failed: {e}')
            self.logger.info('Test case has been executed successfully, test result: FAIL')
            raise
