from selenium.webdriver.common.by import By

class InventoryPage:
    backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text