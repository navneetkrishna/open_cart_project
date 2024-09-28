import pytest, os, inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from utilities import read_properties
from pages import ecommerce_home_page, ecommerce_my_account_page


class TestLogOut:

    def screenshot_filename(self):
        # To get the current test method name
        # Stack > ParentMethod > ChildMethod

        stack = inspect.stack()
        # stack [0] = child, stack[1] = parent
        screenshot_filename = stack[1].function

        return screenshot_filename

    @pytest.mark.smoke
    def test_logout(self, driver, logger):

        try:

            homepage = ecommerce_home_page.HomePage(driver)
            homepage.click_my_account()

            # locate logout button
            account_link = WebDriverWait(driver, 10).until(
                presence_of_element_located((By.XPATH, "(//a[contains(text(), 'Log out')])[1]")))
            logger.info("User is already logged in.")

        except Exception as e:

            # Save the screenshot
            driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + f"{self.screenshot_filename()}.png")

            # If not logged in, you can log in or skip the test
            logger.error(f"User is not logged in, skipping the test.{e}")
            pytest.skip("User is not logged in.")

            # since pytest.skip is already used, 'raise' keyword will become unreachable
            # raise

        my_account = ecommerce_my_account_page.Login(driver)
        my_account.click_logout()


