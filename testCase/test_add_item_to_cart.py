# import pytest
# from selenium.webdriver.common.by import By
# from pages import ecommerce_home_page
# from utilities import read_properties
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located
#
#
# class TestAddItemToCart:
#
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self, driver):
#         # parameter driver is a fixture from conftest module
#
#         self.driver = driver
#         url = read_properties.ReadConfig.get_application_URL()
#         self.driver.get(url)
#         self.driver.maximize_window()
#         # logger.info(f'Loading URL: {url} and launching browser')
#
#     @pytest.mark.demoo
#     def test_add_item_to_cart(self, item, logger):
#         if item.text() == 'Logo Collection'
#
