import inspect

from pages import ecommerce_home_page, ecommerce_my_account_page
from utilities import excel_util
import os
import pytest

# get the name of the file
file = os.getcwd() + '/testData' + '/login_cred.xlsx'


class TestUserLoginDDT:

    def screenshot_filename(self):
        # To get the current test method name
        # Stack > ParentMethod > ChildMethod

        stack = inspect.stack()
        # stack [0] = child, stack[1] = parent
        screenshot_filename = stack[1].function

        return screenshot_filename

    rows = excel_util.get_row_count(file)
    col = excel_util.get_column_count(file)

    @pytest.mark.ddt
    def test_valid_user_login(self, driver, logger):
        logger.info('--------------------valid login---------------------')
        logger.info('Executing test case ID: test_valid_user_login')

        home_page = ecommerce_home_page.HomePage(driver)
        home_page.click_my_account()

        # User login process
        my_account_login_page = ecommerce_my_account_page.Login(driver)
        logger.debug('My Account login page object created')

        for r in range(2, self.rows + 1):

            print("*************")

            for c in range(1, self.col + 1):
                # print(c)
                print(excel_util.read_data(file, r, c))



# from utilities import excel_util
# import os
#
# # get the name of the file
# file = os.getcwd() + '/testData' + '/login_cred.xlsx'
#
# # print(excel_util.get_sheet_name(file)) "Sheet1"
# # print(excel_util.get_row_count(file)) 4
# # print(excel_util.get_column_count(file)) 3
# # print(excel_util.read_data(file, 2, 1))
# # excel_util.write_data(file, 1, 4, "hi")
# # excel_util.fill_green_color(file, 1, 4)
# # excel_util.fill_red_color(file, 1, 5)
#
