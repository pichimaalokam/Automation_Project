from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")

    def enter_username(self, text):
        self.driver.find_element(*self.username_locator).send_keys(text)

    def enter_password(self, text):
        self.driver.find_element(*self.password_locator).send_keys(text)

    def click_login(self):
        self.driver.find_element(*self.login_button_locator).click()