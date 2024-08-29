import pytest
import pdb
from pages import ecommerce_home_page
from testCase import test_search_item, test_user_login_001, test_logout_001, test_add_item_to_cart, test_checkout
from utilities import read_properties


class TestEcommerceFlow:

    @pytest.mark.eflow
    def test_flow(self, logger, driver):

        login_obj = test_user_login_001.TestUserLogin()
        search_item_obj = test_search_item.TestSearchItem()
        add_cart_obj = test_add_item_to_cart.TestAddItemToCart()
        checkout = test_checkout.TestCheckout()
        logout_obj = test_logout_001.TestLogOut()


        # login_obj.test_valid_user_login(driver, logger)

        # searched_item = search_item_obj.test_valid_search_item(driver, logger)
        # logger.info(f"searched item: {searched_item}")

        # item_added_to_cart = add_cart_obj.test_add_item_to_cart(driver, logger, searched_item)
        # logger.info(f"item added to cart:{item_added_to_cart}")

        checkout.test_checkout(driver, logger)
        logger.info(f"checkout successful")
        # logout_obj.test_logout(driver, logger)

    # login = test_user_login_001.TestUserLogin()
    #
    # if checkout_page.is_user_logged_in() is False:
    #     login.test_valid_user_login(driver, logger)
    #
    #     # redirect to check out page
    #     homepage.click_checkout()

