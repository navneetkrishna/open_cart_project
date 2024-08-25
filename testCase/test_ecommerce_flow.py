import pytest
import pdb
from pages import ecommerce_homepage
from testCase import test_search_item, test_user_login_001, test_logout_001
from utilities import read_properties


class TestEcommerceFlow:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):

        self.driver = driver
        url = read_properties.ReadConfig.get_application_URL()
        self.driver.get(url)
        self.driver.maximize_window()

        # Navigate to home page > my account
        home_page = ecommerce_homepage.HomePage(self.driver)
        # self.logger.debug('Homepage object created')

        home_page.click_my_account()

    @pytest.mark.flow
    def test_flow(self, driver, logger):

        login = test_user_login_001.TestUserLogin()
        item = test_search_item.TestSearchItem()
        logout = test_logout_001.TestLogOut()

        login.test_valid_user_login(self.driver, logger)
        item.test_valid_search_item(self.driver, logger)
        logout.test_logout(self.driver, logger)
