import pytest
import pdb
from pages import ecommerce_home_page
from testCase import test_search_item, test_user_login_001, test_logout_001
from utilities import read_properties


class TestEcommerceFlow:

    @pytest.mark.flow
    def test_flow(self, logger, driver):

        login = test_user_login_001.TestUserLogin()
        # item = test_search_item.TestSearchItem()
        logout = test_logout_001.TestLogOut()

        login.test_valid_user_login(driver, logger)
        # item = item.test_valid_search_item(driver, logger)
        # logger.info(f"item: {item}")
        logout.test_logout(driver, logger)
