import configparser
import os
import random

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + '\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def get_application_URL():
        url = config.get('commonInfo', 'base_URL')
        return url

    # reading common info username
    @staticmethod
    def get_username():
        username = config.get('commonInfo', 'username')
        return username

    # reading common info password
    @staticmethod
    def get_password():
        password = config.get('commonInfo', 'password')
        return password

    # reading admin info username
    @staticmethod
    def get_admin_username():
        username = config.get('adminInfo', 'username')
        return username

    # reading admin info password
    @staticmethod
    def get_admin_password():
        password = config.get('adminInfo', 'password')
        return password

    @staticmethod
    def get_random_item_name():
        item_list = ['Album', 'Beanie with Logo', 'Cap', 'Belt', 'Sunglasses', 'Single', 'Hoodie with Logo',
                     'Logo Collection', 'Polo', 'Long Sleeve Tee', 'V-Neck T-Shirt']

        return random.choices(item_list)

    @staticmethod
    def get_coupon(coupon="FREE"):

        return coupon
