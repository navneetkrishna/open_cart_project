from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest, os, inspect
from pages import ecommerce_checkout_page, ecommerce_home_page
from testCase import test_user_login_001, test_add_item_to_cart, test_search_item


class TestCheckout:

    def screenshot_filename(self):
        # To get the current test method name
        # Stack > ParentMethod > ChildMethod

        stack = inspect.stack()
        # stack [0] = child, stack[1] = parent
        screenshot_filename = stack[1].function

        return screenshot_filename

    @pytest.mark.smoke
    def test_checkout(self, driver, logger):

        logger.info(f"execution -------------{__name__}------------")

        homepage = ecommerce_home_page.HomePage(driver)
        checkout_page = ecommerce_checkout_page.CheckoutPage(driver)
        login = test_user_login_001.TestUserLogin()

        logger.info(f"navigate to checkout page")
        homepage.click_checkout()

        # if cart is empty then add an item to cart
        if checkout_page.is_cart_empty() is True:

            logger.info(f"cart is empty")

            search_item_obj = test_search_item.TestSearchItem()
            searched_item = search_item_obj.test_valid_search_item(driver, logger)
            logger.info(f"searched item: {searched_item}")

            add_cart_obj = test_add_item_to_cart.TestAddItemToCart()
            item_added_to_cart = add_cart_obj.test_add_item_to_cart(driver, logger, searched_item)
            logger.info(f"item added to cart:{item_added_to_cart}")

            # once item is added to cart, move to checkout page
            homepage.click_checkout()

        # in case cart is not empty proceed to checkout
        logger.info("cart not empty")

        # before checkout, ensure that user is logged in
        if checkout_page.is_user_logged_in() is False:

            # User is not logged in, calling the login method
            logger.info("User is not logged in, calling the login method")
            login.test_valid_user_login(driver, logger)

            # redirect to check out page
            homepage.click_checkout()

        checkout_page.click_display_coupon_btn()
        checkout_page.apply_coupon()
        logger.info("coupon applied")

        try:

            checkout_page.place_order()
            logger.info("order placed clicked")

            expected_msg = "Order received"

            order_success = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Order received')]")))
            logger.info(f"-----order success type: {type(order_success)}")
            logger.info(f"-----order success test: {order_success.text}")
            assert order_success.text == expected_msg
            logger.info("order placed")

        except TimeoutException as e:

            # Save the screenshot
            driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + f"{self.screenshot_filename()}.png")

            logger.error(f"Order not placed, issue in checkout{e}")
