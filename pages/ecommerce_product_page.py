from selenium.webdriver.common.by import By


class ProductPage:
    product_title_xpath = "//h1[contains(text(),'Logo Collection')]"
    add_cart_btn_xpath = "//button[contains(text(),'Add to cart')]"

    # locators of special products which requires addition data (color, size, quantity)

    # item 1 > Logo Collection has 2 sub items (requires quantity before adding to cart)
    # 1. Hoodie with Logo
    # 2. T-shirt
    hoodie_with_logo_qnty_txtbox_xpath = "//input[@id='quantity_66cc817198dd0']"
    tshirt_qnty_txtbox_xpath = "//input[@id='quantity_66cc83a14801a']"

    # item 2 > V-Neck T-Shirt > requires color and size selection before adding to cart

    tshirt_color_dropdown_xpath = "//select[@id='pa_color']"
    tshirt_size_dropdown_xpath = "//select[@id='pa_size']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # define actions

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_cart_btn_xpath).click()

    def match_product(self, item):
        title = self.driver.find_element(By.XPATH, self.product_title_xpath)

        return title == item.text()

    def select_hoodie_qnty(self, qnty):
        h_qnty_box = self.driver.find_element(By.XPATH, self.hoodie_with_logo_qnty_txtbox_xpath)
        h_qnty_box.clear()
        h_qnty_box.sendKeys(qnty)

    def select_tshirt_qnty(self, qnty):
        t_qnty_box = self.driver.find_element(By.XPATH, self.tshirt_qnty_txtbox_xpath)
        t_qnty_box.clear()
        t_qnty_box.sendKeys(qnty)
