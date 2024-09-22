import pytest, os, inspect
from selenium.webdriver.common.by import By
from pages import ecommerce_home_page
from utilities import read_properties
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class TestSearchItem:

    def screenshot_filename(self):
        # To get the current test method name
        # Stack > ParentMethod > ChildMethod

        stack = inspect.stack()
        # stack [0] = child, stack[1] = parent
        screenshot_filename = stack[1].function

        return screenshot_filename

    @pytest.mark.smoke
    def test_invalid_search_item(self, driver, logger):

        logger.info('--------------------search an invalid item---------------------')
        logger.info('test_invalid_search_item')

        homepage = ecommerce_home_page.HomePage(driver)
        homepage.click_shop()

        item = 'invalid_item'
        homepage.search_product(item)

        try:
            error_msg = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//div[contains(text("
                                                                                               "),'No products were "
                                                                                               "found matching your "
                                                                                               "selection.')]")))

            expected_error = 'No products were found matching your selection.'
            assert error_msg.text == expected_error

            logger.debug(f"Searched item name{item} is not available")

            logger.info(f"{__name__} successfully executed, test result: Pass")

        except Exception as e:

            # Save the screenshot
            driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + f"{self.screenshot_filename()}.png")

            logger.error(f"'Invalid item searched", e)
            logger.info(f"{__name__}TC executed, test result: FAIL")
            raise

        return item

    @pytest.mark.smoke
    def test_valid_search_item(self, driver, logger):

        logger.info('--------------------search a valid item---------------------')
        logger.info('test_valid_search_item')

        homepage = ecommerce_home_page.HomePage(driver)
        homepage.click_shop()

        item = read_properties.ReadConfig.get_random_item_name()
        homepage.search_product(item)

        try:
            cart_btn = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, "//button["
                                                                                                   "contains(text(),"
                                                                                                   "'Add to cart')]")))
            assert cart_btn.text == "Add to cart"
            logger.debug(f"item name{item} is searched")

            logger.info(f"{__name__} successfully executed, test result: Pass")

        except Exception as e:

            # Save the screenshot
            driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + f"{self.screenshot_filename()}.png")

            logger.error(f"'test_add_item_to_cart' > Product not available", e)
            logger.info(f"{__name__} TC executed, test result: FAIL")
            raise

        return item
