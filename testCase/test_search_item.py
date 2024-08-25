import pytest
from selenium.webdriver.common.by import By
from pages import ecommerce_homepage
from utilities import read_properties
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class TestSearchItem:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        # parameter driver is a fixture from conftest module

        self.driver = driver
        url = read_properties.ReadConfig.get_application_URL()
        self.driver.get(url)
        self.driver.maximize_window()
        # self.logger.info(f'Loading URL: {url} and launching browser')

    @pytest.mark.smoke
    def test_invalid_search_item(self, driver, logger):

        logger.info('--------------------search an invalid item---------------------')
        logger.info('test_invalid_search_item')

        self.driver = driver

        homepage = ecommerce_homepage.HomePage(self.driver)
        homepage.click_shop()

        item = 'invalid_item'
        homepage.search_product(item)

        try:
            error_msg = WebDriverWait(self.driver, 10).until(presence_of_element_located((By.XPATH, "//div[contains(text(),'No products were found matching your selection.')]")))

            expected_error = 'No products were found matching your selection.'
            assert error_msg.text == expected_error

            logger.debug(f"Searched item name{item} is not available")

            logger.info(f"{__name__} successfully executed, test result: Pass")

        except Exception as e:

            logger.error(f"'Invalid item searched", e)
            logger.info(f"{__name__}TC executed, test result: FAIL")
            raise

    @pytest.mark.smoke
    def test_valid_search_item(self, driver, logger):

        logger.info('--------------------search a valid item---------------------')
        logger.info('test_valid_search_item')

        self.driver = driver

        homepage = ecommerce_homepage.HomePage(self.driver)
        homepage.click_shop()

        item = read_properties.ReadConfig.get_random_item_name()
        homepage.search_product(item)

        try:
            cart_btn = WebDriverWait(self.driver, 10).until(presence_of_element_located((By.XPATH, "//button["
                                                                                                   "contains(text(),"
                                                                                                   "'Add to cart')]")))
            assert cart_btn.text == "Add to cart"
            logger.debug(f"item name{item} is searched")

            logger.info(f"{__name__} successfully executed, test result: Pass")

        except Exception as e:

            logger.error(f"'test_add_item_to_cart' > Product not available", e)
            logger.info(f"{__name__} TC executed, test result: FAIL")
            raise

