from selenium.webdriver.common.by import By

from pageObjects.productPage import ProductPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    cart = (By.CSS_SELECTOR, "#cartur")
    sign_in = (By.CSS_SELECTOR, "#signin2")
    log_in = (By.CSS_SELECTOR, "#login2")
    sign_in_username_textbox = (By.CSS_SELECTOR, "#sign-username")
    sign_in_password_textbox = (By.CSS_SELECTOR, "#sign-password")
    sign_in_button = (By.CSS_SELECTOR, "[onclick='register()']")
    log_in_button = (By.CSS_SELECTOR, "[onclick='logIn()']")
    log_in_username_textbox = (By.CSS_SELECTOR, "#loginusername")
    log_in_password_textbox = (By.CSS_SELECTOR, "#loginpassword")


    def get_sign_in(self):
        return self.driver.find_element(*HomePage.sign_in)

    def get_sign_in_username(self):
        return self.driver.find_element(*HomePage.sign_in_username_textbox)

    def get_sign_in_password(self):
        return self.driver.find_element(*HomePage.sign_in_password_textbox)

    def get_sign_in_button(self):
        return self.driver.find_element(*HomePage.sign_in_button)

    def get_log_in(self):
        return self.driver.find_element(*HomePage.log_in)

    def get_log_in_username(self):
        return self.driver.find_element(*HomePage.log_in_username_textbox)

    def get_log_in_password(self):
        return self.driver.find_element(*HomePage.log_in_password_textbox)

    def get_log_in_button(self):
        return self.driver.find_element(*HomePage.log_in_button)

    def verify_and_accept_sign_in_alert(self):
        alert = self.driver.switch_to.alert
        assert alert.text == "Sign up successful."
        print("the alert text is: " + alert.text)
        alert.accept()

    def click_on_product_by_name(self, product_name):
        self.driver.find_element_by_xpath(f"//a[contains(text(), '{product_name}')]").click()
        on_product_page = ProductPage(self.driver)
        return on_product_page

