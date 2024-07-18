import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import read_properties, random_email_generator
from pages import my_account, ecommerce_homepage

# URL = 'http://localhost/ecommerce_project'


driver = webdriver.Edge()
driver.get(read_properties.ReadConfig.get_application_URL())
driver.maximize_window()

#  navigate to home page > my account
ecm_obj1 = ecommerce_homepage.HomePage(driver)
ecm_obj1.click_my_account()

# # user registration process

# Create my account registration page object
# my_account_obj = my_account.Registration(driver)

# generate random email address
# email = random_email_generator.generate_email()

# my_account_obj.enter_email(email)
# print(email)
# my_account_obj.enter_password()
# my_account_obj.click_register()


# # user login process

# Create my account > login page object
my_account_login_obj = my_account.Login(driver)

username = 'sl6xm-@hotmail.com'
my_account_login_obj.enter_username(username)
my_account_login_obj.enter_password()
my_account_login_obj.click_login()

time.sleep(3)

driver.close()
