from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.read_properties import ReadConfig


class CheckoutPage:

    # locators
    displayCoupon_btn_xpath = "//div/button[contains(text(), 'Add a coupon')]"
    coupon_txtbox_xpath = "//input[@id='wc-block-components-totals-coupon__input-0']"
    apply_coupon_btn_xpath = "//span[contains(text(),'Apply')]"
    cod_btn_xpath = "//span[contains(text(),'Cash on delivery')]"
    place_order_btn_xpath = "//div/button/span[contains(text(), 'Place Order')]"
    coupon_applied_xpath = "//div[contains(text(),'Coupon code applied successfully.')]"
    empty_cart_text_xpath = "//h2[contains(text(),'Your cart is currently empty!')]"

    login_status_xpath = "//a[contains(text(),'Log in')]"

    #     constructor

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # actions

    def ckick_display_coupon_btn(self):

        # self.driver.find_element(By.XPATH, self.displayCoupon_btn_xpath).click()
        coupon_display = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.displayCoupon_btn_xpath)))
        coupon_display.click()

    def apply_coupon(self):

        coupon = ReadConfig.get_coupon()

        try:
            # Type coupon 'FREE'
            coupon_textbox = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.coupon_txtbox_xpath)))
            coupon_textbox.send_keys(coupon)

            # Click apply button only if coupon is entered
            if coupon_textbox.get_attribute("value") != "":
                self.wait.until(EC.element_to_be_clickable((By.XPATH, self.apply_coupon_btn_xpath))).click()

        except TimeoutException as e:
            print(f"Coupon {coupon} did not work{e}")

        return coupon

    def place_order(self):

        # Ensure that coupon is applied
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, self.coupon_applied_xpath)))
        # click 'Place Order' button

        # in case of no coupon before placing the order, select COD option
        # self.driver.find_element(By.XPATH, self.cod_btn_xpath).click()

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.place_order_btn_xpath))).click()

        except TimeoutException as e:
            print(f"Place order button is not clickable {e}")

    def is_cart_empty(self):

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.empty_cart_text_xpath)))

            return True

        except TimeoutException as e:

            print(f"cart is not empty or the empty_cart_text_xpath elements is not present on the page. {e}")

            return False

    def is_user_logged_in(self):

        # if login button (link element) is available on the page, that means user is not logged in.
        # and return False

        try:

            self.wait.until(EC.presence_of_element_located((By.XPATH, self.login_status_xpath)))

            return False

        except TimeoutException as e:

            print(f"Element not found, user already logged in. {e}")

            return True
