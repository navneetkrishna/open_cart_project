from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from testCase.conftest import driver
from utilities import read_properties, random_email_generator
from utilities.cutom_logger import LogGen
from pages import my_account, ecommerce_homepage


class TestNewUserRegistration:

    # for logging
    logger = LogGen.loggen()

    def test_register_user(self, driver):

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
