# import pytest
# import pdb
# from pages import ecommerce_home_page
# from testCase import test_search_item, test_user_login_001, test_logout_001, test_add_item_to_cart
# from utilities import read_properties
#
#
# class TestEcommerceFlow:
#
#     @pytest.mark.main
#     def test_flow(self, logger, driver):
#
#         login_obj = test_user_login_001.TestUserLogin()
#         search_item_obj = test_search_item.TestSearchItem()
#         add_cart_obj = test_add_item_to_cart.TestAddItemToCart()
#         logout_obj = test_logout_001.TestLogOut()
#
#         login_obj.test_valid_user_login(driver, logger)
#
#         searched_item = search_item_obj.test_valid_search_item(driver, logger)
#         logger.info(f"item: {searched_item}")
#
#         add_cart_obj.test_add_item_to_cart(driver, logger, searched_item)
#
#         logout_obj.test_logout(driver, logger)
