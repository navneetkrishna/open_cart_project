from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:
    # locators

    cart_btn_link_text = 'Cart'
    checkout_btn_link_text = 'Checkout'
    my_account_btn_link_text = 'My account'
    sample_page_btn_link_text = 'Sample Page'
    shop_btn_link_text = 'Shop'
    search_box_xpath = "//input[@id='woocommerce-product-search-field-0']"

    # constructor

    def __init__(self, driver):
        self.driver = driver

    # define actions

    def click_cart(self):
        self.driver.find_element(By.LINK_TEXT, self.cart_btn_link_text).click()

    def click_checkout(self):
        self.driver.find_element(By.LINK_TEXT, self.checkout_btn_link_text).click()

    def click_my_account(self):
        self.driver.find_element(By.LINK_TEXT, self.my_account_btn_link_text).click()

    def click_sample_page(self):
        self.driver.find_element(By.LINK_TEXT, self.sample_page_btn_link_text).click()

    def click_shop(self):
        self.driver.find_element(By.LINK_TEXT, self.shop_btn_link_text).click()

    def search_product(self, search_keyword):
        search_box = self.driver.find_element(By.XPATH, self.search_box_xpath)
        search_box.send_keys(search_keyword)
        search_box.send_keys(Keys.ENTER)

