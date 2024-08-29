import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from utilities import read_properties
from pages import ecommerce_home_page, ecommerce_my_account_page


class TestLogOut:

    @pytest.mark.smoke
    def test_logout(self, driver, logger):

        self.driver = driver
        try:

            homepage = ecommerce_home_page.HomePage(self.driver)
            homepage.click_my_account()

            # locate logout button
            account_link = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.XPATH, "(//a[contains(text(), 'Log out')])[1]")))
            logger.info("User is already logged in.")


        except Exception as e:

            # If not logged in, you can log in or skip the test
            logger.error(f"User is not logged in, skipping the test.{e}")
            pytest.skip("User is not logged in.")

            raise

        myaccount = ecommerce_my_account_page.Login(self.driver)
        logger.debug("Logging out...")
        myaccount.click_logout()
