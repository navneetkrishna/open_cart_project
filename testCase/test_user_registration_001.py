import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from testCase.conftest import driver
from utilities import read_properties, random_email_generator
from pages import ecommerce_my_account_page, ecommerce_home_page


class TestNewUserRegistration:
    @pytest.mark.smoke
    def test_invalid_register_user(self, driver, logger):

        logger.info(f'---------------------invalid registration--------------')
        logger.info(f'Executing test_invalid_register_user')

        # Navigate to home page > my account
        home_page = ecommerce_home_page.HomePage(driver)
        # logger.debug('Homepage object created')

        home_page.click_my_account()

        # User registration process
        my_account_page = ecommerce_my_account_page.Registration(driver)
        logger.debug('My Account page object created')

        # Generate random email address
        email = random_email_generator.generate_email()
        logger.debug(f'Registering user with email: {email}')

        my_account_page.enter_email(email)
        # my_account_page.enter_password()
        my_account_page.click_register()

        # logger.debug(f'Email {email} has been registered')

        # Validating if the user has been registered successfully
        try:
            error_txt = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/ul[1]/li[1]"))
            )

            expected_error = 'Error: Please enter an account password.'

            assert error_txt.text == expected_error
            logger.debug(f'Invalid user registration, no password found for {email}')
            logger.info(f'test case ID:{__name__} has been executed successfully, test result: PASS')

        except Exception as e:
            logger.error(f'Invalid user registration, user {email} registered without password, {e}')
            logger.info(f'test case ID:{__name__} has been executed successfully, test result: FAIL')

            raise

    # valid registration operation
    @pytest.mark.smoke
    def test_valid_register_user(self, driver, logger):

        logger.info(f'---------------------valid registration--------------')
        logger.info(f'Executing test_valid_register_user')

        # Navigate to home page > my account
        home_page = ecommerce_home_page.HomePage(driver)
        # logger.debug('Homepage object created')

        home_page.click_my_account()

        # User registration process
        my_account_page = ecommerce_my_account_page.Registration(driver)
        logger.debug('My Account page object created')

        # Generate random email address
        email = random_email_generator.generate_email()
        logger.debug(f'Registering user with email: {email}')

        my_account_page.enter_email(email)
        my_account_page.enter_password()
        my_account_page.click_register()

        logger.debug(f'Email {email} has been registered')

        # Validating if the user has been registered successfully
        try:
            recent_orders_link = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.XPATH, "//a[contains(text(),'recent orders')]"))
            )
            assert recent_orders_link.text == "recent orders"
            logger.debug('User registration validated successfully')
            logger.info(f'test case ID:{__name__} has been executed successfully, test result: PASS')

        except Exception as e:
            logger.error(f'Registration validation failed: {e}')
            logger.info(f'test case ID:{__name__} has been executed successfully, test result: FAIL')

            raise
