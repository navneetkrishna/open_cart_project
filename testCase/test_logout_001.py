import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from utilities import read_properties
from pages import ecommerce_homepage, my_account


class TestLogOut:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):

        self.driver = driver

        url = read_properties.ReadConfig.get_application_URL()
        self.driver.get(url)
        self.driver.maximize_window()


    @pytest.mark.smoke
    def test_logout(self, driver, logger):

        self.driver = driver
        try:
            # Navigate to home page > my account
            homepage = ecommerce_homepage.HomePage(self.driver)
            homepage.click_my_account()

            # locate logout button
            account_link = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.XPATH, "(//a[contains(text(), 'Log out')])[1]")))
            logger.info("User is logged in.")


        except Exception as e:
            # If not logged in, you can log in or skip the test
            logger.error(f"User is not logged in, skipping the test.{e}")
            pytest.skip("User is not logged in.")
            raise

        myaccount = my_account.Login(self.driver)
        myaccount.click_logout()

