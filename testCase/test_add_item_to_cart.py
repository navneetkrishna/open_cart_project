import pytest
from selenium.webdriver.common.by import By

from pages import ecommerce_homepage
from utilities import read_properties
from utilities.custom_logger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class TestAddItem:
    # For logging
    logger = LogGen.loggen()

    # Fixture > scope = function > executed before each function
    # Fixture > autouse = True > executed before each function automatically (without needing to explicitly pass it as an argument.)
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        # parameter driver is a fixture from conftest module

        self.driver = driver
        url = read_properties.ReadConfig.get_application_URL()
        self.driver.get(url)
        self.driver.maximize_window()
        self.logger.info(f'Loading URL: {url} and launching browser')

    @pytest.mark.new
    def test_add_item_to_cart(self):

        self.logger.info('--------------------adding item to cart---------------------')
        self.logger.info('add_item_to_cart')

        homepage = ecommerce_homepage.HomePage(self.driver)
        homepage.click_shop()

        item = read_properties.ReadConfig.get_random_item_name()
        # homepage.search_product(item)
        homepage.search_product('V-Neck T-Shirt')

        try:
            cart_btn = WebDriverWait(self.driver, 10).until(presence_of_element_located((By.XPATH, "//button["                                                                               "contains(text(),"
                                                                                                   "'Add to cart')]")))
            assert cart_btn.text == "Add to cart"

            self.logger.info(f"{__name__} successfully executed, test result: Pass")

        except Exception as e:

            self.logger.error(f"'test_add_item_to_cart' > Product not available", e)
            self.logger.info(f"{__name__} successfully executed, test result: FAIL")
            raise

