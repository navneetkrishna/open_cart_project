import pdb

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages import ecommerce_checkout_page, ecommerce_home_page
from testCase import test_user_login_001, test_add_item_to_cart, test_search_item


class TestCheckout:

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

        logger.info("cart not empty")
        checkout_page.ckick_display_coupon_btn()
        checkout_page.apply_coupon()
        logger.info("coupon applied")

        if checkout_page.is_user_logged_in() is False:
            login.test_valid_user_login(driver, logger)

            # redirect to check out page
            homepage.click_checkout()

        try:
            checkout_page.place_order()
            logger.info("order placed clicked")

            expected_msg = "Order received"

            order_success = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Order received')]")))
            logger.info(order_success, order_success.text)
            assert order_success.text == expected_msg
            logger.info("order placed")

        except TimeoutException as e:
            logger.error(f"Order not placed, issue in checkout{e}")
