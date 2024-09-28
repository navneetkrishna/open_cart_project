import inspect
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from testCase import test_logout_001
from pages import ecommerce_home_page, ecommerce_my_account_page
from utilities import excel_util

# get the path of the file
file = os.getcwd() + '/testData' + '/login_cred.xlsx'


class TestUserLoginDDT:

    def screenshot_filename(self):
        # To get the current test method name
        # Stack > ParentMethod > ChildMethod

        stack = inspect.stack()
        # stack [0] = child, stack[1] = parent
        screenshot_filename = stack[1].function

        return screenshot_filename

    # data driven test user login
    @pytest.mark.data_driven
    def test_ddt_user_login(self, driver, logger):
        logger.info('--------------------data driven valid login---------------------')
        logger.info('Executing test case ID: test_ddt_user_login')

        # get the number of rows and column of testdata
        rows = excel_util.get_row_count(file)
        # col = excel_util.get_column_count(file)

        logger.info(f'Number of rows in login_cred file: {rows}')

        home_page = ecommerce_home_page.HomePage(driver)
        logger.debug('Home page object created')

        home_page.click_my_account()

        # User login process
        my_account_login_page = ecommerce_my_account_page.Login(driver)
        logger.debug('My Account login page object created')

        for r in range(2, rows + 1):
            email = excel_util.read_data(file, r, 1)
            pwd = excel_util.read_data(file, r, 2)
            exp_res = excel_util.read_data(file, r, 3)

            logger.debug(f'Logging in with user:{email} and pass: {pwd}  ')

            my_account_login_page.enter_username(email)
            my_account_login_page.enter_password(pwd)
            my_account_login_page.click_login()

            # positive case, valid login
            if exp_res == "pass":

                try:
                    recent_orders_link = WebDriverWait(driver, 10).until(
                        presence_of_element_located((By.XPATH, "//a[contains(text(),'recent orders')]"))
                    )
                    assert recent_orders_link.text == "recent orders"

                    logger.debug(f'User: {email} has been logged in successfully')
                    logger.info('Test case has been executed successfully, test result: PASS')

                except Exception as e:

                    # Save the screenshot
                    driver.save_screenshot(
                        os.path.abspath(os.curdir) + "\\screenshots\\" + f"{self.screenshot_filename()}.png")

                    logger.error(f'Login validation failed: {e}')
                    logger.info('Test case has been executed, test result: FAIL')
                    raise

                # after successful login, logout to perform next login attempt
                log_out = test_logout_001.TestLogOut()
                log_out.test_logout(driver, logger)

                logger.debug(f"Logging out to perform next login attempt")
                logger.debug(f"calling logout method of TestLogOut class")

            elif exp_res == "fail":

                try:
                    msg_text = WebDriverWait(driver, 10).until(presence_of_element_located(
                        (By.XPATH, "//li[contains(text(),'Unknown email address. Check again or try your username')]")
                    ))
                    expected_error = "Unknown email address. Check again or try your username."
                    assert msg_text.text == expected_error

                    logger.debug(f'Invalid Login, User: {email} is invalid.')
                    logger.info('Test case has been executed successfully, test result: PASS')

                except Exception as e:

                    # Save the screenshot
                    driver.save_screenshot(
                        os.path.abspath(os.curdir) + "\\screenshots\\" + f"{self.screenshot_filename()}.png")

                    logger.error(f'Login with invalid login credentials: {e}')
                    logger.info('Test case has been executed, test result: FAIL')
                    raise
