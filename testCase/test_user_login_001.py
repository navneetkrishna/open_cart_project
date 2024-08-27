import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from utilities import read_properties
from pages import ecommerce_my_account_page, ecommerce_home_page


class TestUserLogin:

    # Login with invalid email
    @pytest.mark.negative
    def test_invalid_login_invalid_email(self, driver, logger):
        logger.info('--------------------invalid login---------------------')
        logger.info('test_invalid_login_invalid_email')

        # Navigate to home page > my account
        home_page = ecommerce_home_page.HomePage(driver)
        # logger.debug('Homepage object created')

        home_page.click_my_account()

        # User login process
        my_account_page = ecommerce_my_account_page.Login(driver)
        logger.debug('My Account page object created')

        # Providing invalid username & password
        email = 'username@invalid.com'
        password = 'invalid@pass'
        logger.debug(f'*Invalid email: {email} and password:{password} used*')

        my_account_page.enter_username(email)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            msg_text = WebDriverWait(driver, 10).until(presence_of_element_located(
                (By.XPATH, "//li[contains(text(),'Unknown email address. Check again or try your username')]")
            ))
            expected_error = "Unknown email address. Check again or try your username."
            assert msg_text.text == expected_error

            logger.debug(f'Invalid Login, User: {email} is invalid.')
            logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            logger.error(f'Login with invalid login credentials: {e}')
            logger.info('Test case has been executed successfully, test result: FAIL')
            raise

    # Login with invalid username
    @pytest.mark.negative
    def test_invalid_login_invalid_username(self, driver, logger):
        logger.info('--------------------invalid login---------------------')
        logger.info('test_invalid_login_invalid_username')

        # Navigate to home page > my account
        home_page = ecommerce_home_page.HomePage(driver)
        # logger.debug('Homepage object created')

        home_page.click_my_account()

        # User login process
        my_account_page = ecommerce_my_account_page.Login(driver)
        logger.debug('My Account page object created')

        # Providing invalid username & password
        user_name = 'I_am_Invalid_User'
        password = 'I_am_Invalid_User'
        logger.debug(f'*Invalid username: {user_name} and password:{password} used*')

        my_account_page.enter_username(user_name)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            msg_text = WebDriverWait(driver, 10).until(presence_of_element_located(
                (By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/ul[1]/li[1]")
            ))
            expected_error = (f"Error: The username {user_name} is not registered on this site. If you are unsure of "
                              f"your username, try your email address instead.")
            assert msg_text.text == expected_error

            logger.debug(f'Invalid Login, User: {user_name} is invalid.')
            logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            logger.error(f'Login with invalid login credentials: {e}')
            logger.info('Test case has been executed successfully, test result: FAIL')
            raise

    # Login with empty username
    @pytest.mark.negative
    def test_invalid_login_empty_username(self, driver, logger):
        logger.info('--------------------invalid login---------------------')
        logger.info('test_invalid_login_empty_username')

        # Navigate to home page > my account
        home_page = ecommerce_home_page.HomePage(driver)
        # logger.debug('Homepage object created')

        home_page.click_my_account()

        # User login process
        my_account_page = ecommerce_my_account_page.Login(driver)
        logger.debug('My Account page object created')

        # Providing empty username & password
        user_name = ''
        password = ''
        logger.debug(f'*Empty username and password used*')

        my_account_page.enter_username(user_name)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            msg_text = WebDriverWait(driver, 10).until(presence_of_element_located(
                (By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/ul[1]/li[1]")
            ))
            expected_error = "Error: Username is required."
            assert msg_text.text == expected_error

            logger.debug('Invalid Login, Username is empty.')
            logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            logger.error(f'Login with empty username: {e}')
            logger.info('Test case has been executed successfully, test result: FAIL')
            raise

    # Login with empty password
    @pytest.mark.negative
    def test_invalid_login_empty_password(self, driver, logger):
        logger.info('--------------------invalid login---------------------')
        logger.info('test_invalid_login_empty_password')

        # Navigate to home page > my account
        home_page = ecommerce_home_page.HomePage(driver)
        # logger.debug('Homepage object created')

        home_page.click_my_account()

        # User login process
        my_account_page = ecommerce_my_account_page.Login(driver)
        logger.debug('My Account page object created')

        # Providing empty password with valid username
        user_name = read_properties.ReadConfig.get_username()
        password = ''
        logger.debug(f'*Valid username: {user_name} and blank password used*')

        my_account_page.enter_username(user_name)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            msg_text = WebDriverWait(driver, 10).until(presence_of_element_located(
                (By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/ul[1]/li[1]")
            ))
            expected_error = "Error: The password field is empty."
            assert msg_text.text == expected_error

            logger.debug('Invalid Login, password is blank.')
            logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            logger.error(f'Login with empty password: {e}')
            logger.info('Test case has been executed successfully, test result: FAIL')
            raise

    # Login with valid credentials
    @pytest.mark.smoke
    def test_valid_user_login(self, driver, logger):

        logger.info('--------------------valid login---------------------')
        logger.info('Executing test case ID: test_valid_user_login')

        # Navigate to home page > my account
        home_page = ecommerce_home_page.HomePage(driver)
        # logger.debug('Homepage object created')

        home_page.click_my_account()

        # User login process
        my_account_page = ecommerce_my_account_page.Login(driver)
        logger.debug('My Account page object created')

        user_name = read_properties.ReadConfig.get_username()
        password = read_properties.ReadConfig.get_password()
        logger.debug(f'*Read username: {user_name} and password from config.ini file*')

        my_account_page.enter_username(user_name)
        my_account_page.enter_password(password)
        my_account_page.click_login()

        # Validating if the user has been logged in successfully
        try:
            recent_orders_link = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.XPATH, "//a[contains(text(),'recent orders')]"))
            )
            assert recent_orders_link.text == "recent orders"

            logger.debug(f'User: {user_name} has been logged in successfully')
            logger.info('Test case has been executed successfully, test result: PASS')

        except Exception as e:
            logger.error(f'Login validation failed: {e}')
            logger.info('Test case has been executed successfully, test result: FAIL')
            raise
