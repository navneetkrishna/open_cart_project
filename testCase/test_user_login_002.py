import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from testCase.conftest import driver
from utilities import read_properties, random_email_generator
from utilities.cutom_logger import LogGen
from pages import my_account, ecommerce_homepage


class TestUserLogin:

    # for logging
    logger = LogGen.loggen()

    def test_user_login(self, driver):

        self.logger.info(f'Executing test case ID:{__name__}')

        self.driver = driver

        # Reading URL from config.ini file and launching browser
        url = read_properties.ReadConfig.get_application_URL()
        self.logger.info(f'Loading URL: {url}')
        self.logger.info('Launching browser')

        self.driver.get(url)
        self.driver.maximize_window()

        # Navigate to home page > my account
        home_page = ecommerce_homepage.HomePage(self.driver)
        home_page.click_my_account()
        self.logger.debug('Homepage object created')

        # user login process
        my_account_page = my_account.Login(self.driver)
        self.logger.debug('My Account page object created')

        user_name = read_properties.ReadConfig.get_username()
        password = read_properties.ReadConfig.get_password()

        self.logger.debug(f'*Read username: {user_name} and password:{password} from config.ini file*')

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
            self.logger.info(f'test case ID:{__name__} has been executed successfully, test result: PASS')

        except Exception as e:
            self.logger.error(f'Registration validation failed: {e}')
            self.logger.info(f'test case ID:{__name__} has been executed successfully, test result: FAIL')

            raise
