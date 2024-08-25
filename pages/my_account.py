from utilities import random_email_generator
from selenium.webdriver.common.by import By


# This method will register a user
# a random email address will be used
# Visit utilities.random_email_generator
# default password for all new users: Demo1234@

class Registration:
    # locators

    email_txtbox_xpath = '//input[@id="reg_email"]'
    password_txtbox_xpath = '//input[@id="reg_password"]'
    register_button_xpath = '//button[contains(text(),"Register")]'

    def __init__(self, driver):
        self.driver = driver

    # define actions

    def enter_email(self, email):
        # email = random_email_generator.generate_email()
        email_txtbox = self.driver.find_element(By.XPATH, self.email_txtbox_xpath)
        email_txtbox.send_keys(email)

    # password for new email is :Demo1234@
    def enter_password(self, password=None):
        # Set password to default if not provided
        if password is None:
            password = 'Demo1234@'

        # Find the password textbox and enter the password
        password_txtbox = self.driver.find_element(By.XPATH, self.password_txtbox_xpath)
        password_txtbox.send_keys(password)
    def click_register(self):
        self.driver.find_element(By.XPATH, self.register_button_xpath).click()


class Login:
    # locators

    username_txtbox_xpath = '//input[@id="username"]'
    password_txtbox_xpath = '//input[@id="password"]'
    login_button_xpath = '//button[contains(text(),"Log in")]'

    def __init__(self, driver):
        self.driver = driver

    # actions

    def enter_username(self, username):

        username_txtbox = self.driver.find_element(By.XPATH, self.username_txtbox_xpath)
        username_txtbox.send_keys(username)

    # password for new email is :Demo1234@
    def enter_password(self, password='Demo1234@'):

        password_txtbox = self.driver.find_element(By.XPATH, self.password_txtbox_xpath)
        password_txtbox.send_keys(password)

    def click_login(self):
        login_btn = self.driver.find_element(By.XPATH, self.login_button_xpath).click()