import time

import pytest

from pageObjects.homePage import HomePage
from testData.storeData import StoreData
from utilities.baseClass import BaseClass


class TestOne(BaseClass):
    def test_sign_in(self, get_data):
        on_home_page = HomePage(self.driver)
        on_home_page.get_sign_in().click()
        on_home_page.get_sign_in_username().send_keys(get_data['username'])
        on_home_page.get_sign_in_password().send_keys(get_data['password'])
        on_home_page.get_sign_in_button().click()
        time.sleep(2)
        on_home_page.verify_and_accept_sign_in_alert()

    def test_log_in(self, get_data):
        log = self.get_logger()
        log.info('with this log I can use logging during the test, the logs will be saved in reports/logfile.log')
        on_home_page = HomePage(self.driver)
        on_home_page.get_log_in().click()
        on_home_page.get_log_in_username().send_keys(get_data['username'])
        on_home_page.get_log_in_password().send_keys(get_data['password'])
        on_home_page.get_log_in_button().click()

    def test_add_product(self):
        log = self.get_logger()
        log.info('with this log I use logging during the test, the logs will be saved in reports/logfile.log')
        on_home_page = HomePage(self.driver)
        time.sleep(2)
        on_product_page = on_home_page.click_on_product_by_name('Samsung galaxy s6')
        on_product_page.verify_product_name('Samsung galaxy s6')
        on_product_page.get_add_to_cart_button().click()
        time.sleep(2)
        on_product_page.verify_and_accept_product_alert()
        on_cart_page = on_product_page.click_on_cart()
        time.sleep(2)
        on_cart_page.verify_product_amount(1)
        on_cart_page.get_place_order_button().click()

    @pytest.fixture(params=StoreData.get_test_data('valid1'))
    def get_data(self, request):
        return request.param
