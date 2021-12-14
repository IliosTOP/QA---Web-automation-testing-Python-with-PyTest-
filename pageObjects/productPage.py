from selenium.webdriver.common.by import By

from pageObjects.cartPage import CartPage


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    product_name = (By.CSS_SELECTOR, '#tbodyid .name')
    add_to_cart_button = (By.XPATH, '//a[contains(text(), "Add to cart")]')
    cart = (By.CSS_SELECTOR, '#cartur')

    def get_add_to_cart_button(self):
        return self.driver.find_element(*ProductPage.add_to_cart_button)

    def verify_and_accept_product_alert(self):
        alert = self.driver.switch_to.alert
        print("the alert text is: " + alert.text)
        assert alert.text == "Product added."
        alert.accept()

    def verify_product_name(self, expected_product_name):
        actual_name = self.driver.find_element(*ProductPage.product_name)
        print(actual_name.text)
        assert actual_name.text == expected_product_name

    def click_on_cart(self):
        self.driver.find_element(*ProductPage.cart).click()
        on_cart_page = CartPage(self.driver)
        return on_cart_page
