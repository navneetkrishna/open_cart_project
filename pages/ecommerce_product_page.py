from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    product_title_xpath = "//h1[contains(text(),'Logo Collection')]"
    add_cart_btn_xpath = "//button[contains(text(),'Add to cart')]"

    # locators of special products which requires addition data (color, size, quantity)
    #
    # item 1 > Logo Collection item has 2/3 additional items (requires quantity before adding to cart)
    # 1. Hoodie with Logo
    # 2. T-shirt
    # 3. Beanie (only for admin account)

    hoodie_with_logo_qnty_txtbox_xpath = "(//input[@class='input-text qty text'])[1]"
    tshirt_qnty_txtbox_xpath = "(//input[@class='input-text qty text'])[2]"
    beanie_qnty_txtbox_xpath = "(//input[@class='input-text qty text'])[3]"

    # item 2 > V-Neck T-Shirt > requires color and size selection before adding to cart
    tshirt_color_dropdown_xpath = "//select[@id='pa_color']"
    tshirt_size_dropdown_xpath = "//select[@id='pa_size']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_cart_btn_xpath))).click()

        except TimeoutException as e:
            print(f"add to cart button is not clickable or may notbe available.{e}")

    def set_hoodie_quantity(self, quantity):
        qnty_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.hoodie_with_logo_qnty_txtbox_xpath)))
        qnty_box.clear()
        qnty_box.send_keys(str(quantity))

    def set_tshirt_quantity(self, quantity):
        qnty_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tshirt_qnty_txtbox_xpath)))
        qnty_box.clear()
        qnty_box.send_keys(str(quantity))

    def select_tshirt_color(self, index):
        try:
            dropdown = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tshirt_color_dropdown_xpath)))
            Select(dropdown).select_by_index(index)

        except TimeoutException as e:
            print(f"Tshirt color dropdown not available or options are not selectable. {e}")


    def select_tshirt_size(self, index):
        try:
            dropdown = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tshirt_size_dropdown_xpath)))
            Select(dropdown).select_by_index(index)

        except TimeoutException as e:
            print(f"Tshirt size dropdown not available or options are not selectable. {e}")
