from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ShopPage:

    # locators
    search_box_xpath = "//input[@id='woocommerce-product-search-field-0']"

    # constructor

    def __init__(self, driver):
        self.driver = driver

    # define actions

    def search_product(self, search_keyword):
        search_box = self.driver.find_element(By.XPATH, self.search_box_xpath)
        search_box.send_keys(search_keyword)
        search_box.send_keys(Keys.ENTER)
