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
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_cart_btn_xpath))).click()

    def set_hoodie_quantity(self, quantity):
        qnty_box = self.wait.until(EC.presence_of_element_located((By.XPATH, self.hoodie_with_logo_qnty_txtbox_xpath)))
        qnty_box.clear()
        qnty_box.send_keys(str(quantity))

    def set_tshirt_quantity(self, quantity):
        qnty_box = self.wait.until(EC.presence_of_element_located((By.XPATH, self.tshirt_qnty_txtbox_xpath)))
        qnty_box.clear()
        qnty_box.send_keys(str(quantity))

    def select_tshirt_color(self, index):
        dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, self.tshirt_color_dropdown_xpath)))
        Select(dropdown).select_by_index(index)

    def select_tshirt_size(self, index):
        dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, self.tshirt_size_dropdown_xpath)))
        Select(dropdown).select_by_index(index)






# from selenium.webdriver.common.by import By
#
#
# class ProductPage:
#     product_title_xpath = "//h1[contains(text(),'Logo Collection')]"
#     add_cart_btn_xpath = "//button[contains(text(),'Add to cart')]"
#
#     # locators of special products which requires addition data (color, size, quantity)
#
#     # item 1 > Logo Collection item has 2/3 additional items (requires quantity before adding to cart)
#     # 1. Hoodie with Logo
#     # 2. T-shirt
#     # 3. Beanie (only for admin account)
#     hoodie_with_logo_qnty_txtbox_xpath = "(//input[@class='input-text qty text'])[1]"
#     tshirt_qnty_txtbox_xpath = "(//input[@class='input-text qty text'])[2]"
#
#     beanie_qnty_txtbox_xpath = "(//input[@class='input-text qty text'])[3]"
#
#     # item 2 > V-Neck T-Shirt > requires color and size selection before adding to cart
#
#     tshirt_color_dropdown_xpath = "//select[@id='pa_color']"
#     tshirt_size_dropdown_xpath = "//select[@id='pa_size']"
#
#     # constructor
#     def __init__(self, driver):
#         self.driver = driver
#
#     # define actions
#
#     def add_to_cart(self):
#         self.driver.find_element(By.XPATH, self.add_cart_btn_xpath).click()
#
#     def match_product(self, item):
#         title = self.driver.find_element(By.XPATH, self.product_title_xpath)
#
#         return title == item.text()
#
#     def select_hoodie_qnty(self, qnty):
#         h_qnty_box = self.driver.find_element(By.XPATH, self.hoodie_with_logo_qnty_txtbox_xpath)
#         h_qnty_box.clear()
#         h_qnty_box.sendKeys(qnty)
#
#     def select_tshirt_qnty(self, qnty):
#         t_qnty_box = self.driver.find_element(By.XPATH, self.tshirt_qnty_txtbox_xpath)
#         t_qnty_box.clear()
#         t_qnty_box.sendKeys(qnty)
