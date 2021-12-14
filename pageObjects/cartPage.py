from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    product_row = (By.CSS_SELECTOR, '#tbodyid tr')
    place_order_button = (By.XPATH, '//button[contains(text(), "Place Order")]')

    def verify_product_amount(self, expected_product_amount):
        actual_product_amount = len(self.driver.find_elements(*CartPage.product_row))
        print('the actual product amount is: ' + str(actual_product_amount))
        assert expected_product_amount == actual_product_amount

    def get_place_order_button(self):
        return self.driver.find_element(*CartPage.place_order_button)
