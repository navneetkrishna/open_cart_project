import os
import pytest
from pages import ecommerce_product_page
import inspect


class TestAddItemToCart:

    def screenshot_filename(self):
        # To get the current test method name
        # Stack > ParentMethod > ChildMethod

        stack = inspect.stack()
        # stack [0] = child, stack[1] = parent
        screenshot_filename = stack[1].function

        return screenshot_filename

    @pytest.mark.smoke
    def test_add_item_to_cart(self, driver, logger, item):

        # a list argument 'item' will be passed to the function

        logger.debug(f"data type of item argument: {type(item)}")

        logger.info(f"requested item to add to cart is: {item}")

        # since the list contains only one item, get the name using index
        logger.info(f"item text:{item[0]}")

        item = item[0] if isinstance(item, list) and len(item) > 0 else item

        logger.info(f"Requested item to add to cart: {item}")

        product_page = ecommerce_product_page.ProductPage(driver)

        try:
            if item == 'Logo Collection':
                product_page.set_hoodie_quantity(1)
                product_page.set_tshirt_quantity(1)

            elif item == 'V-Neck T-Shirt':
                product_page.select_tshirt_color(1)
                product_page.select_tshirt_size(2)

            product_page.add_to_cart()
            logger.info(f"Added item '{item}' to cart successfully.")
            logger.info(f"test script execution complete; result: PASS")

        except Exception as e:

            # Save the screenshot
            driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + f"{self.screenshot_filename()}.png")

            logger.error(f"could not add {item} to cart")
            logger.info(f"test script execution complete; result: FAIL")
            raise

        return item
